Slot Machine Game

Introduction

This is a simple text-based slot machine game implemented in Python. The game allows users to deposit money, place bets on multiple lines, and spin the slot machine to try and win money. The game continues until the user decides to quit.

Features

    Deposit Money: Users can deposit a certain amount of money to start playing.
    Place Bets: Users can place bets on up to 3 lines with customizable bet amounts within a specified range.
    Spin the Slot Machine: The slot machine will randomly generate symbols, and users can win money if the symbols match on the lines they bet on.
    Check Winnings: The game checks for winning lines and calculates the total winnings based on the symbols and bet amount.
    Play Continuously: Users can keep playing as long as they have balance left and choose not to quit.

Game Rules

    Symbols:
        A: Appears 2 times
        B: Appears 3 times
        C: Appears 4 times
        D: Appears 6 times

    Symbol Values:
        A: 5x the bet amount
        B: 4x the bet amount
        C: 3x the bet amount
        D: 2x the bet amount

    Betting:
        Minimum bet per line: $10
        Maximum bet per line: $100
        Maximum number of lines to bet on: 3
    Winning: A line wins if all the symbols in that line are the same.

Getting Started

Prerequisites

    Python 3.x

Running the Game

    Clone the repository:

    bash

git clone https://github.com/sammy508/python-21-projects/tree/main/projects%20code/medium/slot%20machine

Navigate to the project directory:

bash

cd slot-machine-game

Run the game:

bash

    python slot_machine.py

Code Overview

Functions

    deposit(): Prompts the user to deposit money.
    number_of_lines(): Prompts the user to select the number of lines to bet on.
    get_bet(): Prompts the user to enter the bet amount per line.
    get_slot_machine_spin(rows, col, symbols): Generates a random slot machine spin based on the symbols and their counts.
    print_slot_machine(columns): Prints the slot machine columns in a readable format.
    check_winning(columns, lines, bet, values): Checks for winning lines and calculates the winnings.
    spin(balance): Manages the betting and spinning process, and updates the user's balance.
    main(): The main function that manages the game loop.

Example Gameplay

    User is prompted to deposit money.
    User selects the number of lines to bet on.
    User enters the bet amount per line.
    The slot machine spins and displays the result.
    The game checks for winnings and updates the balance.
    The user can choose to play again or quit.

Contributing

If you'd like to contribute to this project, please fork the repository and use a feature branch. Pull requests are welcome.

License

This project is licensed under the MIT License.

Acknowledgements

This game was developed as a fun project to demonstrate basic Python programming and the use of simple loops and conditionals.
