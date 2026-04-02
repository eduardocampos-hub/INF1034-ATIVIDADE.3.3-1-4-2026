from turtle import *
from time import *
t = Turtle()

def desafio6(x):
    return x**3 - x**2 - x + 1

def plano_cartesiano():
    ## eixo x
    t.pu()
    t.goto(-300,0)
    t.pd()
    t.goto(300,0)
    t.stamp()

    ## eixo y

    t.pu()
    t.goto(0,-300)
    t.pd()
    t.goto(0,300)
    t.lt(90)
    t.stamp()

t.rt(90)
plano_cartesiano()
t.pu()
t.goto(-200,-500)
t.pd()
for x in range(-200,200):
    t.goto(x,desafio6(x/50)*10)
sleep(2)

mainloop()