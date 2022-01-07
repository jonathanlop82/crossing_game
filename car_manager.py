from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
NUMBER_OF_INITIAL_CARS = 15



class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.shape("square")
        self.color(random.choice(COLORS))
        self.penup()
        self.increase_speed = STARTING_MOVE_DISTANCE
        self.setheading(180)
        self.hideturtle()
        self.goto(300,300)
        self.cars = []


    def initial_cars(self):
        for _ in range(NUMBER_OF_INITIAL_CARS):
            new_car = CarManager()
            self.cars.append(new_car)
            self.cars[-1].showturtle()
            self.cars[-1].goto(random.randint(-280, 280), random.randint(-260, 260))

    def new_car(self,increase_move):
        new_car = CarManager()
        self.cars.append(new_car)
        self.cars[-1].showturtle()
        self.cars[-1].increase_speed = increase_move
        self.cars[-1].goto(280, random.randint(-260, 260))

    def move_cars(self):
        self.setheading(180)
        self.forward(self.increase_speed)


