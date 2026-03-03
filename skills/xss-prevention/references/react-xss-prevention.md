# React XSS Prevention

## React XSS Prevention

```javascript
// XSSSafeComponent.jsx
import React from "react";
import DOMPurify from "dompurify";

// Safe text rendering (React automatically escapes)
function SafeText({ text }) {
  return <div>{text}</div>;
}

// Sanitized HTML rendering
function SafeHTML({ html }) {
  const sanitized = DOMPurify.sanitize(html, {
    ALLOWED_TAGS: ["p", "br", "strong", "em", "u", "a"],
    ALLOWED_ATTR: ["href"],
  });

  return <div dangerouslySetInnerHTML={{ __html: sanitized }} />;
}

// Safe URL attribute
function SafeLink({ href, children }) {
  const safeHref = sanitizeURL(href);

  return (
    <a href={safeHref} rel="noopener noreferrer" target="_blank">
      {children}
    </a>
  );
}

function sanitizeURL(url) {
  try {
    const parsed = new URL(url);

    if (!["http:", "https:"].includes(parsed.protocol)) {
      return "";
    }

    return parsed.href;
  } catch {
    return "";
  }
}

// Input sanitization hook
function useSanitizedInput(initialValue = "") {
  const [value, setValue] = React.useState(initialValue);

  const handleChange = (e) => {
    const sanitized = DOMPurify.sanitize(e.target.value, {
      ALLOWED_TAGS: [],
      KEEP_CONTENT: true,
    });

    setValue(sanitized);
  };

  return [value, handleChange];
}

// Usage
function CommentForm() {
  const [comment, handleCommentChange] = useSanitizedInput();

  const handleSubmit = async (e) => {
    e.preventDefault();

    await fetch("/api/comments", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ comment }),
    });
  };

  return (
    <form onSubmit={handleSubmit}>
      <textarea
        value={comment}
        onChange={handleCommentChange}
        placeholder="Enter comment"
      />
      <button type="submit">Submit</button>
    </form>
  );
}

export { SafeText, SafeHTML, SafeLink, useSanitizedInput };
```
