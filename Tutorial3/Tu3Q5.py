import turtle
t = turtle.Turtle()
t.speed(0)
def hex(size):
    for _ in range(6):
        t.forward(size)
        t.right(60)
for _ in range(10):
    hex(50)
    t.right(36)
