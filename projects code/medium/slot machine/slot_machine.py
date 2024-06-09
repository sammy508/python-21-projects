import random

max_line = 3
Min_Bet = 10
Max_Bet = 100

rows = 3
col = 3

symbol_count = {
    "A": 2,
    "B": 3,
    "C": 4,
    "D": 6,
}

symbol_value = {
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2,
}

def check_winning(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for column in columns:
            symbol_to_check = column[line]
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machine_spin(rows, col, symbols):
    all_symbols = []
    for symbol, count in symbols.items():
        for _ in range(count):
            all_symbols.append(symbol)
    columns = []
    for _ in range(col):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns

def print_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end="|")
            else:
                print(column[row], end=" ")
        print()

def deposit():
    while True:
        amount = input("How much would you like to deposit? : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be above $0")
        else:
            print("Please enter a valid number")
    return amount

def number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you want to bet on (1-{max_line}): ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= max_line:
                break
            else:
                print("Enter a valid number of lines!")
        else:
            print("Please enter a valid number")
    return lines

def get_bet():
    while True:
        amount = input(f"Enter the amount you would like to bet on each line: ")
        if amount.isdigit():
            amount = int(amount)
            if Min_Bet <= amount <= Max_Bet:
                break
            else:
                print(f"Amount must be between ${Min_Bet}-${Max_Bet}")
        else:
            print("Please enter a valid number")
    return amount

def spin(balance):
    lines = number_of_lines()
    while True:
        bet = get_bet()
        total_bet = lines * bet
        if total_bet > balance:
            print(f"You don't have enough balance to bet, you have only ${balance}")
        else:
            break

    print(f"You are betting {bet} on {lines} lines. Your total bet is {total_bet}")

    slots = get_slot_machine_spin(rows, col, symbol_count)
    print_slot_machine(slots)

    winnings, winning_lines = check_winning(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}")
    print("You won on lines:", *winning_lines)

    return winnings - total_bet

def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        spin_input = input("Press enter to play or (q to quit): ")
        if spin_input == "q":
            break
        else:
            balance += spin(balance)
    
    print(f"You left with ${balance}")

    
    
main()
