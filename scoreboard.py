from turtle import Turtle

class Pen:
    def __init__(self):
        self.pen = Turtle()
        self.pen.speed(0)
        self.pen.shape("square")
        self.pen.color("white")
        self.pen.penup()
        self.pen.hideturtle()
        self.pen.goto(0, 330)
        self.pen.clear()

    def clear(self):
        self.pen.clear()

    def update_score(self, score, high_score):
        self.pen.clear()
        self.pen.write("Score: {}  High Score: {}".format(score, high_score), align="center", font=("Courier", 24, "normal"))
        # Save high score to file
        with open("high_score.txt", "w") as file:
            file.write(str(high_score))  # Записываем high_score в файл

    def final_score(self, score, high_score):
        self.pen.clear()
        self.pen.write("Score: {}  High Score: {} \n Press R to Restart ".format(score, high_score), align="center", font=("Courier", 24, "normal"))
