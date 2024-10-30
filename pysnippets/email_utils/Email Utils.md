# Python Email Utilities Package
This module provides a comprehensive guide for handling various email operations using Python's `smtplib` and `email` modules.

## Table of Contents
- [Installation](#installation)
- [Features](#features)
- [Configuration](#configuration)
- [Usage Examples](#usage-examples)
- [API Reference](#api-reference)
- [Testing](#testing)
- [Contributing](#contributing)

## Installation
```bash
pip install -r requirements.txt
```

Requirements:
```text
aiosmtplib>=2.0.0  # For async email support
python-dotenv>=0.19.0  # For environment variable management
```

## Features
- ✉️ Basic SMTP email sending
- 🎨 HTML-formatted emails
- 👥 Multiple recipient support
- 📎 File attachments
- 🖼️ Embedded images in HTML
- ⚡ Asynchronous sending
- 📨 Bulk email support
- 🔒 SSL/TLS support
- 📝 Email templates
- ✅ Comprehensive testing suite

## Configuration

### Environment Variables
Create a `.env` file in your project root:
```env
SMTP_HOST=smtp.gmail.com
SMTP_PORT=587
SMTP_USERNAME=your.email@gmail.com
SMTP_PASSWORD=your-app-password
```

### Basic Setup
```python
from email_utils import EmailClient

# Create email client instance
email_client = EmailClient(
    host="smtp.gmail.com",
    port=587,
    username="your.email@gmail.com",
    password="your-app-password"
)
```

## Usage Examples

### 1. Send Basic Text Email
```python
from email_utils import EmailClient

client = EmailClient.from_env()
result = client.send_text_email(
    to="recipient@example.com",
    subject="Hello!",
    body="This is a test email."
)
```

### 2. Send HTML Email
```python
html_content = """
<html>
    <body>
        <h1>Welcome!</h1>
        <p>This is a <b>HTML</b> email.</p>
    </body>
</html>
"""

client.send_html_email(
    to="recipient@example.com",
    subject="HTML Test",
    html_body=html_content
)
```

### 3. Send to Multiple Recipients
```python
recipients = [
    "user1@example.com",
    "user2@example.com",
    "user3@example.com"
]

client.send_text_email(
    to=recipients,
    subject="Group Message",
    body="This is a group email."
)
```

### 4. Send Email with Attachments
```python
attachments = [
    "path/to/document.pdf",
    "path/to/image.jpg"
]

client.send_email_with_attachments(
    to="recipient@example.com",
    subject="Files Attached",
    body="Please find the attached files.",
    attachments=attachments
)
```

### 5. Send HTML Email with Embedded Images
```python
html_content = """
<html>
    <body>
        <h1>Product Information</h1>
        <img src="cid:product_image" alt="Product">
    </body>
</html>
"""

client.send_html_email_with_images(
    to="recipient@example.com",
    subject="Product Details",
    html_body=html_content,
    images={"product_image": "path/to/product.jpg"}
)
```

### 6. Async Email Sending
```python
import asyncio

async def send_emails():
    async_client = AsyncEmailClient.from_env()
    
    tasks = [
        async_client.send_text_email(
            to=f"user{i}@example.com",
            subject=f"Async Email {i}",
            body=f"This is async email {i}"
        )
        for i in range(5)
    ]
    
    results = await asyncio.gather(*tasks)
    return results

# Run async function
asyncio.run(send_emails())
```

### 7. Bulk Email Sending
```python
from email_utils import BulkEmailSender

recipients = [
    {"email": "user1@example.com", "name": "User 1"},
    {"email": "user2@example.com", "name": "User 2"},
    # ... more recipients
]

template = """
Hello {name},
This is a personalized message for you.
"""

bulk_sender = BulkEmailSender(
    client=email_client,
    batch_size=50,  # Send 50 emails per batch
    delay=1.0       # 1 second delay between batches
)

results = bulk_sender.send_bulk_emails(
    recipients=recipients,
    subject="Bulk Email",
    template=template
)
```

## API Reference

### EmailClient
Main class for handling email operations.

#### Methods:
- `send_text_email(to, subject, body)`
- `send_html_email(to, subject, html_body)`
- `send_email_with_attachments(to, subject, body, attachments)`
- `send_html_email_with_images(to, subject, html_body, images)`

### AsyncEmailClient
Asynchronous version of EmailClient.

#### Methods:
- `async send_text_email(to, subject, body)`
- `async send_html_email(to, subject, html_body)`
- `async send_email_with_attachments(to, subject, body, attachments)`

### BulkEmailSender
Class for handling bulk email operations.

#### Methods:
- `send_bulk_emails(recipients, subject, template)`
- `send_bulk_html_emails(recipients, subject, html_template)`


## Error Handling

The package includes comprehensive error handling:

```python
from email_utils.exceptions import (
    EmailError,
    SMTPConnectionError,
    AttachmentError,
    TemplateError
)

try:
    client.send_text_email(...)
except SMTPConnectionError as e:
    print(f"SMTP Connection failed: {e}")
except EmailError as e:
    print(f"Email sending failed: {e}")
```

## Best Practices

1. **Environment Management**
   - Always use environment variables for sensitive data
   - Never hardcode credentials

2. **Rate Limiting**
   - Use bulk sender with appropriate batch sizes
   - Implement delays between batches

3. **Error Handling**
   - Always wrap email operations in try-except blocks
   - Log errors appropriately

4. **Testing**
   - Use test SMTP servers for development
   - Mock SMTP connections in tests

