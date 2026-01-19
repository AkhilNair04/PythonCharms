import turtle

fan = turtle.Turtle()
fan.speed(0)
def draw_blade():
    fan.forward(6)
    fan.left(90)
    fan.forward(5)
    fan.right(90)
    fan.forward(90)
    fan.right(90)
    fan.forward(20)
    fan.right(90)
    fan.forward(90)
    fan.right(90)
    fan.forward(5)
    fan.left(90)
    fan.forward(6)
def step_quarter_circle(radius, steps):
    step_length = (3.14 * radius / 2) / steps
    step_angle = 90 / steps

    for _ in range(steps):
        fan.forward(step_length)
        fan.left(step_angle)

for _ in range(4):
    fan.right(90)
    step_quarter_circle(30, 15)
    fan.right(90)
    draw_blade()

turtle.done()
