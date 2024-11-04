import unittest
from unittest.mock import patch
import io
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Problem4 import getWords, getComputerMemoryString, loadWords, askForPlayerGuess, numMatchingLetters, main

class TestHackingMinigame(unittest.TestCase):

    @patch('random.choice')
    @patch('random.sample')
    def test_get_words(self, mock_sample, mock_choice):
        mock_choice.return_value = 'MONITOR'
        # mock_sample.return_value = [3, 6, 9]
        mock_sample.return_value = ['MONITOR', 'ABALONE', 'ABANDON', 'ABILITY', 'ABOLISH', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY']
        
        global WORDS
        # WORDS = ['MONITOR', 'COMPUTER', 'DISPLAY', 'RANDOMLY', 'SOMETHIN', 'CONTAINS', 'ANOTHERW']
        WORDS = ['MONITOR', 'ABALONE', 'ABANDON', 'ABILITY', 'ABOLISH', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY']
        words = getWords()  # Call the function to be tested
        
        self.assertEqual(len(words), 12)
        self.assertIn('MONITOR', words)

    @patch('random.choice')
    @patch('random.sample')
    def test_get_computer_memory_string(self, mock_sample, mock_choice):
        # mock_sample.return_value = [0, 2]
        mock_sample.return_value = ['MONITOR', 'ABALONE', 'ABANDON', 'ABILITY', 'ABOLISH', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY']
        # mock_choice.side_effect = ['#', '@', '%']
        mock_choice.side_effect = lambda x: '#'
        
        words = ['MONITOR', 'COMPUTE', 'ABANDON', 'ABILITY', 'ABOLISH', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY']
        memory_string = getComputerMemoryString(words)  # Call the function to be tested
        
        self.assertIn('MONITOR', memory_string)
        self.assertIn('COMPUTE', memory_string)

    @patch('builtins.input', return_value='MONITOR')
    def test_valid_guess(self, mock_input):
        # words = ['MONITOR', 'COMPUTE', 'DISPLAY']
        words = ['MONITOR', 'ABALONE', 'ABANDON', 'ABILITY', 'ABOLISH', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY']
        guess = askForPlayerGuess(words, 3)  # Call the function to be tested
        
        self.assertEqual(guess, 'MONITOR')

    @patch('builtins.input', side_effect=['INVALID', 'COMPUTE'])
    def test_invalid_guess(self, mock_input):
        words = ['COMPUTE', 'ABALONE', 'ABANDON', 'ABILITY', 'ABOLISH', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY']
        guess = askForPlayerGuess(words, 3)  # Call the function to be tested
        
        self.assertEqual(guess, 'COMPUTE')  # It should prompt until valid input

    def test_num_matching_letters(self):
        self.assertEqual(numMatchingLetters('MONITOR', 'DISPLAY'), 0)
        self.assertEqual(numMatchingLetters('MONITOR', 'COMPANY'), 1)
        self.assertEqual(numMatchingLetters('MONITOR', 'MONITOR'), 7)

    # @patch('builtins.open', new_callable=unittest.mock.mock_open, read_data="monitor\ndisplay\ncompany\n")
    # def test_load_words_from_file(self, mock_open):
    #     loadWords()  # Call the function to load words
    #     self.assertEqual(WORDS, ['MONITOR', 'DISPLAY', 'COMPANY'])

    @patch('builtins.input', side_effect=['COMPANY', 'MONITOR'])
    # @patch('random.sample', return_value=[0, 1])
    @patch('random.sample', return_value=['MONITOR', 'COMPANY', 'DISPLAY', 'ANOTHER', 'INVALID', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY'])
    @patch('random.choice', return_value='MONITOR')
    def test_game_win(self, mock_choice, mock_sample, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()  # Call the main function to run the game
            output = mock_stdout.getvalue()
            self.assertIn('A C C E S S G R A N T E D', output)

    @patch('builtins.input', side_effect=['COMPANY', 'DISPLAY', 'ANOTHER', 'INVALID'])
    # @patch('random.sample', return_value=[0, 1])
    @patch('random.sample', return_value=['MONITOR', 'COMPANY', 'DISPLAY', 'ANOTHER', 'INVALID', 'ABDOMEN', 'ABRAHAM', 'ABYSSAL', 'ACADEMY', 'ACCOUNT', 'ACHIEVE', 'ACIDITY'])
    @patch('random.choice', return_value='MONITOR')
    def test_game_loss(self, mock_choice, mock_sample, mock_input):
        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            main()  # Call the main function to run the game
            output = mock_stdout.getvalue()
            self.assertIn('Out of tries. Secret password was MONITOR.', output)

if __name__ == '__main__':
    unittest.main()  # Uncomment to run tests
