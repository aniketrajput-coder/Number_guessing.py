# Number_guessing.py

## Project Description
This is a simple Number Guessing Game where the computer randomly selects a number between 1 and 100, and the user has to guess it.
The game continues until the correct number is guessed, and it also tracks the number of attempts taken by the player.

## Technologies Used
Python 3
random module (for generating random numbers)

## How It Works
The program uses random.randint(1, 100) to generate a random number.
The user is prompted to guess the number.
Each guess is compared with the generated number:
If the guess is higher, the program prints "Too high".
If the guess is lower, the program prints "Too low".
If the guess is correct, the game ends.
The program keeps track of the number of attempts using a counter (tryi).
Once guessed correctly, it displays:
A success message 
Total attempts taken
