class EmailError(Exception):
    """Base exception for email operations."""
    pass

class SMTPConnectionError(EmailError):
    """Raised when SMTP connection fails."""
    pass

class AttachmentError(EmailError):
    """Raised when handling attachments fails."""
    pass

class TemplateError(EmailError):
    """Raised when template processing fails."""
    pass