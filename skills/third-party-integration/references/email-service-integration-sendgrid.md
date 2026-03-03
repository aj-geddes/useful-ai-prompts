# Email Service Integration (SendGrid)

## Email Service Integration (SendGrid)

```javascript
const sgMail = require("@sendgrid/mail");
sgMail.setApiKey(process.env.SENDGRID_API_KEY);

class EmailService {
  async sendEmail(to, templateId, templateData = {}) {
    try {
      const message = {
        to,
        from: process.env.FROM_EMAIL,
        templateId,
        dynamicTemplateData: {
          ...templateData,
          timestamp: new Date().toISOString(),
        },
        trackingSettings: {
          clickTracking: { enabled: true },
          openTracking: { enabled: true },
        },
      };

      const response = await sgMail.send(message);

      // Log email
      await EmailLog.create({
        to,
        templateId,
        messageId: response[0].headers["x-message-id"],
        status: "sent",
        sentAt: new Date(),
      });

      return { success: true, messageId: response[0].headers["x-message-id"] };
    } catch (error) {
      console.error("Email error:", error.message);

      await EmailLog.create({
        to,
        templateId,
        error: error.message,
        status: "failed",
      });

      throw error;
    }
  }

  async sendBulk(recipients, templateId, templateData) {
    const promises = recipients.map((recipient) =>
      this.sendEmail(recipient, templateId, templateData).catch((err) => ({
        recipient,
        error: err.message,
      })),
    );

    return Promise.allSettled(promises);
  }

  async handleWebhook(event) {
    const { messageId, event: eventType } = event;

    await EmailLog.updateOne(
      { messageId },
      { status: eventType, updatedAt: new Date() },
    );
  }
}

// Usage
const emailService = new EmailService();

app.post("/api/send-welcome-email", async (req, res) => {
  const { email, firstName } = req.body;

  const result = await emailService.sendEmail(email, "d-welcome-template-id", {
    firstName,
  });

  res.json(result);
});
```
