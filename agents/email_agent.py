import smtplib
from email.mime.text import MIMEText

def send_email(to_address, subject, body):
    sender = "youremail@gmail.com"
    password = "your_app_password"  # Use app-specific password or env var

    msg = MIMEText(body)
    msg["Subject"] = subject
    msg["From"] = sender
    msg["To"] = to_address

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(msg)
        return f"📧 Email sent to {to_address}!"
    except Exception as e:
        return f"❌ Failed to send email: {e}"
