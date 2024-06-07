
max_line = 3
Min_Bet = 10
Max_Bet = 100

def deposit():
    while True:
        amount = input("How much would you like to deposit? : ")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Deposit must be above  $10")
        else:
            print("please enter valid number")  
    return amount

def number_of_lines():
    while True:
        lines = input(f"Enter the number of lines you wanna bet on range of (1-{max_line}) : ")
        if lines.isdigit():
            lines = int(lines)
            if 1<= lines <= max_line:
                break
            else:
                print("Enter valid numbers of lines!")
        else:
            print("please enter valid number")  
    return lines


def main():

    balance = deposit()
    lines = number_of_lines()

    print(balance, lines)

main()            


