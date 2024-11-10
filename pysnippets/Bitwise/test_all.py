import unittest
from count_bits import count_set_bits
from find_unique import find_unique
from swap import swap_numbers
from power import is_power_of_two
from flip_bit import flip_bit
from clear_lsb_upto_n import clear_lsb_up_to_pos
from isolate_right_one import isolate_rightmost_one

class TestAdvancedBitManipulation(unittest.TestCase):

    def test_count_set_bits(self):
        self.assertEqual(count_set_bits(5), 2)  # 5 in binary is 101
        self.assertEqual(count_set_bits(15), 4)  # 15 in binary is 1111

    def test_find_unique(self):
        self.assertEqual(find_unique([1, 2, 2, 3, 1]), 3)
        self.assertEqual(find_unique([4, 3, 4, 5, 3]), 5)

    def test_swap_numbers(self):
        a, b = swap_numbers(5, 7)
        self.assertEqual(a, 7)
        self.assertEqual(b, 5)

    def test_is_power_of_two(self):
        self.assertTrue(is_power_of_two(8))  # 8 is 2^3
        self.assertFalse(is_power_of_two(10))

    def test_flip_bit(self):
        self.assertEqual(flip_bit(5, 0), 4)  # 5 is 101, flipping LSB gives 100 (4)
        self.assertEqual(flip_bit(5, 2), 1)  # 5 is 101, flipping bit at position 2 gives 001 (1)

    def test_clear_lsb_up_to_pos(self):
        self.assertEqual(clear_lsb_up_to_pos(15, 2), 12)  # Clears LSBs up to pos 2 in 1111, gives 1100 (12)
        self.assertEqual(clear_lsb_up_to_pos(29, 3), 24)  # 29 is 11101, clearing LSBs up to pos 3 gives 11000 (24)

    def test_isolate_rightmost_one(self):
        self.assertEqual(isolate_rightmost_one(12), 4)  # 12 is 1100, isolates rightmost 1 gives 0100 (4)
        self.assertEqual(isolate_rightmost_one(18), 2)  # 18 is 10010, isolates rightmost 1 gives 00010 (2)

if __name__ == "__main__":
    unittest.main()
