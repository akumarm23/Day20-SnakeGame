from turtle import Turtle

# Constants for text alignment and font style
ALIGN = "center"
FONT = ("Arial", 24, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0

        # Set up Turtle attributes for score display
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.speed("fastest")
        
        # Initial update of the score display
        self.update_score()

    def update_score(self):
        """Update the score display on the screen."""
        self.write(f"Score: {self.score}", align=ALIGN, font=FONT)

    def game_over(self):
        """Display 'GAME OVER' message on the screen."""
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)

    def increase_score(self):
        """Increase the score by 1 and update the score display."""
        self.score += 1
        self.clear()  # Clear the previous score display
        self.update_score()  # Update the score display with the new score
