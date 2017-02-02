# Lesson 3.3: Use Classes
# Mini-Project: Draw Turtles

# turtle is a library we can use to make simple computer
# graphics. Kunal wants you to try drawing a circles using
# squares. You can also use this space to create other
# kinds of shapes. Experiment and share your results
# on the Discussion Forum!

import turtle

def draw_square():
    brad=turtle.Turtle()
    brad=turtle.Turtle()
    brad.shape("turtle")
    brad.color("green")
    brad.speed(2)
    k=0
    while k<4: 
        brad.forward(100)
        brad.right(90)
        k+=1    

def draw_circle():
    liz=turtle.Turtle()
    liz.shape("arrow")
    liz.color("yellow")
    liz.speed(1)
    liz.circle(100)


def draw_circle2():    
    andy=turtle.Turtle()
    andy.shape("circle")
    andy.speed=10
    j=0
    while j<36:
        andy.right(10)
        k=0
        while k<4: 
            andy.forward(100)
            andy.right(90)
            k+=1
        j+=1


def draw_triangle(some_t,length,depth):
    k=0
    L=[]
    while k<3:
        some_t.forward(length*1./2)
        if depth>0:
            some_t.left(120)
            draw_triangle(some_t,length*1./2,depth-1)
            some_t.right(120)
        some_t.forward(length*1./2)
        some_t.right(120)
        k+=1
            
def draw_fractle():
    jack=turtle.Turtle()
    jack.color("red")
    jack.speed(10)
    length=2**8
    depth=3
    #draw the outer triangle
    k=0
    while k<3:
        jack.forward(length)
        jack.left(120)
        k+=1
    length=length*1./2
    x=length
    y=0
    jack.goto(x,y)
    jack.left(120)
    draw_triangle(jack,length,depth)
     
                 
def draw_graphics():
    window=turtle.Screen()
    window.bgcolor("blue")
    draw_square()
    draw_circle()
    draw_circle2()
    draw_fractle()
    window.exitonclick()

draw_graphics()
