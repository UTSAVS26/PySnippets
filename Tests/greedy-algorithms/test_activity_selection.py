import unittest
from pysnippets.greedyalgorithms.activity_selection import activity_selection

class TestActivitySelection(unittest.TestCase):
    def test_activity_selection(self):
        activities = [
            (1, 3), (2, 5), (4, 7), (6, 8),
            (5, 9), (8, 10), (9, 11)
        ]
        result = activity_selection(activities)
        expected_result = [(1, 3), (4, 7), (8, 10)]
        self.assertEqual(result, expected_result)
        
    def test_no_activities(self):
        activities = []
        result = activity_selection(activities)
        self.assertEqual(result, [])
        
    def test_single_activity(self):
        activities = [(1, 5)]
        result = activity_selection(activities)
        self.assertEqual(result, [(1, 5)])

    def test_non_overlapping_activities(self):
        activities = [(1, 2), (3, 4), (5, 6)]
        result = activity_selection(activities)
        self.assertEqual(result, [(1, 2), (3, 4), (5, 6)])

    def test_all_overlapping_activities(self):
        activities = [(1, 5), (2, 6), (3, 7)]
        result = activity_selection(activities)
        self.assertEqual(result, [(1, 5)])

if __name__ == "__main__":
    unittest.main()
