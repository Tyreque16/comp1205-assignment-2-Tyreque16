[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/nUgam1Gs)
# Assignment 2

## Problem 1

A fraction is defined by a numerator (top part) and a denominator (bottom part). There are two types of fractions:

Proper fraction: A fraction where the numerator is smaller than the denominator (e.g., 6/7).

Improper fraction: A fraction where the numerator is equal to or larger than the denominator (e.g., 16/3). Improper fractions can be expressed as a mixed fraction, which is a combination of an integer part and a proper fraction (e.g., 5 + 1/3).

The program needs to:

Accept the numerator and denominator as input from the user.

Determine whether the fraction is proper or improper.

For improper fractions:

Convert the fraction to a mixed fraction (if applicable).

If the fraction can be reduced to an integer (no remainder), display the integer.

Display the result to the user based on the fraction type.

**Tasks**

1. Implement a `get_input` function. This function will prompt the user for the numerator and denominator and return the values.
2. Implement the `is_proper_fraction` function which accept the numerator and denominator as input. This function will check whether the fraction is proper and return `True` if it is proper and `False` if it's improper.
3. Implement the  `convert_to_mixed_fraction` function which accept the numerator and denominator as input. This function will return a string representing the mixed fraction form.
4. Implement the `display_fraction_type` function which accepts the numerator and denominator as input. This function will print whether the fraction is proper or improper, and for improper fractions, it will call `convert_to_mixed_fraction` to display the mixed fraction.
5. Implement the `main()` function. This is the entry point of the program, which calls all the other functions.

**Here is a sample run**

Sample 1:

    Enter a numerator: 16
    Enter a denominator: 3
    16/3 is an improper fraction and it can be written as 5 + 1/3.
 
Sample 2:

    Enter a numerator: 6
    Enter a denominator: 7
    6/7 is a proper fraction.
 
Sample 3:

    Enter a numerator: 6
    Enter a denominator: 2
    6/2 is an improper fraction and it can be written as 3.

## Problem 2

You are being contracted as a programmer for the School of Science Computing and Artificial Intelligence. Your responsibility is to create simple fun games for students enrolled in the Course COMP1205 2024/25 Academic year to play in labs as a means of relaxation in the intense remainder of the semester, in the down periods between classes and lab sessions.

In this game you have to start by printing a grid with a title as follows:

    GRID OF GUESSES
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------


Call a function (sub-program) with at least one loop in it to print the layout of the grid.
Then print the following message:

    Welcome to the guessing game. You have 10 tries to guess the number that I am thinking of between 1 and 30.
    Each time you make an incorrect guess, we will show it to you in the GRID OF GUESSES.
    You may keep guessing until you are successful or until you have run out of guesses.

The algorithm must then generate the number between 1 and 30 and not reveal it to the user, ask the user to guess the number and then read the guess.
The algorithm must check the guess against the generated number and if they are the same it must print a message to the screen saying "Congrats, you have won!", and then
stop the game.

If the guess is not correct, the algorithm must perform two tasks:
Print to the screen the incorrect guess in the grid in the next available spot.
Check to see if the guess is greater or less than the random number and indicate this to the user.
For example, if the random number is 17 and the player guesses 10, the following would be printed on the screen:

    GRID OF GUESSES
    -------------------
     10 |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
    
    Your number is too small. Try again
If the player then guesses 20, the following will be printed on the screen:

    GRID OF GUESSES
    -------------------
     10 | 20 |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------
        |    |    |    
    -------------------

    Your number is too big. Try again

Your algorithm must also keep score. Use a counter that starts at 10 and for every incorrect guess, decrement it. The more guesses the fewer points. The user must be restricted to 10 guesses. If the player runs out of guesses, the algorithm must print a message to the screen saying "Sorry, you are out of guesses".

Print your final score to the screen and to the file: myScores.txt in the format "Final score: X", where X represents the final score.
You do not have to use an array to hold the contents of the grid.

**Function Breakdown:**

1. `print_grid(grid)`:

    This function prints the current state of the grid in a formatted way. It displays guesses made so far in the corresponding grid positions.

2. `get_user_guess(attempt)`:

    Handles input validation, ensuring the user enters a valid integer between 1 and 30.
This keeps the main loop clean by separating input logic.

3. `update_grid(grid, guess, guesses_made)`:
   
    Updates the grid with the user's guess and prints the updated grid.
Centralizing grid updates helps keep the main loop cleaner.

4. `provide_feedback(guess, secret_number)`:

    This function provides feedback (whether the guess is too big or too small) and helps separate the game logic from the display logic.

5. `save_score(score)`:
   
    Saves the final score to the file myScores.txt.
Moving file operations into its own function improves maintainability.

6. `play_game()`:
   
    This is the main function of the game logic:
    - It initializes the grid and displays it.
    - The game prompts the user to guess the number between 1 and 30.
    - It checks if the guess is correct, updates the grid, and provides feedback (too small/too big).
    - The user gets 10 attempts, and each incorrect guess is shown in the grid.
    - After the game ends, it calculates the final score and writes it to myScores.txt.
  
7. `main()`:

    Simply call the `play_game()` function to start the game.

## Problem 3

You’ve probably seen the “Mocking SpongeBob” meme: a picture of SpongeBob SquarePants with a caption whose text alternates between upper- and lowercase letters to indicate sarcasm, like this: **uSiNg SpOnGeBoB MeMeS dOeS NoT mAkE YoU wItTy**.
The goal of this program is to convert user-inputted text into “spongecase,” where the letters randomly alternate between uppercase and lowercase. In addition, the program should be designed as a module, so that other programs can import it and use a spongecase.englishToSpongecase() function.

Use a random choice between `True` and `False` for each letter. If the choice is `True`, convert the letter to uppercase and if the choice is `False`, convert the letter to lowercase.

**Problem Breakdown**

Input: A string from the user (e.g., a sentence or phrase).
Output: The same string where letters randomly alternate between uppercase and lowercase.

**Tasks:**

Create a function `englishToSpongecase` that will take a string as input and return the string with random alternation between uppercase and lowercase letters.

## Problem 4

The Hacking Minigame is inspired by the hacking game from Fallout 3. In this game, players are presented with a list of potential passwords, all of which are 7-letter words. The goal is to guess the correct password by using clues provided after each guess. The player has four chances to guess the password correctly. After each incorrect guess, the player is informed of how many letters in their guess match the correct password in both letter and position.
This game is set up with a cosmetic "computer memory" display that shows random characters interspersed with potential passwords to simulate hacking into a terminal. The game requires a text file, sevenletterwords.txt, containing a list of seven-letter words.

**Gameplay:**

The game starts by randomly selecting 12 words from the word list, including one secret password.

The player is tasked with guessing the correct password from the list.

After each guess, the game indicates how many letters of the guessed word match the secret password at the same positions.

The player has four guesses to find the correct password.

If the player successfully guesses the password, the game displays `A C C E S S G R A N T E D`. If not, the game reveals the correct password after four incorrect attempts.
Tasks

1. Implement `loadWords` function to Load the list of seven-letter words from the sevenletterwords.txt file, converting each word to uppercase and removing any trailing newline characters.
  Store the loaded words in a global variable called `WORDS`.
3. Implement the main loop of the game in a `main` function. This function should:
  Display the rules and instructions.
  Generate a random set of 12 potential passwords.
  Display the "computer memory" with garbage characters and the possible passwords.
  Allow the player to make up to four guesses and provide feedback based on their guesses.

4. Implement a `getWords` function to select 12 words, with the secret password being the first word. Ensure a mix of words with varying numbers of matching letters to the secret password.
5. Implement a `getComputerMemoryString` function that accepts words as input to create a string simulating the computer memory with random garbage characters and randomly placed words.
6. Implement an `askForPlayerGuess` function which takes a list of potential passwords and a guess number and asks the player to enter a guess from the list of potential passwords. Validate the input to ensure it is one of the displayed options.
7. Implement a `numMatchingLetters` function to take two words and count how many letters in the guessed word match the letters in the secret password in both letter and position.
   
**Summary of Gameplay**

Start the Game: The player is shown the instructions and 12 potential passwords.

Display Memory: The computer memory string is displayed, showing random garbage characters with potential passwords embedded.

Player Guesses: The player guesses the password up to four times, and after each guess, they are given feedback on how many letters were correct.

Win or Lose: If the player guesses the password within four tries, they win. Otherwise, the correct password is revealed.

**Sample Run 1**

    Hacking Minigame
    Find the password in the computer's memory. You are given clues after each guess.
    For example, if the secret password is MONITOR but the player guessed CONTAIN,
    they are given the hint that 2 out of 7 letters were correct.

    Press Enter to begin...

    0x12A4 ~!@#$%^COMPANY 0x22B4 #!@HABITAT#@$%
    0x12B4 @!MONITOR!@#@^ 0x22C4 ~@#%ANOTHER$%#
    ...

    Enter password: (4 tries remaining)
    > MONITOR
    Access Denied (1/7 correct)

    Enter password: (3 tries remaining)
    > COMPANY
    A C C E S S G R A N T E D

**Sample Run 2**

    Hacking Minigame
    Find the password in the computer's memory. You are given clues after each guess.
    For example, if the secret password is MONITOR but the player guessed CONTAIN,
    they are given the hint that 2 out of 7 letters were correct.

    Press Enter to begin...

    0x12A4 ~!@#$%^COMPANY 0x22B4 #!@HABITAT#@$%
    0x12B4 @!MONITOR!@#@^ 0x22C4 ~@#%ANOTHER$%#
    ...

    Enter password: (4 tries remaining)
    > MONITOR
    Access Denied (1/7 correct)

    Enter password: (3 tries remaining)
    > RANDOM
    Access Denied (0/7 correct)

    Enter password: (2 tries remaining)
    > CAMERAS
    Access Denied (2/7 correct)

    Enter password: (1 tries remaining)
    > COMPACT
    Access Denied (5/7 correct)

    Out of tries. Secret password was COMPANY.
