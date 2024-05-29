from turtle import Turtle
import random

class UI:
    car_colors = [
        "red",
        "blue",
        "green",
        "yellow",
        "purple",
        "orange",
        "pink",
        "brown",
        "cyan",
        "magenta",
        "lime",
        "olive",
        "navy"
    ]

class Car(Turtle):



    def __init__(self):
        super().__init__("square")
        self.penup()
        self.color(random.choice(UI.car_colors))
        self.shapesize(1, 2)
        self.x_move = 10
        self.setheading(180)
        self.reset_position()

    def move(self):
        new_x = self.xcor() - self.x_move
        self.setposition(new_x, self.ycor())

    def reset_position(self):
        random_x = random.randint(300, 1000)
        random_y = random.randint(-200, 220)
        self.goto(random_x, random_y)

    def make_faster(self):
        self.x_move *= 1.5
