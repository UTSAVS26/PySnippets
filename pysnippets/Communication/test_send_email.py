import smtplib
import unittest
from unittest.mock import patch, MagicMock
from .send_email import send_email

class TestSendEmail(unittest.TestCase):

    @patch('smtplib.SMTP')
    def test_send_email_success(self, mock_smtp):
        # Arrange
        mock_server = MagicMock()
        mock_smtp.return_value.__enter__.return_value = mock_server
        
        # Act
        result = send_email(
            sender_email="test@gmail.com",
            sender_password="password",
            recipient_email="receiver@gmail.com",
            subject="Test Subject",
            body="This is a test email."
        )
        
        # Assert
        self.assertTrue(result)
        mock_server.send_message.assert_called_once()

    @patch('smtplib.SMTP')
    def test_send_email_authentication_error(self, mock_smtp):
        # Arrange
        mock_smtp.side_effect = smtplib.SMTPAuthenticationError
        
        # Act
        result = send_email(
            sender_email="test@gmail.com",
            sender_password="wrong_password",
            recipient_email="receiver@gmail.com",
            subject="Test Subject",
            body="This is a test email."
        )
        
        # Assert
        self.assertFalse(result)

    @patch('smtplib.SMTP')
    def test_send_email_connection_error(self, mock_smtp):
        # Arrange
        mock_smtp.side_effect = smtplib.SMTPConnectError
        
        # Act
        result = send_email(
            sender_email="test@gmail.com",
            sender_password="password",
            recipient_email="receiver@gmail.com",
            subject="Test Subject",
            body="This is a test email."
        )
        
        # Assert
        self.assertFalse(result)

    def test_send_email_missing_parameters(self):
        # Act
        result = send_email(
            sender_email="",
            sender_password="password",
            recipient_email="receiver@gmail.com",
            subject="Test Subject",
            body="This is a test email."
        )
        
        # Assert
        self.assertFalse(result)

if __name__ == '__main__':
    unittest.main() 