from turtle import  Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()  # Инициализируем родительский класс Turtle
        self.shape("circle")
        self.color("red")
        self.penup()
        self.refresh()  # Вызываем метод, чтобы разместить еду

    def refresh(self):
        # Позиционируем еду в случайной позиции
        x = random.randint(-280, 280)
        y = random.randint(-280, 280)
        self.goto(x, y)