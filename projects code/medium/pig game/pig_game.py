
import random

name = input("Enter your name: ")

print(f"Welcom to the game{name}")

def roll():
    min_val = 1
    max_val = 5
    roll = random.randint(min_val,max_val)
    return roll

while True:
    players = int(input("enter number of player (2-4): "))

    if players.isdigit():
        players = int(players)
        if 1 <= players > 4:
            print("playre must between 1 -4 ") 
            break
        else:
            print("invalid number! please enter in range of 1 - 4")


max_score = 100

player_score = [ 0 for i in range  (players)]

while max(player_score)< max_score:
    current_score = 0

    usr_roll = input(f"Would you like to roll a dice (Y for yess): ").lower()

    if usr_roll != "y" :
        break
    value = roll()

    if value == 1:
        print("you turned 1, turn over")
    else: 
        current_score += value
        print(f"You roolled a : {value}")
    print(f"your current score is {current_score}")    






    