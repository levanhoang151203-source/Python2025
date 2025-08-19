# Vẽ lá cờ Việt Nam bằng turtle
import turtle
import math

# Thiết lập cửa sổ
screen = turtle.Screen()
screen.setup(width=600, height=400)
screen.bgcolor("red")

# Vẽ ngôi sao vàng
star = turtle.Turtle()
star.hideturtle()
star.speed(0)
star.color("yellow")
star.penup()
star.goto(0, -60)
star.pendown()

def draw_star(t, size):
    t.begin_fill()
    for i in range(5):
        t.forward(size)
        t.left(144)
    t.end_fill()

draw_star(star, 120)

turtle.done()