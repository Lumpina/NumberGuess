# NumberGuess

Copyright 2025 Sandra Matejka

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

This project is released under a MIT license.

This was a demo project for students in the second grade of an electrical engineering HTL to introduce them to their first complete Python project.

## Mini Game

This project is a console-based Number Guessing Game in Python. It’s designed to:

    Provide entertainment — A simple yet satisfying game loop that keeps users engaged.
    Practice Python basics — Covers input handling, loops, conditionals, functions, and error handling.
    Introduce testing with pytest — Ensures all functions behave correctly, even with invalid inputs.
    Improve code structure — The game is broken into modular functions for better readability, maintenance, and reusability.

Guess a randomly selected number between 1 and 100 — with helpful hints ("Too high" or "Too low") until the user wins. Your goal is to guess the number in as few attempts as possible.

### generate_number()

Generates a random number between 1 and 100 for the player to guess.

### get_guess()

Continuously asks the player for a guess. It ensures the input is a valid integer within the range (1 to 100).

Error handling:
    Catches non-numeric input (e.g., "hello") and prompts the user again.
    Rejects negative numbers or numbers over 100 and asks for a valid number.

### check_guess()

Compares the player’s guess with the secret number.
    Returns False if the guess is too low or too high, providing feedback.
    Returns True if the player guesses correctly.

### play_game()

Controls the overall game loop.
    Calls other functions (generate_number(), get_guess(), check_guess()).
    Tracks the number of attempts.
    Ends when the player guesses correctly, displaying a victory message.

### Testing File

A test file with pytest to verify that each function works correctly — even with invalid inputs like strings, negative numbers, or numbers over 100.