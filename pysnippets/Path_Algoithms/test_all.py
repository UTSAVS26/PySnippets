import unittest

from test_dijkstra import TestDijkstra

def load_tests(loader, tests, pattern):
    tests.addTests(loader.loadTestsFromTestCase(TestDijkstra))
    return tests

if __name__ == '__main__':
    unittest.main() 