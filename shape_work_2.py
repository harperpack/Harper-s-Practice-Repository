# Practice with drawing, shapes, and Turtle class

import turtle

# define the shape to be drawn
def draw_square(some_turtle, some_size):
	for each_count in range(1,5):
		some_turtle.forward(some_size)
		some_turtle.right(90)


# create a Turtle that will make our small shape
tiny = turtle.Turtle()
tiny.color("purple")
tiny.shape("arrow")
tiny.speed(20)

# create a Turtle that will make our medium shape
medium = turtle.Turtle()
medium.color("blue")
medium.shape("square")
medium.speed(40)

# create a Turtle that will make our large shape
biggie = turtle.Turtle()
biggie.color("green")
biggie.shape("triangle")
biggie.speed(80)

# build the loop to draw the shape multiple times
window = turtle.Screen()
window.bgcolor("yellow")
for each_degree in range (1,37):
	draw_square(medium, 100)
	medium.right(10)
	draw_square(tiny, 50)
	tiny.right(10)
	draw_square(biggie, 200)
	biggie.right(10)
window.exitonclick()
