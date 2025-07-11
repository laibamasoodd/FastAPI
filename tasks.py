from celery import Celery
from email.message import EmailMessage
import smtplib
import os
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Celery configuration
app = Celery("tasks", broker="redis://redis:6379", backend="redis://redis:6379")


app.conf.update(
    task_ignore_result=False,
    result_backend='redis://redis:6379',
    task_track_started=True,
    task_serializer='json',
    result_serializer='json',
    accept_content=['json'],
)

@app.task
def send_confirmation_email(to_email: str):
    msg = EmailMessage()
    msg["Subject"] = "Welcome to FastAPI App 🎉"
    msg["From"] = "noreply@yourapp.com"
    msg["To"] = to_email
    msg.set_content(f"""
Hi there,

Thanks for signing up for our app!

We're excited to have you onboard 🚀

- Laiba at Bitsol
""")

    smtp_host = os.getenv("MAILTRAP_HOST", "smtp.mailtrap.io")
    smtp_port = int(os.getenv("MAILTRAP_PORT", 587))
    smtp_user = os.getenv("MAILTRAP_USERNAME", "")
    smtp_pass = os.getenv("MAILTRAP_PASSWORD", "")

    try:
        with smtplib.SMTP(smtp_host, smtp_port) as server:
            server.starttls()
            server.login(smtp_user, smtp_pass)
            server.send_message(msg)
        print(f"✅ Confirmation email sent to {to_email}")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")
        raise
