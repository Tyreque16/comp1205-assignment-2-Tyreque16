import unittest
from unittest.mock import patch
import random
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Problem3 import englishToSpongecase

class TestSpongecase(unittest.TestCase):

    @patch('random.choice', side_effect=[True, False, True, False])
    def test_spongecase_alternating(self, mock_choice):
        # Testing for controlled randomness with alternating uppercase/lowercase.
        input_text = "mock"
        expected_output = "MoCk"  # Based on the side_effect: T, F, T, F
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

    @patch('random.choice', side_effect=[False, True, False, True, False, True, False, True, False])
    def test_spongecase_mixed(self, mock_choice):
        # Testing controlled randomness on another string
        input_text = "spongebob"
        expected_output = "sPoNgEbOb"  # Based on the side_effect: F, T, F, T, F, T, F, T, F
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

    def test_empty_string(self):
        # Testing if input is an empty string
        input_text = ""
        expected_output = ""  # Expecting empty string back
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

    @patch('random.choice', side_effect=[True, False, True])
    def test_single_word(self, mock_choice):
        # Testing controlled randomness for a single word
        input_text = "hey"
        expected_output = "HeY"
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

    @patch('random.choice', side_effect=[False, True, False, True, False, True, True, True, True, True])
    def test_mixed_characters(self, mock_choice):
        # Test with numbers and special characters, which shouldn't change
        input_text = "Hello 123!"
        expected_output = "hElLo 123!"  # Only letters should be affected
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

    @patch('random.choice', side_effect=[True, False, True, False, True])
    def test_uppercase_sentence(self, mock_choice):
        # Testing uppercase input, checking that all letters get random casing
        input_text = "HELLO"
        expected_output = "HeLlO"
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

    @patch('random.choice', side_effect=[False, True, False, True, False])
    def test_lowercase_sentence(self, mock_choice):
        # Testing lowercase input with random alternation
        input_text = "hello"
        expected_output = "hElLo"
        result = englishToSpongecase(input_text)
        self.assertEqual(result, expected_output)

if __name__ == '__main__':
    unittest.main()  # Uncomment this to run tests directly
