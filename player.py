from turtle import Turtle

Y_START = -280


class Player(Turtle):

    def __init__(self):
        super().__init__("turtle")
        self.penup()
        self.setheading(90)
        self.restart_position()

    def move_up(self):
        self.forward(10)

    def move_down(self):
        self.backward(10)

    def did_reach_goal(self):
        return self.ycor() > 280

    def restart_position(self):
        self.goto(0, Y_START)
