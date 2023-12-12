# Snake Game in Python

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
![Python 3.8](https://img.shields.io/badge/Python-3.8-blue.svg)
![Version 1.0](https://img.shields.io/badge/Version-1.0-brightgreen.svg)

This is a simple Snake Game implemented in Python using the Turtle graphics library.

## Files

### 1. `main.py`

The main script that initializes the game, sets up the screen, and runs the game loop.

### 2. `snake.py`

Contains the `Snake` class responsible for managing the snake's behavior, movement, and interaction with the game environment.

### 3. `food.py`

Defines the `Food` class that represents the food item in the game. It handles the creation and placement of the food on the screen.

### 4. `score.py`

Includes the `Score` class responsible for keeping track of the player's score, updating the score display, and handling game over scenarios.

## How to Play

1. Run the `main.py` script to start the game.
2. Control the snake's direction using the arrow keys (Up, Down, Left, Right).
3. Eat the red food to increase your score.
4. Avoid collisions with the walls and the snake's own tail.
5. The game ends when the snake collides with the walls or itself.

## Dependencies

The game relies on the Turtle graphics library, which is included in the Python standard library. No additional dependencies are required.

## Running the Game

Ensure you have Python installed on your system. Run the `main.py` script to start the Snake Game.

```bash
python main.py
```

## License

This Snake Game is distributed under the [MIT License](LICENSE). 

## Acknowledgments

The Snake Game code is inspired by classic snake games and adapted for educational purposes. The Turtle graphics library simplifies the implementation of graphics in a beginner-friendly manner.
