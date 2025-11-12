import smtplib
from email.mime.text import MIMEText
import os

# Load credentials
EMAIL_USER = os.getenv("EMAIL_USER") or "geeti8058@gmail.com"
EMAIL_PASS = os.getenv("EMAIL_PASS") or "ediv djqh esry xadq"

# Recipient for testing
recipient = "yourgmail@gmail.com"  # you can even send it to yourself

msg = MIMEText("This is a test email from Present OS.")
msg["Subject"] = "✅ Gmail SMTP Test Successful"
msg["From"] = EMAIL_USER
msg["To"] = recipient

try:
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL_USER, EMAIL_PASS)
        server.sendmail(EMAIL_USER, recipient, msg.as_string())

    print("✅ Email sent successfully! Check your inbox.")
except smtplib.SMTPAuthenticationError as e:
    print("❌ Authentication failed — Gmail rejected the credentials.")
    print("Reason:", e)
except Exception as e:
    print("❌ Something went wrong:", e)
