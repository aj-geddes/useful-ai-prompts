# Node.js with SendGrid

## Node.js with SendGrid

```javascript
// email-service.js
const sgMail = require("@sendgrid/mail");
const logger = require("./logger");

sgMail.setApiKey(process.env.SENDGRID_API_KEY);

class EmailService {
  async sendEmail(to, subject, htmlContent, textContent = null) {
    try {
      const msg = {
        to: Array.isArray(to) ? to : [to],
        from: process.env.MAIL_FROM || "noreply@example.com",
        subject: subject,
        html: htmlContent,
        ...(textContent && { text: textContent }),
      };

      const result = await sgMail.send(msg);
      logger.info(`Email sent to ${to}: ${subject}`);
      return { success: true, messageId: result[0].headers["x-message-id"] };
    } catch (error) {
      logger.error(`Failed to send email: ${error.message}`);
      return { success: false, error: error.message };
    }
  }

  async sendWelcomeEmail(to, userName) {
    const htmlContent = `
            <h1>Welcome, ${userName}!</h1>
            <p>Thank you for joining us.</p>
            <a href="https://example.com/dashboard">Start Exploring</a>
        `;

    return this.sendEmail(to, "Welcome to Our Platform!", htmlContent);
  }

  async sendPasswordResetEmail(to, resetToken) {
    const resetUrl = `https://example.com/reset-password?token=${resetToken}`;
    const htmlContent = `
            <h1>Reset Your Password</h1>
            <p>Click the link below to reset your password:</p>
            <a href="${resetUrl}">Reset Password</a>
            <p>This link expires in 24 hours.</p>
        `;

    return this.sendEmail(to, "Reset Your Password", htmlContent);
  }

  async sendVerificationEmail(to, verificationToken) {
    const verifyUrl = `https://example.com/verify-email?token=${verificationToken}`;
    const htmlContent = `
            <h1>Verify Your Email</h1>
            <p>Click the link below to verify your email:</p>
            <a href="${verifyUrl}">Verify Email</a>
        `;

    return this.sendEmail(to, "Verify Your Email", htmlContent);
  }

  async sendBulkEmails(recipients, subject, htmlContent) {
    try {
      const personalizations = recipients.map((recipient) => ({
        to: [{ email: recipient.email }],
        substitutions: {
          "-name-": recipient.name,
        },
      }));

      const msg = {
        personalizations: personalizations,
        from: process.env.MAIL_FROM || "noreply@example.com",
        subject: subject,
        html: htmlContent,
      };

      const result = await sgMail.send(msg);
      logger.info(`Bulk email sent to ${recipients.length} recipients`);
      return { success: true, sent: recipients.length };
    } catch (error) {
      logger.error(`Bulk email failed: ${error.message}`);
      return { success: false, error: error.message };
    }
  }
}

module.exports = new EmailService();

// routes.js
const express = require("express");
const emailService = require("../services/email-service");
const { generateToken } = require("../utils/token");

const router = express.Router();

router.post("/send-verification", async (req, res) => {
  try {
    const { email } = req.body;

    if (!email) {
      return res.status(400).json({ error: "Email required" });
    }

    const verificationToken = generateToken();
    const result = await emailService.sendVerificationEmail(
      email,
      verificationToken,
    );

    if (result.success) {
      // Store token in database
      await VerificationToken.create({ email, token: verificationToken });
      return res.json({ message: "Verification email sent" });
    } else {
      return res.status(500).json({ error: "Failed to send email" });
    }
  } catch (error) {
    logger.error(error);
    res.status(500).json({ error: "Internal server error" });
  }
});

router.post("/send-reset", async (req, res) => {
  try {
    const { email } = req.body;

    const user = await User.findOne({ where: { email } });
    if (!user) {
      return res.json({ message: "If email exists, reset link sent" });
    }

    const resetToken = generateToken();
    const result = await emailService.sendPasswordResetEmail(email, resetToken);

    if (result.success) {
      await ResetToken.create({ userId: user.id, token: resetToken });
      return res.json({ message: "Reset email sent" });
    } else {
      return res.status(500).json({ error: "Failed to send email" });
    }
  } catch (error) {
    res.status(500).json({ error: "Internal server error" });
  }
});

module.exports = router;
```
