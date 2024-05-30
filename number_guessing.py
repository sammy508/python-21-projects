
# here we make a number guessign game

import random

print("Welcone to the game.n\n")

lower_bound = int(input('enter lower bound number: '))
upper_bound = int(input('enter upper bound number: '))

if  upper_bound < 0  :
    print('upper  number can\'t be 0')
    quit()
else :
    if (upper_bound == lower_bound) :
        print('can\'t be same')
        quit()

random_number = random.randint(lower_bound, upper_bound)
guesses = 0

while True:
 guesses += 1
 user_guess = int(input('make your guess : '))

 if user_guess == random_number:
    print('Yea congrats!, You got it')
    break
 elif user_guess < random_number :
        print('Your guess is to low')
        print('\n')
 else:
        print('Your guess is high')   
        print('\n')

print(f'you got it in {guesses} guesses')        

   