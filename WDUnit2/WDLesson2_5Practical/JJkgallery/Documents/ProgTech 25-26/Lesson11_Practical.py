import turtle
bob=turtle.Turtle()
bob.color("blue")
for times in range(500):
    bob.circle(100)
    for c in ('blue','green'):
        bob.color(c)
        bob.right(times * 7)
        bob.speed(0)

        #second circle


for times in range(400):
     bob.circle(75)
     bob.color("blue")
    
