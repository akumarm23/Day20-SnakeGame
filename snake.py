from turtle import Turtle

STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
MOVE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # List to store the snake segments
        self.segments = []
        self.create_snake()
        
        # Head of the snake
        self.head = self.segments[0]

    def move(self):
        """Move the snake forward."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        
        self.head.forward(MOVE)

    def up(self):
        """Change the snake's direction to up."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        """Change the snake's direction to down."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        """Change the snake's direction to left."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        """Change the snake's direction to right."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def create_snake(self):
        """Create the initial snake with three segments."""
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """Add a new segment to the snake."""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Extend the snake by adding a new segment to its tail."""
        self.add_segment(self.segments[-1].position())
