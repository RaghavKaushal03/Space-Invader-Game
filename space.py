import turtle
import os
import math
import random

#Inputscreen
wn=turtle.Screen()
wn.bgcolor("black")
wn.title("Space Invader")
wn.bgpic("space_invaders_background.gif")

turtle.register_shape("invader.gif")
turtle.register_shape("player.gif")


#Draw border
borderPen=turtle.Turtle()
borderPen.speed(0)
borderPen.color("white")
borderPen.penup()
borderPen.setposition(-300,-300)
borderPen.pendown()
borderPen.pensize(3)
for side in range(4):
    borderPen.fd(600)
    borderPen.lt(90)
borderPen.hideturtle()    

#create player

player=turtle.Turtle()
player.color("red")
player.shape("player.gif")
player.penup()
player.speed(0)
player.setposition(0,-250)
player.setheading(90)

playerspeed=15

#create enemy
numberofEnemies=5
enemies=[]
#add enemies to the list
for i in range(numberofEnemies):
    enemies.append(turtle.Turtle())
for enemy in enemies:    
    enemy=turtle.Turtle()
    enemy.color("red")
    enemy.shape("invader.gif")
    enemy.penup()
    enemy.speed(0)
    x=random.randint(-200,200)
    y=random.randint(100,250)
    enemy.setposition(x,y)

enemyspeed=3

#create bullet
bullet=turtle.Turtle()
bullet.color("yellow")
bullet.shape("triangle")
bullet.penup()
bullet.speed(0)
bullet.setheading(90)
bullet.shapesize(0.5,0.5)
bullet.hideturtle()

bulletspeed=20

bulletState="ready"

#move player left and right
def moveLeft():
    x=player.xcor()
    x=x-playerspeed
    if x<-280:
        x=-280
    player.setx(x)

def moveRight():
    x=player.xcor()
    x=x+playerspeed
    if x>280:
        x=280
    player.setx(x)

def fireBullet():
    global bulletState
    if bulletState=="ready":
        bulletState="fire"
        #move bullet upwards from where it is fired
        x=player.xcor()
        y=player.ycor()+10
        bullet.setposition(x,y)
        bullet.showturtle()    

def isCollision(t1,t2):
    distance=math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    if distance<15:
        return True
    else:
        return False    

#keyboard binding
turtle.listen()
turtle.onkey(fireBullet,"space")
turtle.onkey(moveLeft,"Left")
turtle.onkey(moveRight,"Right") 

#main loop
while True:
    for enemy in enemies :
        #moving the enemy
        x=enemy.xcor()
        x=x+enemyspeed
        enemy.setx(x)
        #move the enemy down and change direction 
        if enemy.xcor()>280:
            y=enemy.ycor()
            y=y-30
            enemyspeed *= -1
            enemy.sety(y)
        if enemy.xcor()<-280:
            y=enemy.ycor()
            y=y-30
            enemyspeed *= -1
            enemy.sety(y)
           
        #detect collision b\w bullet and enemy
        if isCollision(bullet,enemy):
            bullet.hideturtle
            bulletState="Ready"
            bullet.setposition(0,-400)
            enemy.setposition(-200,250)    
        if isCollision(player,enemy):
            print("Game Over")
            break
    if bulletState=="fire":
            y=bullet.ycor()
            y=y+bulletspeed
            bullet.sety(y)
    if bullet.ycor()>275:
            bullet.hideturtle()
            bulletState="ready"         

delay=input("Enter a key to finish")

while True:
    wn.update()
