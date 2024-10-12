import unittest
from unittest.mock import (
    mock_open,
    patch,
    MagicMock,
)  # used to simulate complex logic or external services
from pysnippets.Communication.send_email import send_email
import smtplib


class TestSendEmail(unittest.TestCase):

    @patch("smtplib.SMTP")
    def test_send_email_success(self, mock_smtp):
        # setup the mock
        context = MagicMock()
        mock_smtp.return_value.__enter__.return_value = context

        # call the function
        send_email(
            "sender@gmail.com",
            "password",
            "recepient@gmail.com",
            "Test Subject",
            "Test Body",
        )

        # assertions
        mock_smtp.assert_called_once_with("smtp.gmail.com", 587)
        context.starttls.assert_called_once()
        context.login.assert_called_once_with("sender@gmail.com", "password")
        context.send_message.assert_called_once()

    @patch("smtplib.SMTP")
    def test_authentication_error(self, mock_smtp):
        # setup the mock to raise an authentication error
        mock_smtp.return_value.__enter__.return_value.login.side_effect = (
            smtplib.SMTPAuthenticationError(535, b"Invalid credentials")
        )

        # call the function and check for raised exception
        with self.assertRaises(smtplib.SMTPAuthenticationError):
            send_email(
                "sender@gmail.com",
                "password",
                "recepient@gmail.com",
                "Test Subject",
                "Test Body",
            )

    @patch("smtplib.SMTP")
    def test_smtp_error(self, mock_smtp):
        # setup the mock to raise an SMTP error
        mock_smtp.return_value.__enter__.return_value.send_message.side_effect = (
            smtplib.SMTPException("Error sending message")
        )

        # call the function and check for raised exception
        with self.assertRaises(smtplib.SMTPException):
            send_email(
                "sender@gmail.com",
                "password",
                "recepient@gmail.com",
                "Test Subject",
                "Test Body",
            )
