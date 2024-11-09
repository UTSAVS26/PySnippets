import smtplib
from email.message import EmailMessage
from dataclasses import dataclass, field
from typing import List, Optional
import logging
import os
from email.utils import make_msgid
from email.headerregistry import Address


@dataclass
class EmailConfig:
    smtp_server: str
    smtp_port: int
    username: str
    password: str
    use_tls: bool = True


@dataclass
class EmailContent:
    subject: str
    body: str
    sender: str
    recipients: List[str]
    attachments: Optional[List[str]] = field(default_factory=list)


class EmailSender:
    def __init__(self, config: EmailConfig):
        self.config = config
        self.logger = logging.getLogger(self.__class__.__name__)

    def send_email(self, content: EmailContent, html: bool = False) -> None:
        try:
            msg = EmailMessage()
            msg['Subject'] = content.subject
            msg['From'] = content.sender
            msg['To'] = ', '.join(content.recipients)
            if html:
                msg.add_alternative(content.body, subtype='html')
            else:
                msg.set_content(content.body)

            for file_path in content.attachments:
                with open(file_path, 'rb') as f:
                    file_data = f.read()
                    file_name = os.path.basename(f.name)
                msg.add_attachment(file_data, maintype='application', subtype='octet-stream', filename=file_name)

            with smtplib.SMTP(self.config.smtp_server, self.config.smtp_port) as server:
                if self.config.use_tls:
                    server.starttls()
                server.login(self.config.username, self.config.password)
                server.send_message(msg)
            self.logger.info("Email sent successfully.")
        except Exception as e:
            self.logger.error(f"Failed to send email: {e}")
            raise 