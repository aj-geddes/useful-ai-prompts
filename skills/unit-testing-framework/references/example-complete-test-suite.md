# Example: Complete Test Suite

```typescript
// user-service.test.ts
import { UserService } from "./user-service";
import { Database } from "./database";
import { EmailService } from "./email-service";

// Mock dependencies
jest.mock("./database");
jest.mock("./email-service");

describe("UserService", () => {
  let userService: UserService;
  let mockDatabase: jest.Mocked<Database>;
  let mockEmailService: jest.Mocked<EmailService>;

  beforeEach(() => {
    mockDatabase = new Database() as jest.Mocked<Database>;
    mockEmailService = new EmailService() as jest.Mocked<EmailService>;
    userService = new UserService(mockDatabase, mockEmailService);
  });

  afterEach(() => {
    jest.clearAllMocks();
  });

  describe("createUser", () => {
    const validUserData = {
      email: "john@example.com",
      firstName: "John",
      lastName: "Doe",
    };

    it("should create user successfully", async () => {
      // Arrange
      const savedUser = { id: "123", ...validUserData };
      mockDatabase.save.mockResolvedValue(savedUser);

      // Act
      const result = await userService.createUser(validUserData);

      // Assert
      expect(result).toEqual(savedUser);
      expect(mockDatabase.save).toHaveBeenCalledWith(
        expect.objectContaining(validUserData),
      );
      expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith(
        validUserData.email,
      );
    });

    it("should throw ValidationError for invalid email", async () => {
      const invalidData = { ...validUserData, email: "invalid" };

      await expect(userService.createUser(invalidData)).rejects.toThrow(
        "Invalid email format",
      );

      expect(mockDatabase.save).not.toHaveBeenCalled();
    });

    it("should handle database errors", async () => {
      mockDatabase.save.mockRejectedValue(new Error("DB Error"));

      await expect(userService.createUser(validUserData)).rejects.toThrow(
        "Failed to create user",
      );
    });

    it("should continue even if welcome email fails", async () => {
      const savedUser = { id: "123", ...validUserData };
      mockDatabase.save.mockResolvedValue(savedUser);
      mockEmailService.sendWelcomeEmail.mockRejectedValue(
        new Error("Email failed"),
      );

      const result = await userService.createUser(validUserData);

      expect(result).toEqual(savedUser);
      // User still created even though email failed
    });
  });

  describe("getUserById", () => {
    it("should return user when found", async () => {
      const user = { id: "123", email: "john@example.com" };
      mockDatabase.findById.mockResolvedValue(user);

      const result = await userService.getUserById("123");

      expect(result).toEqual(user);
    });

    it("should throw NotFoundError when user not found", async () => {
      mockDatabase.findById.mockResolvedValue(null);

      await expect(userService.getUserById("999")).rejects.toThrow(
        "User not found",
      );
    });
  });
});
```
