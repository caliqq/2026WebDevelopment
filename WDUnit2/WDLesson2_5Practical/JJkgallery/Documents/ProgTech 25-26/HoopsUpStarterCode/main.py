from gamelib import *

game = Game(1024,768,"Hoops Up!")

court= Image("court.jpg",game)
player1 = Image("player1.png", game)
player1.setSpeed(4,60)
player1.resizeBy(-60)
x = randint(100,900)
y = randint(100,600)
player1.moveTo(x,y)

player2 = Image("player2.png", game)
player2.setSpeed(3,90)
player2.resizeBy(-70)
x = randint(100,900)
y = randint(100,600)
player2.moveTo(x,y)

opponent_score = 0

net = Image("net.png",game)
net.resizeBy(-90)
net.moveTo(512,100)

ball = Image("basketball.png", game)
ball.resizeBy(-95)

court = Image("court.jpg",game)
court.resizeTo(game.width, game.height)

win = Image("youwin.png",game)
lose = Image("youlose.png",game)

cheer = Sound("cheer.wav",0)
block = Sound("block.wav",1)

game.update(60)
