from turtle import Turtle
import random
import time
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
MAX_CARS = 50
all_cars = []

class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color(random.choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.start_x = random.randint(400, 2800)
        self.start_y = random.randint(-240, 240)
        self.goto(self.start_x, self.start_y)

    def car_move(self):
        new_x = self.xcor() - STARTING_MOVE_DISTANCE
        self.goto(new_x, self.ycor())

    def generate_cars(self):
        for _ in range(0, MAX_CARS):
            car = CarManager()
            all_cars.append(car)

    def erase_cars(self):
        global all_cars
        for car in all_cars:
            car.hideturtle()
        all_cars.clear()

    def increase_car_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT

    def increase_max_cars(self):
        global MAX_CARS
        MAX_CARS += 10

    def level_up(self):
        self.erase_cars()
        self.increase_max_cars()
        self.increase_car_speed()
        self.generate_cars()