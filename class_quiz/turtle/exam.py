import turtle
skippy=turtle.Turtle()
skippy.pensize(2)
#skippy.hideturtle()
#turtle.bgcolor('#f0f0f0')
# turtle.bgcolor('green')
turtle.bgpic('road.gif')
turtle.setup()
skippy.speed(1000)
def shape(n,r,size=200):
    for i in range(r):
        for i in range(n):
            skippy.forward(100)
            skippy.left(360//n)
        skippy.right(360//r)
        #skippy.right(30)

# r=100
# skippy.right(90)
# skippy.circle(r,180)
# skippy.fillcolor("red")
# skippy.begin_fill()
# skippy.circle(100)
# skippy.end_fill()