# Message Types and Protocols

## Message Types and Protocols

```json
// Authentication
{
  "type": "auth",
  "userId": "user123",
  "token": "jwt_token_here"
}

// Chat Message
{
  "type": "message",
  "roomId": "room123",
  "text": "Hello everyone!",
  "timestamp": "2025-01-15T10:30:00Z"
}

// Typing Indicator
{
  "type": "typing",
  "roomId": "room123",
  "isTyping": true
}

// Presence
{
  "type": "presence",
  "status": "online|away|offline"
}

// Notification
{
  "type": "notification",
  "title": "New message",
  "body": "You have a new message",
  "data": {}
}
```
