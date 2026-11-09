
import turtle
bob=turtle.Turtle()


def comet(dist,angle):
    for times in range(50):
        bob.width(times + 2)
        bob.forward(dist)
        bob.left(angle)
