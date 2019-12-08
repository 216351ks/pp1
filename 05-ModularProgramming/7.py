import turtle

pen = turtle.Turtle()


for i in range(8):
    if i%2 == 0:
        pen.forward(100)
        
    else:
        pen.right(90)
        
turtle.done()