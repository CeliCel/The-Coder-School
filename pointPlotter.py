#y=mx+b
import turtle
t=turtle.Turtle()
t.speed(0)

'''
ask = True

#while True:
b=int(input("enter y intercept or 0 to quit: "))
if b == 0:
    ask = False
    break
'''
b=int(input("enter y intercept or 0 to quit: "))
slope=int(input("enter slope: "))
global rise
global run
rise=slope+b
run=10

#here is where we defined them
def graph():
    t.pu()
    t.goto(0,-250)
    
    t.pd()
    t.goto(0,250)
    t.pu()
    t.goto(-250,0)
    t.pd()
    t.goto(250,0)
    
def plot():
  t.pu()
  t.goto(0,b)
  t.pd()
  t.dot(5,"green")
  t.write(t.pos())

def slope():
  for i in range(3):
      #t.goto(run,rise)
      t.fd(run)
      t.lt(90)
      t.fd(rise)
      t.rt(90)
      t.pd()
      t.dot(5,"blue")
      t.write(t.pos())
      
#here is where we called  the functions
graph() 
plot()
slope()
