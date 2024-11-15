# import turtle
 
# screen = turtle.Screen()
# screen.bgcolor("lightblue")
# # Create a turtle
# t = turtle.Turtle()
# t.pensize (5)
# t.shape("turtle")
# t.color("green")
# t.penup()
# t.goto(-180, 20)
# t.pendown()
# t.goto(-180, 100)
# t.penup()
# t.goto(-220,100)
# t.pendown()
# t.goto(-140, 100)
# t.penup()
# t.goto(-110, 100)
# t.pendown()
# t.goto(-110, 20)
# t.goto(-60, 20)
# t.goto(-60, 100)
# t.penup()
# t.goto(-30, 100)
# t.pendown()
# t.goto(10, 100)
# t.goto(10, 60)
# t.goto(-30, 60)
# t.goto(-30, 100)
# t.goto(-30, 20)
# t.goto(-30, 60)
# t.goto(10, 20)
# t.penup()
# t.goto(40, 100)
# t.pendown ()
# t.goto(90, 100)
# t.goto(30, 100)
# t.goto(60, 100)
# t.goto(60, 20)
# t.penup()
# t.goto(120, 100)
# t.pendown()
# t.goto(120, 20)
# t.goto(160, 20)
# t.penup()
# t.goto(190, 100)
# t.pendown()
# t.goto(230, 100)
# t.goto(190, 100)
# t.goto(190, 60)
# t.goto(230, 60)
# t.goto(190, 60)
# t.goto(190, 20)
# t.goto(230, 20)
   

# turtle.done()

# favourite_countries = ["Angola", "Congo", "Jamaica", "Tanzania"]

# for i in favourite_countries:
#     print(i)

# if favourite_countries[3] == "Angola":
#     print("Yayyy, Angola is the best")

# else:
#     print("Boo, Angola is not the best")

# for i in range(9, -1, -1):
#     print(i)

# for i in range (10):
#     print("CJ")

# import random 

# my_num = 50

# rand_num = random.randint(0,50)

# while rand_num != my_num:
#     print(rand_num)
#     rand_num = random.randint(0, 50)

# print(f"You found my number! {my_num}")

# for i in range(12):
#     print(i)

# count = 0

# while count < 12:
#     print("Hello World")
#     count += 1 
    
# import random

# # Loop to generate 6 random numbers
# for i in range(6):
#     rand_num = random.randint(1, 30)  # Generate a random number between 1 and 30
#     print(f"Random number {i+1}: {rand_num}")
    
#     # Check if the random number is divisible by 7
#     if rand_num % 7 == 0:
#         print(f"{rand_num} is divisible by 7")
#     else:
#         print(f"{rand_num} is not divisible by 7")

# Create a while loop to randomly cycle through a list of cards until
# a given card is found.
# cards=[“Diamond”, “Spade”, “Club”, “Heart”]
# Create a variable called current_card and use a list method to
# randomly give it a value from the list every time the loop runs.
# Then compare this to the card you want to find to stop the while
# loop.

# import random

# cards = ["Diamond", "Spade", "Club", "Heart"]

# target_card = ("Spade")

# current_card = ("Diamond")

# while current_card != target_card:
#     current_card = random.choice(cards)
#     print(f"Current card: {current_card}")

# print("Found the card: {target_card}!")

import random 

from turtle import Turtle

colin = Turtle()
juma = Turtle()
tahfia = Turtle()
saleem = Turtle()

colin.color("blue")
colin.shape("turtle")
colin.penup()
colin.goto(-160, 100)


juma.color("red")
juma.shape("turtle")
juma.penup()
juma.goto(-160, 70)

tahfia.color("black")
tahfia.shape("turtle")
tahfia.penup()
tahfia.goto(-160, 40)

saleem.color("green")
saleem.shape("turtle")
saleem.penup()
saleem.goto(-160, 10)

for movement in range(100):
    colin.forward(random.randint(1,7))
    juma.forward(random.randint(1,7))
    tahfia.forward(random.randint(1,7))
    saleem.forward(random.randint(1,7))

input("Press Enter to close")

# from turtle import Turtle

# turtle = Turtle()

# turtle.color('blue')
# turtle.shape("turtle")
# turtle.penup()
# turtle.fillcolor('blue')
# turtle.speed(5)
# turtle.goto(-160, 40)


# def draw_pentagon():
#     turtle.color('blue')
#     turtle.begin_fill()
#     turtle.pendown()
#     sides = 5
#     angle = 72

#     for _ in range(sides):
#         turtle.forward(100)
#         turtle.right(angle)
#     turtle.end_fill()

# draw_pentagon()

# def draw_sides():
#     print()

# input("Press Enter to close")
