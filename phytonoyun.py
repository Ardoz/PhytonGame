#Turtle oyun
import turtle
import math
import random


ekran = turtle.Screen()
ekran.bgcolor("black")
ekran.tracer(3)

sinir = turtle.Turtle()
sinir.color("white")
sinir.penup()
sinir.setposition(-300,-300)
sinir.pendown()
sinir.pensize(3)
for side in range(4):
    sinir.forward(600)
    sinir.left(90)
sinir.hideturtle()

oyuncu = turtle.Turtle()
oyuncu.color("blue")
oyuncu.shape("triangle")
oyuncu.penup()
oyuncu.speed(0)

score = 0

maxGoals = 10
goals = []

for count in range(maxGoals):
    goals.append(turtle.Turtle())
    goals[count].color("red")
    goals[count].shape("circle")
    goals[count].penup()
    goals[count].speed(0)
    goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))

speed = 1

def turnleft():
    oyuncu.left(30)
    
def turnright():
    oyuncu.right(30)
    
def increasespeed():
    global speed
    speed += 1
    
def lowerspeed():
    global speed
    speed -=1

def isCollision(t1, t2):
    d = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2) + math.pow(t1.ycor()-t2.ycor(),2))
    if d < 20:
        return True
    else:
        return False
        

turtle.listen()
turtle.onkey(turnleft, "Left")
turtle.onkey(turnright, "Right")
turtle.onkey(increasespeed, "Up")
turtle.onkey(lowerspeed,"Down")

while True:
    oyuncu.forward(speed)
    

    if oyuncu.xcor() > 300 or oyuncu.xcor() < -300:
        oyuncu.right(180)
       

    if oyuncu.ycor() > 300 or oyuncu.ycor() < -300:
        oyuncu.right(180)
       

    for count in range(maxGoals):
        goals[count].forward(3)

       
        if goals[count].xcor() > 290 or goals[count].xcor() < -290:
            goals[count].right(180)
            
     
        if goals[count].ycor() > 290 or goals[count].ycor() < -290:
            goals[count].right(180)
             

        if isCollision(oyuncu, goals[count]):
            goals[count].setposition(random.randint(-300, 300), random.randint(-300, 300))
            goals[count].right(random.randint(0,360))
          
            score += 1



delay = raw_input("Press Enter to finish.")

