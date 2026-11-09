import turtle
bob=turtle.Turtle()
bob.color("purple")
def spiral():
    for times in range(10):
        bob.forward(times + 2)
        bob.left(30)
