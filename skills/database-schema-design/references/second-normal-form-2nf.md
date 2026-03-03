# Second Normal Form (2NF)

## Second Normal Form (2NF)

**PostgreSQL - Remove Partial Dependencies:**

```sql
-- NOT 2NF: non-key attribute depends on part of composite key
CREATE TABLE enrollment_bad (
  student_id UUID,
  course_id UUID,
  professor_name VARCHAR(255),  -- depends on course_id only
  PRIMARY KEY (student_id, course_id)
);

-- 2NF: separate tables
CREATE TABLE enrollments (
  id UUID PRIMARY KEY,
  student_id UUID NOT NULL,
  course_id UUID NOT NULL,
  FOREIGN KEY (student_id) REFERENCES students(id),
  FOREIGN KEY (course_id) REFERENCES courses(id),
  UNIQUE(student_id, course_id)
);

CREATE TABLE courses (
  id UUID PRIMARY KEY,
  name VARCHAR(255),
  professor_id UUID NOT NULL,
  FOREIGN KEY (professor_id) REFERENCES professors(id)
);
```
