# test_string_functions.py

import pytest
from string_manipulation import swap_case, to_replace, to_split, to_strip, to_encode, to_decode

def test_swap_case():
    assert swap_case("Apple") == "aPPLE"
    assert swap_case("HELLO world") == "hello WORLD"
    assert swap_case("Python") == "pYTHON"

def test_to_replace():
    assert to_replace("hello world", "hello", "goodbye") == "goodbye world"
    assert to_replace("apple apple", "apple", "orange") == "orange orange"
    assert to_replace("123-456", "-", ":") == "123:456"

def test_to_split():
    assert to_split("a,b,c", ",") == ['a', 'b', 'c']
    assert to_split("hello world", " ") == ['hello', 'world']
    assert to_split("apple:orange:banana", ":") == ['apple', 'orange', 'banana']

def test_to_strip():
    assert to_strip("  hello  ") == "hello"
    assert to_strip("hello\n") == "hello"
    assert to_strip("\tapple\t") == "apple"

def test_to_encode():
    assert to_encode("hello") == b'hello'
    assert to_encode("apple") == b'apple'
    assert to_encode("123") == b'123'

def test_to_decode():
    assert to_decode(b'hello') == 'hello'
    assert to_decode(b'apple') == 'apple'
    assert to_decode(b'123') == '123'


