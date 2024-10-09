import unittest
from pysnippets.utilities.retry import retry


class TestRetryDecorator(unittest.TestCase):

    def test_success_on_first_attempt(self):
        """Test that a function succeeds on the first attempt."""

        @retry(retries=3)
        def always_succeeds():
            return "Success"

        result = always_succeeds()
        self.assertEqual(result, "Success")

    def test_success_after_retry(self):
        """Test that a function succeeds after a few retries."""
        attempts = [0]

        @retry(retries=3)
        def succeeds_after_two_attempts():
            attempts[0] += 1
            if attempts[0] < 3:
                raise ValueError("Failed attempt")
            return "Success"

        result = succeeds_after_two_attempts()
        self.assertEqual(result, "Success")
        self.assertEqual(attempts[0], 3)

    def test_raises_exception_after_retries(self):
        """Test that the last exception is raised after retries are exhausted."""

        @retry(retries=3)
        def always_fails():
            raise ValueError("Always fails")

        with self.assertRaises(ValueError) as context:
            always_fails()

        self.assertEqual(str(context.exception), "Always fails")

    def test_custom_retries(self):
        """Test that the decorator respects a custom number of retries."""
        attempts = [0]

        @retry(retries=5)
        def fails_five_times():
            attempts[0] += 1
            if attempts[0] < 6:  # Fail on the first 5 attempts, succeed on the 6th
                raise ValueError("Failed attempt")
            return "Success"

        result = fails_five_times()
        self.assertEqual(result, "Success")
        self.assertEqual(attempts[0], 6)

    def test_no_retries(self):
        """Test that no retries occur if retries are set to 0."""

        @retry(retries=0)
        def fail_without_retry():
            raise ValueError("No retry")

        with self.assertRaises(ValueError) as context:
            fail_without_retry()

        self.assertEqual(str(context.exception), "No retry")


if __name__ == "__main__":
    unittest.main()
