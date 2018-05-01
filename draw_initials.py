import turtle

# create Turtle for drawing
harper = turtle.Turtle()
harper.color("blue")
harper.shape("square")
harper.speed(2)

window = turtle.Screen()

#create the H
harper.left(90)
harper.forward(100)
harper.right(180)
harper.forward(50)
harper.left(90)
harper.forward(33)
harper.left(90)
harper.forward(50)
harper.right(180)
harper.forward(100)

# move to create the P
harper.penup()
harper.left(90)
harper.forward(25)

# create the P
harper.pendown()
harper.left(90)
harper.forward(100)
harper.right(90)
harper.forward(15)
harper.right(45)
harper.forward(20)
harper.right(45)
harper.forward(20)
harper.right(45)
harper.forward(20)
harper.right(45)
harper.forward(15)

window.exitonclick()
