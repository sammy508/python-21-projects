
import random


def roll():
    min_val = 1
    max_val = 5
    roll = random.randint(min_val,max_val)
    return roll

while True:
    players = input("enter number of player (2-4): ")

    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            print("playre must between 2 -4 ") 
            break
        else:
            print("invalid number! please enter in range of 1 - 4")
    else:
        print("Invalid entry, try again")

max_score = 100

player_score = [ 0 for i in range  (players)]

while max(player_score)< max_score:

    
    for player_index in range(players):
        print(f"\n player number,{player_index+1},turn has just started!\n")
        print(f"Your total score is: {player_score[player_index]} \n")
        current_score = 0

        while True:
           usr_roll = input(f"Would you like to roll a dice (Y for yess): ").lower()

           if usr_roll != "y" :
              break
           
           value = roll()
           if value == 1:
                print("you turned 1, turn over")
                current_score=0
                break  
           else: 
                current_score += value
                print(f"You roolled a : {value}")
                print(f"your current score is {current_score}")    

    player_score[player_index]+= current_score
    print(f"Your total score is:",player_score[player_index])   

    
max_score = max(player_score)
winning_idx = player_score.index(max_score)
print("Player number", winning_idx + 1,
      "is the winner with a score of:", max_score)        

# import random


# def roll():
#     min_value = 1
#     max_value = 6
#     roll = random.randint(min_value, max_value)

#     return roll


# while True:
#     players = input("Enter the number of players (2 - 4): ")
#     if players.isdigit():
#         players = int(players)
#         if 2 <= players <= 4:
#             break
#         else:
#             print("Must be between 2 - 4 players.")
#     else:
#         print("Invalid, try again.")

# max_score = 50
# player_scores = [0 for _ in range(players)]

# while max(player_scores) < max_score:
#     for player_idx in range(players):
#         print("\nPlayer number", player_idx + 1, "turn has just started!")
#         print("Your total score is:", player_scores[player_idx], "\n")
#         current_score = 0

#         while True:
#             should_roll = input("Would you like to roll (y)? ")
#             if should_roll.lower() != "y":
#                 break

#             value = roll()
#             if value == 1:
#                 print("You rolled a 1! Turn done!")
#                 current_score = 0
#                 break
           
#             else:
#                 current_score += value
#                 print("You rolled a:", value)

#             print("Your score is:", current_score)

#         player_scores[player_idx] += current_score
#         print("Your total score is:", player_scores[player_idx])

# max_score = max(player_scores)
# winning_idx = player_scores.index(max_score)
# print("Player number", winning_idx + 1,
#       "is the winner with a score of:", max_score)
