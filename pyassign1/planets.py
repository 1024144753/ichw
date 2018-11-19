import turtle
import math

wn=turtle.Screen()
wn.bgcolor('white')
wn.setworldcoordinates(-700,-600,600,500)
sun = turtle.Turtle()
sun.color('red')
sun.shape('circle')
speed_list=[6,7,8,9,10,0]

planets_list = []
for i in range(6):
    a = turtle.Turtle()
    a.shape('circle')
    a.penup()
    planets_list.append(a)
    

planets_list[0].color('blue','blue')
planets_list[1].color('yellow','yellow')
planets_list[2].color('green','green')
planets_list[3].color('hotpink','hotpink')
planets_list[4].color('brown','brown')
planets_list[5].color('black','black')

a_list = [60, 110, 172, 260, 300, 350]
b_list = [50, 100, 170, 250, 280, 320]

def planets_move(t, i, a, b):
    c =(a**2 - b**2)**(0.5)
    x = a * math.cos(math.radians(t))-c
    y = b * math.sin(math.radians(t))
    i.goto(x, y)
    i.pendown()
    
for t in range(1, 4000):
    for i in range(6):
        planets_list[i].speed(speed_list[i])
        planets_move(t, planets_list[i], a_list[i], b_list[i])
        
        
        


