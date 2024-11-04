import smtplib
import os
import logging
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

# Configure logging
logging.basicConfig(level=logging.INFO)

def send_email(
    sender_email: str,
    sender_password: str,
    recipient_email: str,
    subject: str,
    body: str,
    content_type: str = "plain",
    smtp_server: str = "smtp.gmail.com",
    smtp_port: int = 587,
) -> bool:
    """
    Sends an email to the specified recipient.

    Args:
        sender_email (str): The sender's email address.
        sender_password (str): The password for the sender's email account.
        recipient_email (str): The recipient's email address.
        subject (str): The subject line of the email.
        body (str): The content of the email.
        content_type (str, optional): The format of the email body, either 'plain' or 'html'. Defaults to 'plain'.
        smtp_server (str, optional): The SMTP server to connect to. Defaults to 'smtp.gmail.com'.
        smtp_port (int, optional): The port to use for the SMTP server. Defaults to 587.

    Returns:
        bool: True if the email is sent successfully, False otherwise.
    """
    # Validate input parameters
    if not all([sender_email, sender_password, recipient_email, subject, body]):
        logging.error("All parameters must be provided.")
        return False

    # create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recipient_email
    message["Subject"] = subject

    # attach the body of the email
    message.attach(MIMEText(body, content_type))

    try:
        # create a secure SSL/TLS connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # login to the email account
            server.login(sender_email, sender_password)
            # send the email
            server.send_message(message)
        logging.info("Email sent successfully!")
        return True
    except smtplib.SMTPAuthenticationError:
        logging.error("SMTP Authentication Error: Please check your credentials.")
    except smtplib.SMTPConnectError:
        logging.error("SMTP Connection Error: Unable to connect to the SMTP server.")
    except smtplib.SMTPServerDisconnected:
        logging.error("SMTP Disconnection Error: The server unexpectedly disconnected.")
    except smtplib.SMTPException as e:
        logging.error(f"SMTP Error: An error occurred while sending the email: {str(e)}")
    except Exception as e:
        logging.error(f"Network Error: A network-related error occurred: {str(e)}")
    
    return False

if __name__ == "__main__":
    # Load credentials from environment variables for security
    sender_email = os.getenv("SENDER_EMAIL")
    sender_password = os.getenv("SENDER_PASSWORD")

    # Ensure credentials are provided
    if not sender_email or not sender_password:
        logging.error("Error: Please set the SENDER_EMAIL and SENDER_PASSWORD environment variables.")
    else:
        send_email(
            sender_email=sender_email,
            sender_password=sender_password,
            recipient_email="receiver@gmail.com",
            subject="Test Subject",
            body="<h1>This is a test email</h1><p>This email contains HTML formatting.</p>",
            content_type="html"
        )