import unittest
from io import StringIO
import sys
import os

# Import the functions from the fraction program. You can put the fraction program code in a module and import them.
# For example:
sys.path.insert(1, os.path.join(sys.path[0], '..'))
from Problem1 import is_proper_fraction, convert_to_mixed_fraction, display_fraction_type, main

# Assuming functions from fraction program are available in the current namespace:
# is_proper_fraction, convert_to_mixed_fraction, display_fraction_type

class TestFractionFunctions(unittest.TestCase):

    # Test cases for is_proper_fraction
    def test_is_proper_fraction(self):
        self.assertTrue(is_proper_fraction(6, 7))   # Proper fraction: 6/7
        self.assertFalse(is_proper_fraction(16, 3)) # Improper fraction: 16/3
        self.assertFalse(is_proper_fraction(6, 2))  # Improper fraction: 6/2
        self.assertTrue(is_proper_fraction(2, 3))   # Proper fraction: 2/3

    # Test cases for convert_to_mixed_fraction
    def test_convert_to_mixed_fraction(self):
        self.assertEqual(convert_to_mixed_fraction(16, 3), "5 + 1/3")  # Improper fraction
        self.assertEqual(convert_to_mixed_fraction(6, 2), "3")           # Simplified to integer
        self.assertEqual(convert_to_mixed_fraction(10, 4), "2 + 2/4")  # Improper fraction
        self.assertEqual(convert_to_mixed_fraction(9, 4), "2 + 1/4")   # Improper fraction
        self.assertEqual(convert_to_mixed_fraction(5, 5), "1")           # Improper fraction, reduces to 1

    # Test cases for display_fraction_type
    def test_display_fraction_type_proper(self):
        output = StringIO() # Capture output
        sys.stdout = output
        display_fraction_type(6, 7)  # Proper fraction
        self.assertEqual(output.getvalue().strip(), "6/7 is a proper fraction.")
        sys.stdout = sys.__stdout__  # Reset stdout

    def test_display_fraction_type_improper_mixed(self):
        output = StringIO()
        sys.stdout = output
        display_fraction_type(16, 3)  # Improper fraction, mixed form
        self.assertEqual(output.getvalue().strip(), "16/3 is an improper fraction and it can be written as 5 + 1/3.")
        sys.stdout = sys.__stdout__

    def test_display_fraction_type_improper_integer(self):
        output = StringIO()
        sys.stdout = output
        display_fraction_type(6, 2)  # Improper fraction, reduced to integer
        self.assertEqual(output.getvalue().strip(), "6/2 is an improper fraction and it can be written as 3.")
        sys.stdout = sys.__stdout__

    # Testing the main function indirectly by simulating input and capturing output
    def test_main_proper(self):
        input_values = ['6', '7']  # Proper fraction: 6/7
        output = StringIO()
        sys.stdout = output
        sys.stdin = StringIO("\n".join(input_values))  # Simulate input

        main()

        self.assertEqual(output.getvalue().strip(), "Enter a numerator: Enter a denominator: 6/7 is a proper fraction.")
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_main_improper_mixed(self):
        input_values = ['16', '3']  # Improper fraction: 16/3
        output = StringIO()
        sys.stdout = output
        sys.stdin = StringIO("\n".join(input_values))  # Simulate input

        main()

        self.assertEqual(output.getvalue().strip(), "Enter a numerator: Enter a denominator: 16/3 is an improper fraction and it can be written as 5 + 1/3.")
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__

    def test_main_improper_integer(self):
        input_values = ['6', '2']  # Improper fraction: 6/2, simplifies to 3
        output = StringIO()
        sys.stdout = output
        sys.stdin = StringIO("\n".join(input_values))  # Simulate input

        main()

        self.assertEqual(output.getvalue().strip(), "Enter a numerator: Enter a denominator: 6/2 is an improper fraction and it can be written as 3.")
        sys.stdout = sys.__stdout__
        sys.stdin = sys.__stdin__


if __name__ == "__main__":
    unittest.main()
