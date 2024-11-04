import unittest
from unittest.mock import patch, mock_open
import io
import random
import os
import sys

sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Problem2 import print_grid, get_user_guess,update_grid,provide_feedback,save_score, play_game

# Assuming the game functions are imported here

class TestGuessingGame(unittest.TestCase):

#     @patch('sys.stdout', new_callable=io.StringIO)
#     def test_print_grid(self, mock_stdout):
#         grid = [
#             ['10', '', '', ''],
#             ['', '', '', ''],
#             ['', '', '', ''],
#             ['', '', '', ''],
#             ['', '', '', '']
#         ]
#         print_grid(grid)  # Test the grid print function
#         output = mock_stdout.getvalue()
#         expected_output = """GRID OF GUESSES
# -------------------
#  10 |    |    |    
# -------------------
#     |    |    |    
# -------------------
#     |    |    |    
# -------------------
#     |    |    |    
# -------------------
#     |    |    |    
# -------------------
# """
#         self.assertEqual(output.strip(), expected_output.strip())

    @patch('builtins.input', side_effect=['10', '20', '15'])
    @patch('random.randint', return_value=15)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_print_grid(self, mock_stdout, mock_randint, mock_input):
        play_game()  # Test full game flow with a win
        output = mock_stdout.getvalue()
        self.assertIn('10', output)
        self.assertIn('20', output)
        self.assertIn('-', output)
        self.assertIn('|', output)

    @patch('builtins.input', side_effect=['35', '-5', '15'])
    def test_get_user_guess(self, mock_input):
        guess = get_user_guess(1)  # Test input validation
        self.assertEqual(guess, 15)  # Valid guess in range [1, 30]

    # @patch('sys.stdout', new_callable=io.StringIO)
    # def test_update_grid(self, mock_stdout):
    #     grid = [
    #         ['', '', '', ''],
    #         ['', '', '', ''],
    #         ['', '', '', ''],
    #         ['', '', '', ''],
    #         ['', '', '', '']
    #     ]
    #     guesses_made = 0
    #     guess = 10
    #     update_grid(grid, guess, guesses_made)  # Test grid update
    #     output = mock_stdout.getvalue()
    #     self.assertIn('10', output)  # Check if guess was added to the grid

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_provide_feedback_too_small(self, mock_stdout):
        guess = 10
        secret_number = 15
        provide_feedback(guess, secret_number)  # Test feedback for too small guess
        output = mock_stdout.getvalue()
        self.assertIn('Your number is too small', output)

    @patch('sys.stdout', new_callable=io.StringIO)
    def test_provide_feedback_too_big(self, mock_stdout):
        guess = 20
        secret_number = 15
        provide_feedback(guess, secret_number)  # Test feedback for too big guess
        output = mock_stdout.getvalue()
        self.assertIn('Your number is too big', output)

    @patch('builtins.open', new_callable=mock_open)
    def test_save_score(self, mock_file):
        score = 8
        save_score(score)  # Test score saving
        mock_file().write.assert_called_once_with('Final score: 8\n')  # Check file write

    @patch('builtins.input', side_effect=['10', '20', '15'])
    @patch('random.randint', return_value=15)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_win(self, mock_stdout, mock_randint, mock_input):
        play_game()  # Test full game flow with a win
        output = mock_stdout.getvalue()
        self.assertIn('Congrats, you have won!', output)

    @patch('builtins.input', side_effect=['10', '20', '30', '25', '15', '5', '7', '22', '18', '13'])
    @patch('random.randint', return_value=17)
    @patch('sys.stdout', new_callable=io.StringIO)
    def test_play_game_loss(self, mock_stdout, mock_randint, mock_input):
        play_game()  # Test full game flow with a loss
        output = mock_stdout.getvalue()
        self.assertIn('Sorry, you are out of guesses', output)

if __name__ == '__main__':
    unittest.main()  # Uncomment this to run the tests directly
