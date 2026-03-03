# REST Assured for Java

## REST Assured for Java

```java
// ContractTest.java
import io.restassured.RestAssured;
import io.restassured.module.jsv.JsonSchemaValidator;
import org.junit.jupiter.api.Test;
import static io.restassured.RestAssured.*;
import static org.hamcrest.Matchers.*;

public class UserAPIContractTest {

    @Test
    public void getUserShouldMatchSchema() {
        given()
            .pathParam("id", "123")
        .when()
            .get("/api/users/{id}")
        .then()
            .statusCode(200)
            .body(JsonSchemaValidator.matchesJsonSchemaInClasspath("schemas/user-schema.json"))
            .body("id", notNullValue())
            .body("email", matchesPattern("^[\\w-\\.]+@([\\w-]+\\.)+[\\w-]{2,4}$"))
            .body("age", greaterThanOrEqualTo(0));
    }

    @Test
    public void createUserShouldValidateRequest() {
        String userJson = """
            {
                "email": "test@example.com",
                "name": "Test User",
                "age": 30
            }
            """;

        given()
            .contentType("application/json")
            .body(userJson)
        .when()
            .post("/api/users")
        .then()
            .statusCode(201)
            .body("id", notNullValue())
            .body("email", equalTo("test@example.com"))
            .body("createdAt", matchesPattern("\\d{4}-\\d{2}-\\d{2}T.*"));
    }

    @Test
    public void getUserOrdersShouldReturnArray() {
        given()
            .pathParam("id", "123")
            .queryParam("limit", 10)
        .when()
            .get("/api/users/{id}/orders")
        .then()
            .statusCode(200)
            .body("orders", isA(java.util.List.class))
            .body("orders[0].id", notNullValue())
            .body("orders[0].status", isIn(Arrays.asList(
                "pending", "paid", "shipped", "delivered", "cancelled"
            )))
            .body("total", greaterThanOrEqualTo(0));
    }

    @Test
    public void invalidRequestShouldReturn400() {
        String invalidUser = """
            {
                "email": "not-an-email",
                "age": -5
            }
            """;

        given()
            .contentType("application/json")
            .body(invalidUser)
        .when()
            .post("/api/users")
        .then()
            .statusCode(400)
            .body("error", notNullValue());
    }
}
```
