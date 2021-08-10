import turtle
from turtle import *

angle = 30
color('#3f1905')
speed(0)
t=turtle.Turtle()

# "Entrées :
#  Sorties :
#  Méthodes :
#  Connu :
def arbre(n,longueur):

    if n==0:
        color('green')
        forward(longueur) # avance
        backward(longueur) # recule
        color('#3f1905')
    else:
        width(n)
        forward(longueur/3) #avance
        left(angle) # tourne vers la gauche de angle degrés
        arbre(n-1,longueur*2/3)
        right(2*angle) # tourne vers la droite de angle degrés
        arbre(n-1,longueur*2/3)
        left(angle) # tourne vers la gauche de angle degrés
        backward(longueur/3) # recule


# "Entrées :
#  Sorties :
#  Méthodes :
#  Connu :
def deplace(x,y):

    penup()
    goto(x,y)
    pendown()
    seth(90)
    # arbre(10,100) #


# "Entrées :
#  Sorties :
#  Méthodes :
#  Connu :


def planter():
    # x=300
    # y=300

    deplace(-160, -190)
    arbre(8,90)
    deplace(210,-190)
    arbre(8, 90)
    deplace(-230,-290)
    arbre(8, 90)
    deplace(250,-290)
    arbre(8, 90)
    deplace(-110,-120)
    arbre(4,60)
    deplace(160, -120)
    arbre(4, 50)

    begin_fill()
    fillcolor('#3f1905')
    deplace(-10,-60)
    seth(0)
    forward(130)
    goto(220, -290)
    backward(400)
    goto(-180,-290)
    goto(-10, -60)
    end_fill()
    # deplace(50,-75)
    # pensize(10)
    # pencolor("white")
    # goto(45,-275)


showturtle() # affiche la tortue
# mainloop()