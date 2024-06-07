

import random
import time

OPERATORS = ["*","-","+","/"]
MinOPERATOR = 3
MaxOPERATOR = 15
total_problem = 10

def generate_problem():
    left = random.randint(MinOPERATOR, MaxOPERATOR)

    right = random.randint(MinOPERATOR, MaxOPERATOR)
    operator = random.choice(OPERATORS)

    expression = str(left) + "" + operator + str(right)
    answer = eval(expression)  # here in python eval function evaluates the python string and perfoms the operations
    return expression, answer

wrong =1  
input("Are you ready? Press enter to start")
print("__________________________________")  
start_time = time.time()
for i in range (total_problem):
    expression, answer =generate_problem()
    while True:
        user_guess =  input(f"Probloem {i+1}: {expression} = ")
        if user_guess == str(answer):
            break
        else:
            wrong+=1

    
end_time = time.time()
total_time = end_time-start_time

print(f"congrats, you complete on {total_time}seconds!")