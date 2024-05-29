import time
from turtle import Screen
from player import Player
from car import Car
import random


screen = Screen()
screen.setup(600, 600)
screen.tracer(0)

cars = []
for _ in range(20):
    c = Car()
    cars.append(c)

player = Player()

screen.listen()
screen.onkey(player.move_up, "w")
screen.onkey(player.move_down, "s")

is_playing = True
while is_playing:
    time.sleep(0.1)
    screen.update()

    for car in cars:
        car.move()
        if car.xcor() < -300:
            car.reset_position()
        if car.distance(player) < 25:
            print("THE TURTLE WAS CRUSHED TO DEATH")
            player.restart_position()

    if player.did_reach_goal():
        print("FORTUNE WAS ON THE TURTLE'S SIDE TODAY")
        player.restart_position()
        for car in cars:
            random_bool = random.choice([True, False])
            if random_bool:
                car.make_faster()

screen.exitonclick()
