# test_string_matching.py
import unittest

from pysnippets import (
    boyer_moore_string_matching,
    finite_automata_string_matching
)

def test_boyer_moore_string_matching():
    assert boyer_moore_string_matching("ababcababcabc", "abc") == [2, 7, 10]
    assert boyer_moore_string_matching("aaaaa", "aa") == [0, 1, 2, 3]
    assert boyer_moore_string_matching("hello world", "world") == [6]
    assert boyer_moore_string_matching("abcd", "xyz") == []
    assert boyer_moore_string_matching("abababab", "ab") == [0, 2, 4, 6]

def test_finite_automata_string_matching():
    assert finite_automata_string_matching("ababcababcabc", "abc") == [2, 7, 10]
    assert finite_automata_string_matching("aaaaa", "aa") == [0, 1, 2, 3]
    assert finite_automata_string_matching("hello world", "world") == [6]
    assert finite_automata_string_matching("abcd", "xyz") == []
    assert finite_automata_string_matching("abababab", "ab") == [0, 2, 4, 6]

if __name__ == "__main__":
    unittest.main()
