**Number Guessing Game**

**
Project Description**

This is a simple number guessing game implemented in Python. The game generates a random number within a user-defined range, and the player attempts to guess the number. Feedback is provided for each guess, indicating whether the guess is too high, too low, or correct. The game continues until the player guesses the correct number, and the total number of guesses is displayed at the end.

**Features**

User-defined range for the random number.
Input validation to ensure the upper bound is not less than or equal to the lower bound.
Feedback for each guess: too high, too low, or correct.
Count of total guesses made by the player.
Exits gracefully if input bounds are invalid.
How to Run the Project
Ensure you have Python installed on your system. You can download it from python.org.
Download the number_guessing_game.py script from this repository.
Open your terminal or command prompt.
Navigate to the directory where number_guessing_game.py is located.
Run the script using the command: python number_guessing_game.py.

**Sample Code**

Here's a snippet of the Python code for the number guessing game:

python


import random

print("Welcome to the game.\n\n")

lower_bound = int(input('Enter lower bound number: '))
upper_bound = int(input('Enter upper bound number: '))

if upper_bound < 0:
    print('Upper number can\'t be 0')
    quit()
else:
    if upper_bound == lower_bound:
        print('Upper and lower bounds can\'t be the same')
        quit()

random_number = random.randint(lower_bound, upper_bound)
guesses = 0

while True:
    guesses += 1
    user_guess = int(input('Make your guess: '))

    if user_guess == random_number:
        print('Yea congrats! You got it')
        break
    elif user_guess < random_number:
        print('Your guess is too low')
        print('\n')
    else:
        print('Your guess is too high')
        print('\n')

print(f'You got it in {guesses} guesses')

**Usage**

Run the script to start the game.
Enter the lower and upper bounds for the random number range.
Guess the number based on the feedback provided.
The game ends when the correct number is guessed, displaying the total number of guesses.
Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. For major changes, please open an issue to discuss what you would like to change.

**License**

This project is open-source and available under the MIT License.
