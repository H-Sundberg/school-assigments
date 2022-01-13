import turtle

t = turtle.Turtle()

# rita hängare
def start():
    t.clear()
    t.home()
    t.hideturtle()
    t.speed(0)
    t.color('#593b16')
    t.pensize(5)
    t.pendown()
    t.left(90)
    t.forward(175)
    t.left(90)
    t.forward(74)
    t.left(90)
    t.forward(35)
    t.penup()
    t.goto(-135,-35)
      

# rita huvud
def huvud():
    t.goto(-74, 140)
    t.pensize(3)
    t.color('#b3fffc')
    t.begin_fill()
    t.pendown()
    t.right(90)
    t.circle(15)
    t.penup()
    t.end_fill()

# rita kropp
def kropp():
    t.goto(-74, 140)
    t.pensize(4)
    t.pendown()
    t.color('#42f5bc')
    t.left(90)
    t.penup()
    t.forward(30)
    t.pendown()
    t.forward(40)
    t.right(180)
    t.forward(30)
    t.penup()

# rita första armen
def arm1():      
    t.goto(-74, 100)
    t.pensize(4)
    t.pendown()
    t.color('#42f5bc')
    t.left(55)
    t.forward(45)
    t.right(180)
    t.forward(45)
    t.penup()

# rita andra armen
def arm2():       
    t.goto(-74, 100)
    t.pensize(4)
    t.pendown()
    t.color('#42f5bc')
    t.left(70)
    t.forward(45)
    t.right(180)
    t.forward(45)
    t.penup()

# rita första benet
def ben1():  
    t.goto(-74, 100)
    t.pensize(4)
    t.pendown()
    t.color('#429bf5')
    t.left(55)
    t.penup()
    t.forward(30)
    t.pendown()
    t.right(30)
    t.forward(60)
    t.right(180)
    t.forward(60)
    t.penup()

# rita andra benet
def ben2():
    t.goto(-74, 70)
    t.pensize(4)
    t.pendown()
    t.color('#429bf5')
    t.right(120)
    t.forward(60)
    t.penup()
    

def felgissning(gissning):
    if gissning == 6:
        huvud()
    elif gissning == 5:
        kropp()
    elif gissning == 4:
        arm1()
    elif gissning == 3:
        arm2()
    elif gissning == 2:
        ben1()
    elif gissning == 1:
        ben2()