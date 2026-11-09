from gradient import *

bob.speed(0)
bob.width(1)
turtle.colormode(255)
'''
def polygon
# gradient design 1
for times in range( 256 ):
  c = ( 0, times, 0 )
  polygon(4, 100, c )
  bob.left(3)
  bob.forward(5)
'''

# gradient design 2
for times in range( 256 ):
  c = ( times, 0, 0 )
  polygon(3, 255 - times, c )
  bob.forward(10)
  bob.left(10)


'''
# gradient design 3
turtle.bgcolor("black")
for times in range( 256 ):
  c = ( times, 0, 255 - times )
  bob.color("yellow", c)
  polygon(5, 40, c )
  bob.forward(times)
  bob.left(25)
'''

