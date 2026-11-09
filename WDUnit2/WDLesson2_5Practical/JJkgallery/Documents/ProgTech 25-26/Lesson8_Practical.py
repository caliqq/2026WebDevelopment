import turtle
bob=turtle.Turtle()
for times in range(5):
    bob.forward(100)
    bob.left(72)

bob.penup()
bob.goto(300,0)
bob.pendown()
for times in range(6):
    bob.forward(100)
    bob.left(60)



   
bob.penup()
bob.goto(-300,0)
bob.pendown()
for times in range(8):
    bob.forward(100)
    bob.left(135)
bob.penup()
bob.goto(0,300)
bob.pendown()

for times in range(3):
    bob.forward(100)
    bob.left(120)
    

