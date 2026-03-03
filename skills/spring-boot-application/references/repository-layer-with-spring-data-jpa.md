# Repository Layer with Spring Data JPA

## Repository Layer with Spring Data JPA

```java
// UserRepository.java
package com.example.repository;

import com.example.model.User;
import org.springframework.data.domain.Page;
import org.springframework.data.domain.Pageable;
import org.springframework.data.jpa.repository.JpaRepository;
import org.springframework.data.jpa.repository.Query;
import org.springframework.stereotype.Repository;
import java.util.Optional;

@Repository
public interface UserRepository extends JpaRepository<User, String> {
    Optional<User> findByEmail(String email);

    @Query("SELECT u FROM User u WHERE u.email LIKE %:search% OR u.firstName LIKE %:search%")
    Page<User> searchUsers(String search, Pageable pageable);

    Page<User> findByRole(User.Role role, Pageable pageable);
}

// PostRepository.java
@Repository
public interface PostRepository extends JpaRepository<Post, String> {
    Page<Post> findByAuthorAndPublishedTrue(User author, Pageable pageable);

    @Query(value = "SELECT p FROM Post p WHERE p.published = true ORDER BY p.createdAt DESC",
           countQuery = "SELECT COUNT(p) FROM Post p WHERE p.published = true")
    Page<Post> findPublishedPosts(Pageable pageable);

    Long countByAuthorId(String authorId);
}
```
