from myFunctions import *
turtle.tracer(3)
bob.width(1)
turtle.colormode(255)

turtle.bgcolor("magenta")
for times in range( 256 ):
  c = (  255, 255 - times, 255 )
  bob.color("blue", c)
  polygon(8, 50, c )
  bob.forward(times)
  bob.left(25)
