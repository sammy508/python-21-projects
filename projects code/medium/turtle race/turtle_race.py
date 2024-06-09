# import tkinter as TK
import turtle
import time
import random

COLORS = ["Red","Green","Black","Yellow","Blue","Pink","cyan","Orange","Brown"]

WIDTH = 500
HEIGHT = 500

def get_number_of_racers():
    while True:
        racers = input("Enter the number of turtles you want to race (2-8): ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a numeric value.")
            continue
        if 2 <= racers <= 8:
            return racers
        else:
            print("Please enter a valid number of racers between 2 and 8.")


def race(colors):
    turtles = create_turtle(colors)
    while True:
        for racer in turtles:
            distance = random.randrange(1,30)
            racer.forward(distance)
            x,y = racer.pos()
            
            if y >= HEIGHT//2 -10:
                return colors[turtles.index(racer)]





def create_turtle(colors):

    spacing = WIDTH//(len(colors)+1)
    
    turtles =[]
    for i, color in enumerate(colors):
        position_width = -WIDTH//2 +(i+1)*spacing
        position_height = -HEIGHT//2+20
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        racer.penup()
        racer.setpos(position_width,position_height)
        racer.pendown()
        turtles.append(racer)

    return turtles      






def init_turtle():

    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title("Turtle Racing!")

racers = get_number_of_racers()
init_turtle()
racer = turtle.Turtle()
# racer = turtle.forward(100) # it gives turtles of 100 pixel

random.shuffle(COLORS)
colors = COLORS [:racers] # here : is a slice operaotr it pick the colour from list 
winner = race(colors)
print(f"The winner is {winner}")


