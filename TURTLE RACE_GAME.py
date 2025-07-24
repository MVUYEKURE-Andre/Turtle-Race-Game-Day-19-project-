# drawing your thought with turtle graphics using python
import turtle
from turtle import Turtle,Screen
import random
is_race_on=False
screen=Screen()
screen.title("Welcome to the turtle race😎 !")
screen.setup(width=500, height=600)
user_bet=screen.textinput("betting for tutle race", "Name of turtle which will win:")
color=["green", "red", "blue","yellow","purple","chocolate"]
location_turtle=[(-210,-250),(-210,-180),(-210,-70),(-210,70),(-210,180),(-210,250)]
all_turtle=[]
for x in range (6):
    new_turtle=Turtle(shape="turtle")
    new_turtle.color(color[x])
    new_turtle.penup()
    new_turtle.goto(location_turtle[x])
    all_turtle.append(new_turtle)
    if user_bet:
        is_race_on=True
while is_race_on:
   for turtle in all_turtle:
       if turtle.xcor()>230:
           is_race_on=False
           winning_color =turtle.pencolor()
           if winning_color==user_bet:
               print(f"you have won with: {winning_color} color congratulation you guessed it right 😁😁😁")
           else:
               print(f"you have lost blue the winning color is:{winning_color}> try again later 😎😎 ")


       turtle_distance=random.randint(0,10)
       turtle.forward(turtle_distance)


# def move_forward():
#     tim.forward(20)
# def move_backward():
#     tim.backward(20)
# def move_clockwise():
#     new_heading=tim.heading()+10
#     tim.setheading(new_heading)
#
#     # tim.right(90)
# def move_counter_clockwise():
#     new_heading=tim.heading()-10
#     tim.setheading(new_heading)
#     # tim.left(90)
# def clear_drawing():
#     tim.reset()
#
# screen.listen()
# screen.onkey( key="w",fun=move_forward)
# screen.onkey( key="s",fun=move_backward)
#
# screen.onkey( key="a",fun=move_counter_clockwise)
# screen.onkey( key="d",fun=move_clockwise)
# screen.onkey( key="c",fun=clear_drawing)
screen.exitonclick()
