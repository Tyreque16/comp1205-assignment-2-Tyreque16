def print_grid(grid):
    print("GRID OF GUESSES")
    print("-" * 20)
    for row in grid:
        print(" | ".join(row))
        print("-" * 20)


def get_user_guess(attempt):
    while True:
        guess = input(f"Attempt {attempt}: Enter a number between 1 and 30: ")
        if guess.isdigit():
            guess = int(guess)
            if 1 <= guess <= 30:
                return guess
        print("Invalid input. Please enter a number between 1 and 30.")


def update_grid(grid, guess, guesses_made):
    row = (guesses_made - 1) // 5
    col = (guesses_made - 1) % 5
    grid[row][col] = str(guess)
    print_grid(grid)


def provide_feedback(guess, secret_number):
    if guess < secret_number:
        print("Your number is too small. Try again.")
    else:
        print("Your number is too big. Try again.")


def save_score(score):
    with open("myScores.txt", "w") as file:
        file.write(f"Final score: {score}\n")


def play_game():
    grid = [[" " for _ in range(5)] for _ in range(5)]
    print_grid(grid)
    secret_number = 17  # You can change this to random.randint(1, 30) for a real game
    score = 10
    guesses_made = 0
    
    while guesses_made < 10:
        guess = get_user_guess(guesses_made + 1)
        
        if guess == secret_number:
            print("Congrats, you have won!")
            break
        
        guesses_made += 1
        update_grid(grid, guess, guesses_made)
        provide_feedback(guess, secret_number)
        score -= 1
    else:
        print("Sorry, you are out of guesses.")
    
    print(f"Final score: {score}")
    save_score(score)


if __name__ == "__main__":
    main()
