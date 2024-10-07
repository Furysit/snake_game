from turtle import Screen, Turtle
import time
from snake import Snake
from food import Food
from scoreboard import Pen

# SCREEN
screen = Screen()
screen.setup(width=900, height=900)
screen.bgcolor('black')
screen.title("Solid snake")
screen.tracer(0)

# DRAW BORDER
border = Turtle()
border.speed(0)
border.color("blue")
border.penup()
border.goto(-322, 322)  # Левый верхний угол игрового поля
border.pendown()
border.pensize(20)  # Толщина линии
for _ in range(4):
    border.forward(644)  # Рисуем сторону поля
    border.right(90)
border.hideturtle()

# SCORE VARIABLES
score = 0
# Load high score from file
try:
    with open("high_score.txt", "r") as file:
        high_score = int(file.read())
except FileNotFoundError:
    high_score = 0  # Если файл не существует, начнем с 0

# INIT
snake = Snake()
food = Food()
pen = Pen()


def reset_game():
    global score, game_is_on
    score = 0
    food.refresh()
    pen.update_score(score, high_score)
    screen.bgcolor('black')
    game_is_on = True
    screen.update()
    


# LISTEN
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")




# MAIN LOOP
game_is_on = True

while True:  # Бесконечный цикл для возможности перезапуска
    while game_is_on:
        screen.update()
        time.sleep(0.09)

        snake.move()

        # Проверка столкновения с едой
        if snake.check_food(food):
            score += 15
            if score > high_score:
                high_score = score
            pen.update_score(score, high_score)

        # Проверка столкновения
        if snake.check_collision():
            screen.bgcolor("red")
            time.sleep(1)
            game_is_on = False
            screen.onkey(reset_game, "r")
            pen.final_score(score,high_score)

    # Ожидание нажатия клавиши "R" для перезапуска игры
    screen.update()
    time.sleep(0.1)





