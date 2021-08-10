import genieCivilOuvrage2D as tracer
import turtle
import arbre
from  pont import  deplace_toi



def escalier(longueur, largeur,x,y, t=turtle.Turtle()):
    # x=-50
    # y=0
    t.speed(10)
    for i in range(1,7):
       deplace_toi(x,y,t)
       tracer.dessiner_rectangle(longueur,largeur,x,y,t)
       x+=5
       y+=largeur
       longueur-=10
    t.hideturtle()

    return


def porte(hauteur, largeur,x,y, t=turtle.Turtle()):
    t.speed(10)
    deplace_toi(x,y,t)
    t.begin_fill()
    t.fillcolor("#FFFFFF")
    tracer.dessiner_rectangle(largeur,hauteur,x,y,t)
    t.end_fill()
    deplace_toi(x+largeur/2, y, t)
    t.seth(90)
    t.forward(hauteur)
    deplace_toi(x, hauteur/2, t)
    t.seth(0)
    t.forward(largeur)
    deplace_toi(x+largeur,hauteur,t)
    tracer.dessiner_demicercle(largeur/2,t)
    deplace_toi(x+largeur/5,(hauteur+largeur),t)
    t.begin_fill()
    t.fillcolor("black")
    tracer.dessiner_cercle(largeur/3, t)
    t.end_fill()
    deplace_toi(x, (hauteur + 2.5*largeur), t)
    t.begin_fill()
    t.fillcolor("#FFFFFF")
    tracer.dessiner_rectangle(30,largeur,x, (hauteur + 2.5*largeur),t)
    t.end_fill()
    deplace_toi(x+largeur/2,(hauteur + 2.5*largeur)-30, t)
    t.seth(90)
    t.forward(30)
    t.hideturtle()

def face_porte(hauteur, largeur,x,y, t=turtle.Turtle()):
    t.speed(15)
    #x=10
    #y=0
    t.begin_fill()
    t.fillcolor("#dddddd")
    tracer.dessiner_rectangle(hauteur,largeur,x,y,t)
    t.end_fill()
    # deplace_toi(-x,y,t)
    tracer.dessiner_rectangle(hauteur+20,largeur,-x+10,y,t)
    # deplace_toi(-x-10, 0, t)
    tracer.dessiner_rectangle(hauteur+40, largeur,-x, 0,t)
    tracer.dessiner_rectangle(35,-10,-x, 0,t)
    # deplace_toi(hauteur+20,0,t)
    tracer.dessiner_rectangle(-35,-10,hauteur+30,0,t)
    # deplace_toi(-x-20,largeur,t)
    tracer.dessiner_rectangle(hauteur+60, 30,-x-10,largeur, t)
    t.hideturtle()

def face_laterale(hauteur, largeur,x,y, t=turtle.Turtle()):
    t.speed(13)
    tmp=x
    deplace_toi(x,-y,t)
    tracer.dessiner_rectangle(10,-50,x,-y,t)
    deplace_toi(x+10,-y-50,t)

    t.forward(largeur)
    if (tmp < 0):
        t.seth(-90)
    else:
        t.seth(90)

    t.forward(hauteur)
    t.seth(180)
    if(tmp<0):
        t.forward(largeur+20)
    else:
        t.forward(largeur - 10)
    x=t.xcor()
    y=t.ycor()

    t.seth(0)
    if(tmp<0):
        # t.seth(0)
        tracer.dessiner_trapeze(largeur+20 , largeur-10, 20, x, y, t)
    else:
         tracer.dessiner_trapeze(largeur-10,largeur+30,20,x,y,t)


    t.hideturtle()

def fenetre(longueur, largeur, x, y, t=turtle.Turtle()):
    t.speed(10)
    #x=120
    #y=35
    # 80, 230
    deplace_toi(x,-y,t)
    t.begin_fill()
    t.fillcolor("#70726E")
    tracer.dessiner_rectangle(longueur, largeur,x,-y, t)
    t.end_fill()
    x=t.xcor()
    y=t.ycor()
    deplace_toi(x+5, y+5, t)
    t.begin_fill()
    t.fillcolor("#FFFFFF")
    tracer.dessiner_rectangle(30+longueur/2,largeur/2,x+5, y+5, t)
    t.end_fill()
    x = t.xcor()
    y = t.ycor()
    deplace_toi(x+(30+longueur/2)/2,y, t)
    t.goto(x+(30+longueur/2)/2, (30+longueur/2)+15)
    deplace_toi(x,y+largeur/4,t)
    t.forward(longueur-10)
    # t.hideturtle()
    y=y+20+largeur/2
    deplace_toi(x, y, t)
#     ----------new window
    t.begin_fill()
    t.fillcolor("#FFFFFF")
    tracer.dessiner_rectangle(30 + longueur / 2, largeur / 3,x, y, t)
    t.end_fill()
    x = t.xcor()
    y = t.ycor()
    deplace_toi(x + (30 + longueur / 2) / 2, y+largeur / 3, t)
    t.seth(-90)
    t.forward( largeur / 3)
    t.seth(0)
    deplace_toi(x, (y + (largeur / 3)/2), t)
    t.forward(longueur - 10)

    t.hideturtle()

def fenetre_toit(pos_x,pos_y,nbr,t=turtle.Turtle()):
    #pos_x = 200
    #pos_y = 230
    t.speed(10)
    deplace_toi(pos_x+10, pos_y, t)
    if (nbr==3):
        for j in range(3):
            for i in range(2):
                tracer.dessiner_rectangle(10, 30,t.xcor(), pos_y, t)
                deplace_toi(t.xcor() + 10, pos_y, t)

            deplace_toi(t.xcor() + 20, pos_y, t)
    else:
        for i in range(2):
            tracer.dessiner_rectangle(10, 30, t.xcor(), pos_y, t)
            deplace_toi(t.xcor() + 10, pos_y, t)
    t.hideturtle()


def plafond(x,y,t=turtle.Turtle()):
    # x = 200
    # y = 230
    t.speed(10)
    deplace_toi(x, y,t)
    tracer.dessiner_rectangle(150,40,x,y,t)
    deplace_toi(x,y+40,t)
    t.begin_fill()
    t.fillcolor("#B0F2B6")
    tracer.dessiner_triangle(150,80,80,x,y+40,t)
    t.end_fill()
    t.hideturtle()

def cap(t=turtle.Turtle()):
    t.speed(10)
    # fermer le  chapeau toit----------------------
    deplace_toi(263, 298, t)
    t.begin_fill()
    t.fillcolor("#B0F2B6")
    t.seth(180)
    t.forward(422)
    deplace_toi(-87, 270, t)
    t.seth(0)
    t.forward(280)
    t.end_fill()
    t.hideturtle()


# #     fin chapequ----------------------

def house():
    t=turtle.Turtle()
    x=130
    y=35
    #
    face_porte(90, 200, 10, 0)
    porte(90, 40,35,0)
    escalier(110,10,0,-60)

    face_laterale(270, 400,110,10)
    for i in range(3):
        fenetre(80, 230, x,y)
        x+=120
    x=130
    face_laterale(-270, -400, -10, 10)
    for i in range(3):
        fenetre(80,230,-x+25,y)
        x+=120

    plafond(190,230)
    fenetre_toit(200, 230,3)
    plafond(-230,230)
    fenetre_toit(-220,230,3)
    fenetre_toit(-10,230,3)
    fenetre_toit(120,230,1)
    fenetre_toit(-50, 230, 1)
    cap(t)
    arbre.planter()









