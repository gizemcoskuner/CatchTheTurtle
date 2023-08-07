import turtle
import time
import datetime
from random import randint

turtle_board = turtle.Screen()
turtle_board.bgcolor("BlanchedAlmond")
turtle_board.title("Catch The Turtle")

turtle_instance = turtle.Turtle()
turtle_instance.color("green")
turtle_instance.shape("turtle")
turtle_instance.shapesize(4)
turtle_instance.speed(0)
time_t = turtle.Turtle()
time_t.hideturtle()
time_t.penup()
time_t.setposition(200,200)

total_seconds = 15

score = 0

pen_score = turtle.Turtle()
pen_score.hideturtle()
pen_score.penup()
pen_score.goto(0,200)
pen_score.write(f"Score: {score}", align="center", font=("Arial",15,"normal"))

def scored(x,y):
    global score
    score += 1
    pen_score.clear()
    pen_score.write(f"Score: {score}", align="center", font=("Arial", 15, "normal"))


while total_seconds > 0:
    turtle_instance.penup()
    turtle_instance.goto(randint(-250,250),randint(-250,250))
    timer = datetime.timedelta(seconds=total_seconds)
    time_t.write("timer: {}" .format(int(total_seconds)),font=("Arial",15,"normal"))
    time.sleep(1)
    time_t.clear()
    total_seconds -= 1
    turtle_instance.onclick(scored)
else:
    turtle_instance.onclick(None)
    turtle.write("Bzzzt! Time is over!!!", font=("Arial", 15, "normal"))

turtle.mainloop()