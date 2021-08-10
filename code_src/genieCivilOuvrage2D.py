import turtle
import math

from pont import deplace_toi

trace = turtle.Turtle()

# "Entrées : rayon, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Appel de fonction
#  Connu :"
def dessiner_cercle(rayon, draw = turtle.Turtle()):

    draw.circle(rayon)
    draw.home


# Entrées : rayon, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Appel de fonction
#  Connu :
def dessiner_demicercle(rayon,draw = turtle.Turtle()):

    draw.setheading(90)
    draw.circle(rayon, 180)
    draw.home

# Entrées : cote, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Usage d’une fonction itérative
#  Connu :
def dessiner_carre(cote):
    draw = turtle.Turtle()
    for i in range(4):
        draw.forward(cote)
        draw.left(90)


# Entrées : cote1, cote2, cote3, x, y, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Appel de fonction
#  Connu :
def dessiner_triangle(cote1, cote2, cote3,x,y, draw=turtle.Turtle()):
    # draw=turtle.Turtle()
    # trace.circle(cote1,90, steps=3)
    # trace.home()
    cosinus = ((cote1*cote1+cote2*cote2-cote3*cote3)/(2*cote1*cote2))
    print(cosinus)
    gamma = math.degrees(math.acos(cosinus))
    print(gamma)
    cosinus = (math.pow(cote1, 2)+math.pow(cote3, 2)-math.pow(cote2, 2))/(2*cote1*cote3)
    alpha=math.degrees(math.acos(cosinus))
    # x = (math.pow(cote2, 2) + math.pow(cote3, 2) - math.pow(cote1, 2)) / (2 * cote2 * cote3)
    # beta=math.acos(cosinus)
    draw.seth(0)
    draw.forward(cote1)
    draw.left(180-gamma)
    draw.forward(cote2)
    draw.left(180-alpha)
    # draw.forward(cote3)
    draw.goto(x,y)
    draw.seth(0)
    # trace.forward(cote3)
    # trace.left((beta))
    # draw.hideturtle()
    # draw.seth(0)



# Entrées : longueur, largeur,x_draw,y_draw draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Usage d’une fonction itérative
#  Connu :

def dessiner_rectangle(longueur, largeur,x_draw,y_draw,draw = turtle.Turtle()):
    deplace_toi(x_draw,y_draw,draw)
    for i in range(2):
        draw.forward(longueur)
        draw.left(90)
        draw.forward(largeur)
        draw.left(90)

#  Entrées : nombre_de_cote, cote, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Appel de fonction
#  Connu :
def dessiner_polygone(nombre_de_cote, cote, draw = turtle.Turtle()):

    draw.circle(cote, steps=nombre_de_cote)
    draw.home


# Entrées : petite_base, grande_base , hauteur,x_draw,y_draw,draw (étant la variable qui stock turtle),
# x_draw, y_draw
#  Sorties : draw
#  Méthodes : Appel de fonctio
def dessiner_trapeze(petite_base, grande_base, hauteur,x_draw,y_draw, draw= turtle.Turtle()):
    # draw.speed()
    deplace_toi(x_draw,y_draw,draw)
    draw.forward(petite_base)

    draw.goto(x_draw+grande_base, y_draw + hauteur)
    draw.backward(grande_base)
    draw.goto(x_draw,y_draw)

#  Entrées : cote, angle, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Usage d’une fonction itérative
#  Connu :
def dessiner_losange(cote, angle, draw = trace):

    for i in range(2):
        draw.forward(cote)
        draw.left(angle)
        draw.forward(cote)
        draw.left(180 - angle)

    draw.home()


#  Entrées : grand_axe, petit_axe, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Usage de fonction itérative
#  Connu
def dessiner_ellipse(grand_axe, petit_axe,draw = trace):

    # trace.shape("circle")
    # trace.shapesize(grand_axe, petit_axe, 2)
    draw.seth(45)
    for i in range(2):

        draw.circle(grand_axe,90)
        draw.circle(petit_axe ,90)

    trace.hideturtle()


#  Entrées : grand_axe, draw (étant la variable qui stock turtle)
#  Sorties : draw
#  Méthodes : Usage de l'objet turtle.circle
#  Connu
def dessiner_demiellipse(grand_axe, draw=turtle.Turtle()):

    # trace.goto(0,petit_axe)
    # trace.goto(0,0)
    # trace.fd(grand_axe)
    draw.seth(135)
    draw.circle(grand_axe, 90)
    # trace.seth(0)
    # trace.home()
    # dessiner_triangle(60, 60, 60)
    # trace.goto(0,0)



    trace.hideturtle()
    return draw

# def pont(taille):




