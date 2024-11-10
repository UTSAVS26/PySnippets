import asyncio
import unittest

class TestAsync(unittest.IsolatedAsyncioTestCase):
    async def test_simple_task(self):
        async def task():
            return 123
        result = await task()
        self.assertEqual(result, 123)

if __name__ == "__main__":
    unittest.main() 