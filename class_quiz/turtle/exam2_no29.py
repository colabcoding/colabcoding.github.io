import turtle
import time
turtle.penup()
turtle.goto(-200,0)
turtle.bgcolor('#f0f0f0')
while True:
    turtle.addshape('frame0.gif')
    turtle.shape('frame0.gif')
    turtle.forward(5)
    time.sleep(0.1)
    turtle.addshape('frame1.gif')
    turtle.shape('frame1.gif')
    turtle.forward(5)
    time.sleep(0.1)
    turtle.addshape('frame2.gif')
    turtle.shape('frame2.gif')
    turtle.forward(5)
    time.sleep(0.1)
    if turtle.xcor() >100:
        break
