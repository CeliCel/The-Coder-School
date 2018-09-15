import turtle
from random import randint
t= turtle.Turtle()
t.speed(0)
'''
wn = turtle.Screen()
wn.bgcolor("Black")
'''
def drawBox():
    t.color("white")
    for i in range(4):
        t.fd(600)
        t.rt(90)
        t.write(t.pos())
        

def cardDirections():
    FONT = ('Arial', 25, 'normal') 
    cDir = ["N","E","S","W"] #list of strings for NESW
    x = [0, 315,0,-345]
    y = [300,0,-340,0]
    for i in range(4):
        t.pu()
        t.goto(x[i],y[i])
        t.pd()
        t.write(cDir[i], font = FONT)

def Canvas():
    t.pu()
    t.goto(-300,300)
    t.pd()
    drawBox()

    t.pu()
    t.goto(0,-300)
    t.pd()
    t.circle(300)
    
    cardDirections()

def Circle():
    t.color("white", "gold")
    t.begin_fill()
    t.circle(2)
    t.end_fill()
    
def Cepheus():
    t.pu()
    t.goto(-100,150)
    t.pd()
    t.rt(45)
    for i in range(4):
        Circle()
        t.fd(25)
        t.rt(90)
    for i in range(3):
        t.fd(25)
        t.lt(120)
    t.write("Cepheus")
    return

    


def Perseus():
    t.pu()
    t.goto(0, 290)
    t.pd()
    t.rt(45)
    for i in range(5):
        Circle()
        t.fd(10)
    t.write("Perseus")
    t.lt(117)
    t.fd(10)
    for i in range(5):
        Circle()
        t.fd(15)
        
'''    
def gridLines():
    x = 0
    y = 0
    for i in range(4): 
        t.rt(90)
        t.pu()
        t.goto(i,y)
        t.pd()
        t.color("red")
        t.fd(300)
'''
def Corvus():
    t.pu()
    t.goto(150,-150)
    t.pd()
    for i in range(2):
        Circle()
        t.fd(25)
        t.rt(45)
    for i in range(2):
        Circle()
        t.rt(45)
        t.fd(45)
        t.rt(85)
    
def drawConstellation():
    s = t.getscreen()
    s.bgcolor("black")
    t.color("white")
    #s.onclick(Circle)
    #t.mainloop()


drawConstellation()
Canvas()
#gridLines()
Cepheus()
Perseus()
Corvus()
t.ht()
