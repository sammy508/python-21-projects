

print("Welcome!, to the game")

playing = input("Are you ready to play? ")

if playing.lower() != "yes":
    quit()
score = 0
question_list = [
    'What is the color of the sky on a clear day?',
    'What is the largest animal in the world?',
    'What fruit is known for keeping the doctor away?',
    'How many days are there in a week?',
    'What do bees make that we can eat?',
    'What is the capital of Nepal?'

]


ans = input(question_list[0])
if ans.lower() == 'blue':
    print('corrrect!')
    score += 5

else:
    print('incorrext')    
ans = input(question_list[1])
print('\n')
if ans.lower() == 'whale':
    print('corrrect!')
    score += 5
    print('\n')
else:
    print('incorrext')  
    print('\n')  
ans = input(question_list[2])
if ans.lower() == 'apple':
    print('corrrect!')
    score += 5
    print('\n')
else:
    print('incorrext')    
    print('\n')

ans = input(question_list[3])
if ans.lower() == 'seven':
    print('corrrect!')
    score += 5
    print('\n')
else:
    print('incorrext')    
    print('\n')

ans = input(question_list[4])
if ans.lower() == 'honey':
    print('corrrect!')
    score += 5
    print('\n')
else:
    print('incorrext')  
    print('\n')  
ans = input(question_list[5])
if ans.lower() == 'kathmandu':
    print('corrrect!')
    score += 5
    print('\n')
else:
    print('incorrext')    

print(f"you got total {score} marks")    
