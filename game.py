import random


# Function to generate a random number
def generate_number():
    return random.randint(1, 100)


# Function to get the player's guess
def get_guess():
    while True:
        try:
            guess = int(input("Enter your guess: "))
            if 1 <= guess <= 100:
                return guess
            else:
                print("Please enter a number between 1 and 100!")
        except ValueError:
            print("Please enter a valid number!")


# Function to check the guess
def check_guess(guess, secret_number):
    if guess < secret_number:
        print("Too low! Try again.")
        return False
    elif guess > secret_number:
        print("Too high! Try again.")
        return False
    else:
        print("Correct!")
        return True


# Main game function
def play_game():
    secret_number = generate_number()
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")

    attempts = 0

    while True:
        guess = get_guess()
        attempts += 1

        if check_guess(guess, secret_number):
            print(
                f"Congratulations! You guessed the number {secret_number} in {attempts} attempts."
            )
            break


# Start the game
if __name__ == "__main__":
    play_game()
