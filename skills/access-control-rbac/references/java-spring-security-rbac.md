# Java Spring Security RBAC

## Java Spring Security RBAC

```java
// RBACConfiguration.java
package com.example.security;

import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;
import org.springframework.security.config.annotation.method.configuration.EnableGlobalMethodSecurity;
import org.springframework.security.config.annotation.web.builders.HttpSecurity;
import org.springframework.security.web.SecurityFilterChain;

@Configuration
@EnableGlobalMethodSecurity(prePostEnabled = true)
public class RBACConfiguration {

    @Bean
    public SecurityFilterChain filterChain(HttpSecurity http) throws Exception {
        http
            .authorizeHttpRequests(authz -> authz
                // Public endpoints
                .requestMatchers("/api/public/**").permitAll()

                // Role-based access
                .requestMatchers("/api/admin/**").hasRole("ADMIN")
                .requestMatchers("/api/users/**").hasAnyRole("USER", "ADMIN")

                // Permission-based access
                .requestMatchers("/api/posts/**").hasAuthority("posts:read")
                .requestMatchers("/api/posts/create").hasAuthority("posts:create")
                .requestMatchers("/api/posts/*/edit").hasAuthority("posts:update")
                .requestMatchers("/api/posts/*/delete").hasAuthority("posts:delete")

                // Default
                .anyRequest().authenticated()
            )
            .csrf().disable();

        return http.build();
    }
}

// UserController.java with method-level security
import org.springframework.security.access.prepost.PreAuthorize;
import org.springframework.web.bind.annotation.*;

@RestController
@RequestMapping("/api/users")
public class UserController {

    @GetMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN') or #id == authentication.principal.id")
    public User getUser(@PathVariable String id) {
        // Users can view their own profile or admins can view any
        return userService.findById(id);
    }

    @PutMapping("/{id}")
    @PreAuthorize("@accessControl.canUpdateUser(authentication, #id)")
    public User updateUser(@PathVariable String id, @RequestBody User user) {
        return userService.update(id, user);
    }

    @DeleteMapping("/{id}")
    @PreAuthorize("hasRole('ADMIN')")
    public void deleteUser(@PathVariable String id) {
        userService.delete(id);
    }
}

// AccessControlService.java - Custom permission logic
@Service
public class AccessControlService {

    public boolean canUpdateUser(Authentication auth, String userId) {
        // Admins can update anyone
        if (auth.getAuthorities().stream()
            .anyMatch(a -> a.getAuthority().equals("ROLE_ADMIN"))) {
            return true;
        }

        // Users can update themselves
        return auth.getPrincipal().equals(userId);
    }

    public boolean canApproveExpense(Authentication auth, Expense expense) {
        UserDetails user = (UserDetails) auth.getPrincipal();

        // Check if user is manager
        if (!auth.getAuthorities().stream()
            .anyMatch(a -> a.getAuthority().equals("ROLE_MANAGER"))) {
            return false;
        }

        // Check department match
        return user.getDepartment().equals(expense.getDepartment());
    }
}
```
