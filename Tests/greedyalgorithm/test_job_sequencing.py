import unittest
from pysnippets.greedyalgorithm.job_sequencing import Job, job_sequencing

class TestJobSequencing(unittest.TestCase):
    def test_max_profit_sequence(self):
        jobs = [
            Job('a', 4, 20),
            Job('b', 1, 10),
            Job('c', 1, 40),
            Job('d', 1, 30)
        ]
        n = 4
        expected_sequence = ['c', 'a']
        self.assertEqual(job_sequencing(jobs, n), expected_sequence)

    def test_single_job(self):
        jobs = [Job('a', 1, 10)]
        n = 1
        expected_sequence = ['a']
        self.assertEqual(job_sequencing(jobs, n), expected_sequence)

    def test_all_jobs_same_deadline(self):
        jobs = [
            Job('a', 1, 10),
            Job('b', 1, 20),
            Job('c', 1, 30)
        ]
        n = 3
        expected_sequence = ['c']
        self.assertEqual(job_sequencing(jobs, n), expected_sequence)

    def test_no_jobs(self):
        jobs = []
        n = 0
        expected_sequence = []
        self.assertEqual(job_sequencing(jobs, n), expected_sequence)

if __name__ == "__main__":
    unittest.main()
