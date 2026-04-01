from turtle import *
from time import *
t = Turtle()
t.speed(10)
# FUNCOES

def soma_2(x):
    return x + 2

def raizdeX(x):
    return x**0.5

def umsobrex(x):
    return 1/x

def elevado(x):
    return 2**x

def desafio4(x):
    return 5-x**2

def desafio5(x):
    return  x**2 - 5*x + 6
#plano cartesiano--------------------------------------------------|
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

# desenho da função------------------------------------------------|

# t.color('red')
# t.pu()
# t.goto(-100,soma_2(-100))
# t.pd()
# t.goto(100,soma_2(100))

# o range vai do primeiro numero ate o ultimo - 1

# print(list(range(-100,100)))

plano_cartesiano()
t.pu()
t.goto(0,raizdeX(0))
t.pd()
for x in range(10,400):
    t.goto(x*2,raizdeX(x*2))

sleep(2)
t.clear()

t.rt(90)
plano_cartesiano()
t.pu()
t.goto(-299,umsobrex(10))
t.pd()
for x in range(-299,0):
    t.goto(x,umsobrex(x/50)*10)

for x in range(1,299):
    t.goto(x,umsobrex(x/50)*10)
sleep(2)
t.clear()

t.rt(90)
plano_cartesiano()
t.pu()
t.goto(0,elevado(0))
t.pd()
for x in range(0,400):
    t.goto(x,elevado(x/50)*10)
sleep(2)
t.clear()


t.rt(90)
plano_cartesiano()
t.pu()
t.goto(0,0)
t.pd()
for x in range(0,400):
    t.goto(x,desafio4(x/50)*10)
sleep(2)
t.clear()

t.rt(90)
plano_cartesiano()
t.pu()
t.goto(-100,400)
t.pd()
for x in range(-100,400):
    t.goto(x,desafio5(x))
sleep(2)
t.clear()

mainloop()