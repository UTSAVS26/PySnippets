import unittest
import os
from unittest.mock import patch, Mock
from pysnippets.email_utils.client import EmailClient, AsyncEmailClient
from pysnippets.email_utils.bulk import BulkEmailSender
from pysnippets.email_utils.exceptions import SMTPConnectionError, AttachmentError


class TestEmailUtils(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.email_client = EmailClient(
            host="test.smtp.com",
            port=587,
            username="test@example.com",
            password="testpass"
        )
        cls.temp_dir = "temp_test_files"
        os.makedirs(cls.temp_dir, exist_ok=True)
    
    @classmethod
    def tearDownClass(cls):
        # Clean up any created files or directories
        for file in os.listdir(cls.temp_dir):
            os.remove(os.path.join(cls.temp_dir, file))
        os.rmdir(cls.temp_dir)

    @patch('smtplib.SMTP')
    def test_send_text_email(self, mock_smtp):
        to = "recipient@example.com"
        subject = "Test Subject"
        body = "Test Body"
        result = self.email_client.send_text_email(to, subject, body)
        
        self.assertTrue(result)
        mock_smtp.return_value.__enter__.return_value.send_message.assert_called_once()

    @patch('smtplib.SMTP')
    def test_send_html_email(self, mock_smtp):
        to = "recipient@example.com"
        subject = "Test Subject"
        html_body = "<html><body>Test</body></html>"
        
        result = self.email_client.send_html_email(to, subject, html_body)
        self.assertTrue(result)
        mock_smtp.return_value.__enter__.return_value.send_message.assert_called_once()

    @patch('smtplib.SMTP')
    def test_send_email_with_attachments(self, mock_smtp):
        to = "recipient@example.com"
        subject = "Test Subject"
        body = "Test Body"
        
        # Create a temporary test file
        test_file = os.path.join(self.temp_dir, "test.txt")
        with open(test_file, "w") as f:
            f.write("Test content")
        
        result = self.email_client.send_email_with_attachments(to, subject, body, [test_file])
        self.assertTrue(result)
        mock_smtp.return_value.__enter__.return_value.send_message.assert_called_once()

    @patch('aiosmtplib.SMTP')
    async def test_async_send_text_email(self, mock_smtp):
        client = AsyncEmailClient(
            host="test.smtp.com",
            port=587,
            username="test@example.com",
            password="testpass"
        )
        mock_smtp.return_value.send_message = Mock()
        
        result = await client.send_text_email(to="recipient@example.com", subject="Test", body="Test Body")
        
        self.assertTrue(result)
        mock_smtp.return_value.send_message.assert_called_once()

    @patch.object(EmailClient, 'send_text_email')
    def test_bulk_email_sender(self, mock_send):
        bulk_sender = BulkEmailSender(
            client=self.email_client,
            batch_size=2,
            delay=0.1
        )
        
        recipients = [
            {"email": "user1@example.com", "name": "User 1"},
            {"email": "user2@example.com", "name": "User 2"},
            {"email": "user3@example.com", "name": "User 3"}
        ]
        
        template = "Hello {name}!"
        results = bulk_sender.send_bulk_emails(
            recipients=recipients,
            subject="Test",
            template=template
        )
        
        self.assertEqual(len(results), 3)
        self.assertTrue(all(r['status'] == 'success' for r in results))
        self.assertEqual(mock_send.call_count, 3)


if __name__ == '__main__':
    unittest.main()
