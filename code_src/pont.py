import turtle
import math

import genieCivilOuvrage2D as tracer

def hauteur(poteau,longueur):
    h = math.sqrt((poteau*poteau)-(longueur*longueur))
    return h

def poteau(x,h,draw=turtle.Turtle()):
    draw.forward(x)
    draw.left(90)
    draw.forward(hauteur(h, x))
    draw.backward(hauteur(h, x))
    draw.seth(0)

def deplace_toi(x,y,t=turtle.Turtle):
    t.penup()
    t.goto(x,y)
    t.pendown()

def support(longueur,largeur,x_t,y_t,t=turtle.Turtle()):

    t.begin_fill()
    t.fillcolor("blue")
    tracer.dessiner_rectangle(longueur,largeur,x_t,y_t, t)
    t.end_fill()

def pont(x_t,y_t, t = turtle.Turtle()):
    # x_t=400
    # y_t=0

    t.penup()
    t.goto(-x_t,y_t)
    t.pendown()
    tracer.dessiner_triangle(65, 60, 40, -x_t, y_t, t)
    t.goto(-x_t+65, 0)
    tracer.dessiner_triangle(90, 90, 90, t.xcor(),y_t,t)

    t.goto(t.xcor()+90, 0)
    tracer.dessiner_triangle(90, 97, 97, t.xcor(), y_t, t)
    t.goto(t.xcor()+90, 0)
    tracer.dessiner_triangle(90, 84, 83, t.xcor(),y_t,t)
    t.goto(t.xcor()+90, 0)
    tracer.dessiner_triangle(65, 45, 42, t.xcor(), y_t, t)
    t.goto(t.xcor()+65, 0)
    print(t.pos())
    tracer.dessiner_demiellipse(300, t)
    t.goto(-x_t, y_t)
    t.seth(0)
    t.forward(17)
    t.left(90)
    t.forward(hauteur(40, 17))
    t.penup()
    t.goto(-x_t, y_t)
    t.seth(0)
    t.pendown()
    poteau(65, 90, t)
    poteau(45,90,t)
    poteau(45,97,t)
    poteau(45, 97, t)
    poteau(45, 94, t)
    poteau(45, 83, t)
    poteau(45, 65, t)
    poteau(65/2, 42, t)
    # t.hideturtle()

def construire_ponts():
    t=turtle.Turtle()
    t.speed(15)

    # -------------------new support
    # deplace_toi(-680, -45, t)
    support(100, 25,-680, -45, t)
    # deplace_toi(-680, -20, t)
    support(75, 20,-680, -20, t)
    # -------------------new support
    # deplace_toi(-300, -45, t)
    support(100, 25,-300, -45, t)
    # deplace_toi(-290, -20, t)
    support(75, 20,-290, -20, t)
    # -------------------new support
    # deplace_toi(100, -45, t)
    support(100, 25,100, -45, t)
    # deplace_toi(110, -20, t)
    support(75, 20,110, -20, t)
    # -------------------new support
    # deplace_toi(500, -45, t)
    support(100, 25,500, -45, t)
    # deplace_toi(510, -20, t)
    support(75, 20, 510, -20, t)
    # -------------------new pont
    t.pensize(6)
    t.color("#77B5FE")
    pont(650,0,t)
    # -----------------new pont
    pont(250, 0, t)
#     --------------------new pont
    pont(-150,0,t)



