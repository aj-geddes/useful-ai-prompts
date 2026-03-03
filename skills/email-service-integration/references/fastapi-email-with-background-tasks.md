# FastAPI Email with Background Tasks

## FastAPI Email with Background Tasks

```python
# email_service.py
from fastapi import BackgroundTasks
from fastapi_mail import FastMail, MessageSchema, ConnectionConfig

conf = ConnectionConfig(
    mail_server=os.getenv("MAIL_SERVER"),
    mail_port=int(os.getenv("MAIL_PORT")),
    mail_from=os.getenv("MAIL_FROM"),
    mail_password=os.getenv("MAIL_PASSWORD"),
    mail_from_name=os.getenv("MAIL_FROM_NAME", "Example App"),
    use_credentials=True,
    validate_certs=True
)

fm = FastMail(conf)

class EmailService:
    @staticmethod
    async def send_email(
        recipients: list,
        subject: str,
        body: str,
        background_tasks: BackgroundTasks = None
    ):
        message = MessageSchema(
            subject=subject,
            recipients=recipients,
            body=body,
            subtype="html"
        )

        if background_tasks:
            background_tasks.add_task(fm.send_message, message)
        else:
            await fm.send_message(message)

    @staticmethod
    async def send_welcome_email(
        email: str,
        name: str,
        background_tasks: BackgroundTasks
    ):
        html_body = f"""
        <h1>Welcome, {name}!</h1>
        <p>Thank you for joining us.</p>
        <a href="https://example.com/dashboard">Start Exploring</a>
        """

        await EmailService.send_email(
            recipients=[email],
            subject="Welcome to Our Platform!",
            body=html_body,
            background_tasks=background_tasks
        )

# routes.py
from fastapi import BackgroundTasks
from email_service import EmailService

@app.post("/api/send-email")
async def send_email(
    email: str,
    background_tasks: BackgroundTasks
):
    await EmailService.send_welcome_email(email, "User", background_tasks)
    return {"message": "Email queued for sending"}
```
