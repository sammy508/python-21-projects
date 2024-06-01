import random

# variables for user and cmp
user_wins = 0
cmp_wins = 0

# list options rock paper scissors
options = ["rock","paper","scissors"]

while True:
    user_input = input("type rock paper scissors  or q to quit :").lower()
    if user_input== "q":
        quit()

    if user_input not in options:
        continue

    random_num = random.randint(0,2)    
    
    com_picks = options[random_num]
    print(f"computer picks {com_picks}")

    if user_input == "rock" and com_picks == "scissors" :
     print("You won")
     
     user_wins += 1

    elif user_input == "scissors" and com_picks == "paper" :
     print("You won")
   
     user_wins += 1

    elif user_input == "scissors" and com_picks == "rock" :
     print("You won")
     user_wins += 1

    elif user_input == com_picks :
     print ("both of you choose same") 

    else:
     print("You loose")
     cmp_wins += 1


    print(f"user wins {user_wins} times")
    print(f"cmp wins {cmp_wins} times")
    print("Good Bye!!")

