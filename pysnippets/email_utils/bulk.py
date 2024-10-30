import time
from typing import List, Dict, Any
from .client import EmailClient
from .exceptions import TemplateError

class BulkEmailSender:
    def __init__(
        self,
        client: EmailClient,
        batch_size: int = 50,
        delay: float = 1.0
    ):
        self.client = client
        self.batch_size = batch_size
        self.delay = delay

    def send_bulk_emails(
        self,
        recipients: List[Dict[str, Any]],
        subject: str,
        template: str
) -> List[Dict[str, Any]]:
        """
        Send bulk emails using a template.
        
        Args:
            recipients: List of dictionaries containing recipient data
            subject: Email subject
            template: Email template with placeholders
            
        Returns:
            List of dictionaries with sending results
        """
        results = []
        
        for i in range(0, len(recipients), self.batch_size):
            batch = recipients[i:i + self.batch_size]
            
            for recipient in batch:
                try:
                    # Format template with recipient data
                    email_body = template.format(**recipient)
                    
                    # Send email
                    self.client.send_text_email(
                        to=recipient['email'],
                        subject=subject,
                        body=email_body
                    )
                    
                    results.append({
                        'email': recipient['email'],
                        'status': 'success',
                        'error': None
                    })
                except Exception as e:
                    results.append({
                        'email': recipient['email'],
                        'status': 'failed',
                        'error': str(e)
                    })
            
            # Delay between batches
            if i + self.batch_size < len(recipients):
                time.sleep(self.delay)
        
        return results

    def send_bulk_html_emails(
        self,
        recipients: List[Dict[str, Any]],
        subject: str,
        html_template: str,
        text_template: str = None
    ) -> List[Dict[str, Any]]:
        """
        Send bulk HTML emails using a template.
        
        Args:
            recipients: List of dictionaries containing recipient data
            subject: Email subject
            html_template: HTML email template
            text_template: Optional plain text template
        """
        results = []
        
        for i in range(0, len(recipients), self.batch_size):
            batch = recipients[i:i + self.batch_size]
            
            for recipient in batch:
                try:
                    # Format templates with recipient data
                    html_body = html_template.format(**recipient)
                    text_body = text_template.format(**recipient) if text_template else None
                    
                    # Send email
                    self.client.send_html_email(
                        to=recipient['email'],
                        subject=subject,
                        html_body=html_body,
                        text_body=text_body
                    )
                    
                    results.append({
                        'email': recipient['email'],
                        'status': 'success',
                        'error': None
                    })
                except Exception as e:
                    results.append({
                        'email': recipient['email'],
                        'status': 'failed',
                        'error': str(e)
                    })
            
            # Delay between batches
            if i + self.batch_size < len(recipients):
                time.sleep(self.delay)
        
        return results