# Jest Mocking (JavaScript/TypeScript)

## Jest Mocking (JavaScript/TypeScript)

### Basic Mocking

```typescript
// services/UserService.ts
import { UserRepository } from "./UserRepository";
import { EmailService } from "./EmailService";

export class UserService {
  constructor(
    private userRepository: UserRepository,
    private emailService: EmailService,
  ) {}

  async createUser(userData: CreateUserDto) {
    const user = await this.userRepository.create(userData);
    await this.emailService.sendWelcomeEmail(user.email, user.name);
    return user;
  }

  async getUserStats(userId: string) {
    const user = await this.userRepository.findById(userId);
    if (!user) throw new Error("User not found");

    const orderCount = await this.userRepository.getOrderCount(userId);
    return { ...user, orderCount };
  }
}

// __tests__/UserService.test.ts
import { UserService } from "../UserService";
import { UserRepository } from "../UserRepository";
import { EmailService } from "../EmailService";

// Mock the dependencies
jest.mock("../UserRepository");
jest.mock("../EmailService");

describe("UserService", () => {
  let userService: UserService;
  let mockUserRepository: jest.Mocked<UserRepository>;
  let mockEmailService: jest.Mocked<EmailService>;

  beforeEach(() => {
    // Clear all mocks before each test
    jest.clearAllMocks();

    // Create mock instances
    mockUserRepository = new UserRepository() as jest.Mocked<UserRepository>;
    mockEmailService = new EmailService() as jest.Mocked<EmailService>;

    userService = new UserService(mockUserRepository, mockEmailService);
  });

  describe("createUser", () => {
    it("should create user and send welcome email", async () => {
      // Arrange
      const userData = {
        email: "test@example.com",
        name: "Test User",
        password: "password123",
      };

      const createdUser = {
        id: "123",
        ...userData,
        createdAt: new Date(),
      };

      mockUserRepository.create.mockResolvedValue(createdUser);
      mockEmailService.sendWelcomeEmail.mockResolvedValue(undefined);

      // Act
      const result = await userService.createUser(userData);

      // Assert
      expect(result).toEqual(createdUser);
      expect(mockUserRepository.create).toHaveBeenCalledWith(userData);
      expect(mockUserRepository.create).toHaveBeenCalledTimes(1);
      expect(mockEmailService.sendWelcomeEmail).toHaveBeenCalledWith(
        userData.email,
        userData.name,
      );
    });

    it("should not send email if user creation fails", async () => {
      // Arrange
      mockUserRepository.create.mockRejectedValue(new Error("Database error"));

      // Act & Assert
      await expect(
        userService.createUser({ email: "test@example.com" }),
      ).rejects.toThrow("Database error");

      expect(mockEmailService.sendWelcomeEmail).not.toHaveBeenCalled();
    });
  });

  describe("getUserStats", () => {
    it("should return user with order count", async () => {
      // Arrange
      const userId = "123";
      const user = { id: userId, name: "Test User" };

      mockUserRepository.findById.mockResolvedValue(user);
      mockUserRepository.getOrderCount.mockResolvedValue(5);

      // Act
      const result = await userService.getUserStats(userId);

      // Assert
      expect(result).toEqual({ ...user, orderCount: 5 });
      expect(mockUserRepository.findById).toHaveBeenCalledWith(userId);
      expect(mockUserRepository.getOrderCount).toHaveBeenCalledWith(userId);
    });

    it("should throw error if user not found", async () => {
      // Arrange
      mockUserRepository.findById.mockResolvedValue(null);

      // Act & Assert
      await expect(userService.getUserStats("999")).rejects.toThrow(
        "User not found",
      );

      expect(mockUserRepository.getOrderCount).not.toHaveBeenCalled();
    });
  });
});
```

### Spying on Functions

```javascript
// services/PaymentService.js
const stripe = require("stripe");

class PaymentService {
  async processPayment(amount, currency, customerId) {
    const charge = await stripe.charges.create({
      amount: amount * 100,
      currency,
      customer: customerId,
    });

    this.logPayment(charge.id, amount);
    return charge;
  }

  logPayment(chargeId, amount) {
    console.log(`Payment processed: ${chargeId} for $${amount}`);
  }
}

// __tests__/PaymentService.test.js
describe("PaymentService", () => {
  let paymentService;
  let stripeMock;

  beforeEach(() => {
    // Mock Stripe module
    stripeMock = {
      charges: {
        create: jest.fn(),
      },
    };
    jest.mock("stripe", () => jest.fn(() => stripeMock));

    paymentService = new PaymentService();
  });

  it("should process payment and log", async () => {
    // Arrange
    const mockCharge = { id: "ch_123", amount: 5000 };
    stripeMock.charges.create.mockResolvedValue(mockCharge);

    // Spy on internal method
    const logSpy = jest.spyOn(paymentService, "logPayment");

    // Act
    await paymentService.processPayment(50, "usd", "cus_123");

    // Assert
    expect(stripeMock.charges.create).toHaveBeenCalledWith({
      amount: 5000,
      currency: "usd",
      customer: "cus_123",
    });
    expect(logSpy).toHaveBeenCalledWith("ch_123", 50);

    logSpy.mockRestore();
  });
});
```
