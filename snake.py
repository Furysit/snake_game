from turtle import Turtle
import time

starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.direction = up  # Инициализируем направление головы

    def create_snake(self):
        for position in starting_positions:
            new_segment = Turtle(shape="square")
            new_segment.color("white")
            new_segment.penup()
            new_segment.goto(position)
            self.segments.append(new_segment)
        

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(move_distance)

    def check_collision(self):
        if self.head.xcor() > 300 or self.head.xcor() < -300 or self.head.ycor() > 300 or self.head.ycor() < -300:
            self.reset_snake()
            return True

        for segment in self.segments[1:]:
            if self.head.distance(segment) < 1:
                self.reset_snake()
                return True

        return False

    def check_food(self, food):
        if self.head.distance(food) < 15:
            self.eat()
            food.refresh()
            return True
        return False

    def reset_snake(self):
        self.head.goto(0, 0)
        self.head.direction = up
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def eat(self):
        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        last_segment_position = self.segments[-1].position()
        new_segment.goto(last_segment_position)
        self.segments.append(new_segment)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
