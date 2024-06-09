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
print(colors)


