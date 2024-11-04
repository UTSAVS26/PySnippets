# Overview

This module provides a function to send emails using an SMTP server. The function utilizes the `smtplib` library to establish a connection and send messages securely.

## Table of Contents

1. [Requirements](#requirements)
2. [Function: `send_email`](#function-send_email)
   - [Arguments](#arguments)
   - [Exceptions](#exceptions)
   - [Example Usage](#example-usage)

## Requirements

To use this module, you need Python's built-in `smtplib` and `email` libraries. There are no additional libraries required.

## Function: `send_email`

```python
send_email(
    sender_email,
    sender_password,
    recipient_email,
    subject,
    body,
    content_type="plain",
    smtp_server="smtp.gmail.com",
    smtp_port=587,
)
```

Sends an email using the provided SMTP server.

### Arguments

- **sender_email** (str): The email address of the sender.
- **sender_password** (str): The password for the sender's email account.
- **recipient_email** (str): The email address of the recipient.
- **subject** (str): The subject of the email.
- **body** (str): The body of the email.
- **content_type** (str, optional): The format of the email body, either 'plain' or 'html'. Defaults to 'plain'.
- **smtp_server** (str, optional): The SMTP server to use. Defaults to `'smtp.gmail.com'`.
- **smtp_port** (int, optional): The port to use for the SMTP server. Defaults to `587`.

### Exceptions

- **smtplib.SMTPAuthenticationError**: Raised if authentication fails.
- **smtplib.SMTPException**: Raised if there's an error sending the email.
- **ValueError**: Raised if any required parameters are missing.

### Example Usage

```python
if __name__ == "__main__":
    # NOTE: Never hardcode sensitive information like this in practice
    send_email(
        "sender@gmail.com",
        "password",
        "receiver@gmail.com",
        "Test Subject",
        "This is a test Email",
        content_type="html"
    )
```
