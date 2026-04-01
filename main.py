from turtle import *

t = Turtle()

# FUNCOES

def soma_2(x):
    return x + 2


#plano cartesiano--------------------------------------------------|

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
print(list(range(-100,100)))
t.pu()
t.goto(-100,soma_2(-100))
t.pd()
for x in range(-99,101):
    t.goto(x,soma_2(x))


mainloop()