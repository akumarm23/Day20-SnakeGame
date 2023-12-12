from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()

        # Set up Turtle attributes for food
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("red")
        self.speed("fastest")

        # Initial placement of the food
        self.refresh()

    def refresh(self):
        """Move the food to a random position on the screen."""
        x_cor = random.randint(-280, 280)
        y_cor = random.randint(-280, 280)
        self.goto(x_cor, y_cor)
