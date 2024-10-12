import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


def send_email(
    sender_email,
    sender_password,
    recepient_email,
    subject,
    body,
    smtp_server="smtp.gmail.com",
    smtp_port=587,
):
    """
    Sends an email using the provided SMTP server.

    Args:
        sender_email (str): The email address of the sender.
        sender_password (str): The password for the sender's email account.
        recepient_mail (str): The email address of the recepient.
        subject (str): The subject of the email.
        body (str): The body of the email.
        smtp_server (str, optional): The SMTP server to use. Defaults to 'smtp.gmail.com'.
        smtp_port (int, optional): The port to use for the SMTP server. Defaults to 587.

    Raises:
        smtplib.SMTPAuthenticationError: If authentication fails.
        smtplib.SMTPException: If there's an error sending the email.

    Example:
        send_email(
            "aashishnkumar@gmail.com",
            "your_password",
            "aashishnandakumar.official.in@gmail.com",
            "Test Subject",
            "This is a test email",
        )
    """
    # create the email message
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = recepient_email
    message["Subject"] = subject

    # attach the body of the email
    message.attach(MIMEText(body, "plain"))

    try:
        # create a secure SSL/TLS connection
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            # login to the email account
            server.login(sender_email, sender_password)
            # send the email
            server.send_message(message)
        print("Email sent successfully!")
    except smtplib.SMTPAuthenticationError:
        print(
            "SMTP Authentication Error: The server didn't accept the username/password combination."
        )
        raise
    except smtplib.SMTPException as e:
        print(f"SMTP Error: An error occured while sending the email: {str(e)}")
        raise


if __name__ == "__main__":
    # NOTE: Never hardcode sensitive information like this in practice
    send_email(
        "sender@gmail.com",
        "password",
        "receiver@gmail.com",
        "Test Subject",
        "This is a test Email",
    )
