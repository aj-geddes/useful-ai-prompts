# Node.js XSS Prevention

## Node.js XSS Prevention

```javascript
// xss-prevention.js
const createDOMPurify = require("dompurify");
const { JSDOM } = require("jsdom");
const he = require("he");

const window = new JSDOM("").window;
const DOMPurify = createDOMPurify(window);

class XSSPrevention {
  /**
   * HTML Entity Encoding - Safest for text content
   */
  static encodeHTML(str) {
    return he.encode(str, {
      useNamedReferences: true,
      encodeEverything: false,
    });
  }

  /**
   * Sanitize HTML - For rich content
   */
  static sanitizeHTML(dirty) {
    const config = {
      ALLOWED_TAGS: [
        "p",
        "br",
        "strong",
        "em",
        "u",
        "h1",
        "h2",
        "h3",
        "ul",
        "ol",
        "li",
        "a",
        "img",
        "blockquote",
        "code",
      ],
      ALLOWED_ATTR: ["href", "src", "alt", "title", "class"],
      ALLOWED_URI_REGEXP: /^(?:https?|mailto):/i,
      KEEP_CONTENT: true,
      RETURN_DOM: false,
      RETURN_DOM_FRAGMENT: false,
    };

    return DOMPurify.sanitize(dirty, config);
  }

  /**
   * Strict sanitization - For untrusted HTML
   */
  static sanitizeStrict(dirty) {
    return DOMPurify.sanitize(dirty, {
      ALLOWED_TAGS: ["b", "i", "em", "strong"],
      ALLOWED_ATTR: [],
      KEEP_CONTENT: true,
    });
  }

  /**
   * JavaScript context encoding
   */
  static encodeForJS(str) {
    return str.replace(/[<>"'&]/g, (char) => {
      const escape = {
        "<": "\\x3C",
        ">": "\\x3E",
        '"': "\\x22",
        "'": "\\x27",
        "&": "\\x26",
      };
      return escape[char];
    });
  }

  /**
   * URL parameter encoding
   */
  static encodeURL(str) {
    return encodeURIComponent(str);
  }

  /**
   * Attribute context encoding
   */
  static encodeAttribute(str) {
    return str
      .replace(/&/g, "&amp;")
      .replace(/</g, "&lt;")
      .replace(/>/g, "&gt;")
      .replace(/"/g, "&quot;")
      .replace(/'/g, "&#x27;")
      .replace(/\//g, "&#x2F;");
  }

  /**
   * Validate and sanitize URLs
   */
  static sanitizeURL(url) {
    try {
      const parsed = new URL(url);

      // Only allow safe protocols
      if (!["http:", "https:", "mailto:"].includes(parsed.protocol)) {
        return "";
      }

      return parsed.href;
    } catch {
      return "";
    }
  }

  /**
   * Strip all HTML tags
   */
  static stripHTML(str) {
    return str.replace(/<[^>]*>/g, "");
  }

  /**
   * React-style JSX escaping
   */
  static escapeForReact(str) {
    return {
      __html: DOMPurify.sanitize(str),
    };
  }
}

// Express middleware
function xssProtection(req, res, next) {
  // Sanitize request body
  if (req.body) {
    req.body = sanitizeObject(req.body);
  }

  // Sanitize query parameters
  if (req.query) {
    req.query = sanitizeObject(req.query);
  }

  next();
}

function sanitizeObject(obj) {
  const sanitized = {};

  for (const [key, value] of Object.entries(obj)) {
    if (typeof value === "string") {
      sanitized[key] = XSSPrevention.stripHTML(value);
    } else if (typeof value === "object" && value !== null) {
      sanitized[key] = sanitizeObject(value);
    } else {
      sanitized[key] = value;
    }
  }

  return sanitized;
}

// Express example
const express = require("express");
const app = express();

app.use(express.json());
app.use(xssProtection);

app.post("/api/comments", (req, res) => {
  const { comment } = req.body;

  // Additional sanitization for rich content
  const safeComment = XSSPrevention.sanitizeHTML(comment);

  // Store in database
  // db.comments.insert({ content: safeComment });

  res.json({ comment: safeComment });
});

module.exports = XSSPrevention;
```
