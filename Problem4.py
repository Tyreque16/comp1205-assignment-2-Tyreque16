
import random

WORDS = []

def loadWords(filename):
    global WORDS
    with open(filename, 'r') as file:
        WORDS = [line.strip().upper() for line in file if len(line.strip()) == 7]

def getWords():
    """Select 12 words for the game, with the first being the secret password."""
    selected_words = random.sample(WORDS, 12)
    secret_password = selected_words[0]
    return selected_words, secret_password

def getComputerMemoryString(words):
    garbage_chars = ''.join(random.choices('!@#$%^&*()_+=-~<>?,./;', k=30))
    memory_string = garbage_chars
    for word in words:
        position = random.randint(0, len(memory_string) - 1)
        memory_string = memory_string[:position] + word + memory_string[position + len(word):]
    return memory_string

def askForPlayerGuess(possible_passwords, attempt):
    while True:
        guess = input(f"Enter password: ({attempt} tries remaining)\n> ").strip().upper()
        if guess in possible_passwords:
            return guess
        print(" Invalid input. Please choose from the displayed options.")

def numMatchingLetters(guess, secret_password):
    """Count how many letters in the guessed word match the secret password in both letter and position."""
    return sum(1 for g, s in zip(guess, secret_password) if g == s)

def main():
    """Main function to run the Hacking Minigame."""
    loadWords('sevenletterwords.txt')
    
    print("Hacking Minigame")
    print("Find the password in the computer's memory. You are given clues after each guess.")
    print("For example, if the secret password is MONITOR but the player guessed CONTAIN,")
    print("they are given the hint that 2 out of 7 letters were correct.")
    input("Press Enter to begin...")

    possible_passwords, secret_password = getWords()
    memory_string = getComputerMemoryString(possible_passwords)
    
    print(memory_string)
    
    attempts = 4
    for attempt in range(attempts, 0, -1):
        guess = askForPlayerGuess(possible_passwords, attempt)
        matches = numMatchingLetters(guess, secret_password)

        if guess == secret_password:
            print("A C C E S S G R A N T E D")
            return
        else:
            print(f"Access Denied ({matches}/7 correct)")

    print(f"Out of tries. Secret password was {secret_password}.")

if __name__ == "__main__":
    main()
