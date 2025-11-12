import os
import smtplib
from email.mime.text import MIMEText

# Try loading environment variables locally
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Try importing Streamlit for cloud secrets
try:
    import streamlit as st
    USE_STREAMLIT_SECRETS = True
except ImportError:
    USE_STREAMLIT_SECRETS = False


# Load credentials
if USE_STREAMLIT_SECRETS and "EMAIL_USER" in st.secrets:
    EMAIL_USER = st.secrets["EMAIL_USER"]
    EMAIL_PASS = st.secrets["EMAIL_PASS"]
    DEMO_MODE = st.secrets.get("DEMO_MODE", "False").lower() == "true"
else:
    EMAIL_USER = os.getenv("EMAIL_USER")
    EMAIL_PASS = os.getenv("EMAIL_PASS")
    DEMO_MODE = os.getenv("DEMO_MODE", "False").lower() == "true"


def send_email(recipient: str, subject: str, body: str) -> str:
    """
    Sends an email using Gmail SMTP.
    Supports Demo Mode for safe public presentations.
    """
    if DEMO_MODE:
        return f"✅ [Demo Mode] Email prepared to {recipient} with subject '{subject}'. (Email not actually sent.)"

    if not EMAIL_USER or not EMAIL_PASS:
        return "⚠️ Email credentials not configured. Please set EMAIL_USER and EMAIL_PASS in environment or Streamlit secrets."

    try:
        msg = MIMEText(body)
        msg["Subject"] = subject
        msg["From"] = EMAIL_USER
        msg["To"] = recipient

        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(EMAIL_USER, EMAIL_PASS)
            server.sendmail(EMAIL_USER, recipient, msg.as_string())

        return f"✅ Email sent successfully to {recipient}!"

    except smtplib.SMTPAuthenticationError:
        return "❌ Authentication failed. Please check your Gmail app password or credentials."
    except Exception as e:
        return f"❌ Failed to send email: {e}"
