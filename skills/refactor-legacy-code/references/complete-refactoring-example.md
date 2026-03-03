# Complete Refactoring Example

## Complete Refactoring Example

### Before

```javascript
// legacy-user-service.js - 200 lines of complex, coupled code
var UserService = {
  createUser: function (fn, ln, em, ph, addr) {
    if (!em || em.indexOf("@") === -1) {
      return { error: "Invalid email" };
    }
    var conn = mysql.createConnection(config);
    conn.connect();
    conn.query(
      "INSERT INTO users (first_name, last_name, email, phone, address) VALUES (?, ?, ?, ?, ?)",
      [fn, ln, em.toLowerCase(), ph, addr],
      function (err, result) {
        if (err) {
          console.log(err);
          return { error: "Database error" };
        }
        // Send welcome email
        var nodemailer = require("nodemailer");
        var transporter = nodemailer.createTransport(emailConfig);
        transporter.sendMail(
          {
            to: em,
            subject: "Welcome!",
            html: "<h1>Welcome " + fn + "!</h1>",
          },
          function (err, info) {
            if (err) console.log(err);
          },
        );
        conn.end();
        return { id: result.insertId };
      },
    );
  },
};
```

### After

```typescript
// user-service.ts - Clean, testable, maintainable
interface UserData {
  firstName: string;
  lastName: string;
  email: string;
  phone: string;
  address: string;
}

class UserService {
  constructor(
    private database: Database,
    private emailService: EmailService,
    private validator: Validator,
  ) {}

  async createUser(userData: UserData): Promise<User> {
    this.validator.validateEmail(userData.email);

    const normalizedData = this.normalizeUserData(userData);
    const user = await this.database.users.create(normalizedData);

    await this.sendWelcomeEmail(user);

    return user;
  }

  private normalizeUserData(data: UserData): UserData {
    return {
      ...data,
      email: data.email.toLowerCase().trim(),
    };
  }

  private async sendWelcomeEmail(user: User): Promise<void> {
    await this.emailService.send({
      to: user.email,
      subject: "Welcome!",
      template: "welcome",
      data: { firstName: user.firstName },
    });
  }
}

// validator.ts
class Validator {
  validateEmail(email: string): void {
    if (!email || !email.includes("@")) {
      throw new ValidationError("Invalid email format");
    }
  }
}

// Easy to test
describe("UserService", () => {
  it("should create user with valid data", async () => {
    const mockDb = createMockDatabase();
    const mockEmail = createMockEmailService();
    const service = new UserService(mockDb, mockEmail, new Validator());

    const user = await service.createUser({
      firstName: "John",
      lastName: "Doe",
      email: "john@example.com",
      phone: "555-0123",
      address: "123 Main St",
    });

    expect(user.id).toBeDefined();
    expect(mockDb.users.create).toHaveBeenCalled();
    expect(mockEmail.send).toHaveBeenCalledWith(
      expect.objectContaining({ to: "john@example.com" }),
    );
  });
});
```
