# Node.js Secrets Manager with Rotation

## Node.js Secrets Manager with Rotation

```javascript
// secrets-manager.js
const AWS = require("aws-sdk");
const crypto = require("crypto");

class SecretsManager {
  constructor() {
    this.secretsManager = new AWS.SecretsManager({
      region: process.env.AWS_REGION,
    });

    this.rotationSchedule = new Map();
  }

  /**
   * Generate new secret value
   */
  generateSecret(type = "api_key", length = 32) {
    switch (type) {
      case "api_key":
        return crypto.randomBytes(length).toString("hex");

      case "password":
        // Generate strong password
        const chars =
          "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*";
        let password = "";
        for (let i = 0; i < length; i++) {
          password += chars.charAt(crypto.randomInt(chars.length));
        }
        return password;

      case "jwt_secret":
        return crypto.randomBytes(64).toString("base64");

      default:
        return crypto.randomBytes(length).toString("base64");
    }
  }

  /**
   * Store secret in AWS Secrets Manager
   */
  async createSecret(name, value, description = "") {
    const params = {
      Name: name,
      SecretString: JSON.stringify(value),
      Description: description,
    };

    try {
      const result = await this.secretsManager.createSecret(params).promise();
      return result;
    } catch (error) {
      if (error.code === "ResourceExistsException") {
        // Update existing secret
        return this.updateSecret(name, value);
      }
      throw error;
    }
  }

  /**
   * Retrieve secret
   */
  async getSecret(name) {
    const params = { SecretId: name };

    try {
      const data = await this.secretsManager.getSecretValue(params).promise();

      if ("SecretString" in data) {
        return JSON.parse(data.SecretString);
      }

      // Binary secret
      const buff = Buffer.from(data.SecretBinary, "base64");
      return buff.toString("ascii");
    } catch (error) {
      console.error(`Error retrieving secret ${name}:`, error);
      throw error;
    }
  }

  /**
   * Update secret value
   */
  async updateSecret(name, value) {
    const params = {
      SecretId: name,
      SecretString: JSON.stringify(value),
    };

    return this.secretsManager.updateSecret(params).promise();
  }

  /**
   * Rotate secret with zero downtime
   */
  async rotateSecret(name, type = "api_key") {
    console.log(`Starting rotation for secret: ${name}`);

    try {
      // Step 1: Generate new secret
      const newValue = this.generateSecret(type);

      // Step 2: Store new version
      const currentSecret = await this.getSecret(name);

      // Keep old value temporarily for graceful transition
      const secretWithRotation = {
        current: newValue,
        previous: currentSecret.current || currentSecret,
        rotatedAt: new Date().toISOString(),
      };

      await this.updateSecret(name, secretWithRotation);

      console.log(`New secret version created for: ${name}`);

      // Step 3: Wait for applications to pick up new secret
      await this.waitForPropagation(5000);

      // Step 4: Verify new secret works
      const verificationPassed = await this.verifySecret(name, newValue);

      if (!verificationPassed) {
        throw new Error("Secret verification failed");
      }

      // Step 5: Remove previous version after grace period
      setTimeout(async () => {
        await this.updateSecret(name, {
          current: newValue,
          rotatedAt: new Date().toISOString(),
        });
        console.log(`Rotation completed for: ${name}`);
      }, 300000); // 5 minutes grace period

      return {
        success: true,
        secretName: name,
        rotatedAt: new Date().toISOString(),
      };
    } catch (error) {
      console.error(`Rotation failed for ${name}:`, error);

      // Rollback on failure
      await this.rollbackRotation(name);

      throw error;
    }
  }

  /**
   * Schedule automatic rotation
   */
  async scheduleRotation(name, intervalDays = 90) {
    const intervalMs = intervalDays * 24 * 60 * 60 * 1000;

    const rotationJob = setInterval(async () => {
      try {
        await this.rotateSecret(name);
        console.log(`Scheduled rotation completed for: ${name}`);
      } catch (error) {
        console.error(`Scheduled rotation failed for ${name}:`, error);
        // Alert operations team
        this.sendAlert(name, error);
      }
    }, intervalMs);

    this.rotationSchedule.set(name, rotationJob);

    // AWS Secrets Manager automatic rotation
    const params = {
      SecretId: name,
      RotationLambdaARN: process.env.ROTATION_LAMBDA_ARN,
      RotationRules: {
        AutomaticallyAfterDays: intervalDays,
      },
    };

    await this.secretsManager.rotateSecret(params).promise();
  }

  /**
   * Rotate database credentials
   */
  async rotateDatabaseCredentials(secretName) {
    const credentials = await this.getSecret(secretName);

    // Generate new password
    const newPassword = this.generateSecret("password", 20);

    // Update database user password
    const connection = await this.connectToDatabase(credentials);

    await connection.query("ALTER USER ? IDENTIFIED BY ?", [
      credentials.username,
      newPassword,
    ]);

    // Update secret
    await this.updateSecret(secretName, {
      username: credentials.username,
      password: newPassword,
      host: credentials.host,
      database: credentials.database,
      rotatedAt: new Date().toISOString(),
    });

    await connection.end();

    return { success: true };
  }

  /**
   * Rotate TLS certificate
   */
  async rotateTLSCertificate(domain) {
    // Use Let's Encrypt or internal CA
    const certbot = require("certbot");

    try {
      // Request new certificate
      const newCert = await certbot.certonly({
        domains: [domain],
        email: process.env.ADMIN_EMAIL,
        agreeTos: true,
        renewByDefault: true,
      });

      // Store in secrets manager
      await this.createSecret(`tls-cert-${domain}`, {
        certificate: newCert.certificate,
        privateKey: newCert.privateKey,
        chain: newCert.chain,
        issuedAt: new Date().toISOString(),
        expiresAt: newCert.expiresAt,
      });

      // Update load balancer/web server
      await this.updateServerCertificate(domain, newCert);

      console.log(`TLS certificate rotated for: ${domain}`);

      return { success: true };
    } catch (error) {
      console.error("Certificate rotation failed:", error);
      throw error;
    }
  }

  async waitForPropagation(ms) {
    return new Promise((resolve) => setTimeout(resolve, ms));
  }

  async verifySecret(name, value) {
    // Implement verification logic
    // Test API call, database connection, etc.
    return true;
  }

  async rollbackRotation(name) {
    // Restore previous version
    console.log(`Rolling back rotation for: ${name}`);
  }

  async sendAlert(secretName, error) {
    // Send to monitoring system
    console.error(`ALERT: Rotation failed for ${secretName}`, error);
  }

  async connectToDatabase(credentials) {
    // Database connection logic
    return null;
  }

  async updateServerCertificate(domain, cert) {
    // Update server configuration
    return null;
  }
}

// Usage
const secretsManager = new SecretsManager();

// Rotate API key
async function rotateAPIKey() {
  await secretsManager.rotateSecret("api-key-external-service", "api_key");
}

// Schedule automatic rotation
async function setupRotationSchedule() {
  await secretsManager.scheduleRotation("database-credentials", 90);
  await secretsManager.scheduleRotation("api-keys", 30);
}

// Rotate database credentials
async function rotateDatabaseCreds() {
  await secretsManager.rotateDatabaseCredentials("rds-production");
}

module.exports = SecretsManager;
```
