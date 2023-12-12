# SNAKE GAME Python Code v0.1

# Import necessary modules
from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

# Set up the screen
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game v0.1")
screen.tracer(0)  # Turn off automatic updates

# Create Snake, Food, and Score instances
snake = Snake()
food = Food()
score = Score()

# Set up keyboard bindings
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()  # Update the screen manually
    time.sleep(0.1)  # Pause for a short duration to control the speed of the game
    snake.move()  # Move the snake

    # Detect collision with Food
    if snake.head.distance(food) < 15:
        food.refresh()  # Move food to a new random position
        snake.extend()  # Extend the length of the snake
        score.increase_score()  # Increase the score

    # Detect collision with Wall
    if (
        snake.head.xcor() > 290
        or snake.head.xcor() < -290
        or snake.head.ycor() > 290
        or snake.head.ycor() < -290
    ):
        game_is_on = False
        score.game_over()

    # Detect collision with Tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False
            score.game_over()

# Exit the game when the user clicks on the screen
screen.exitonclick()

# Clear the terminal screen (may not work in all environments)
print("\033c", end="")

# END OF CODE
