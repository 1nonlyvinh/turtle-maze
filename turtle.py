import turtle
t = turtle.Turtle()
t.speed(10) 

def draw_maze():
  
	t.penup()
t.penup()
t.setpos(-200, 200)
t.pendown()

#Creates Outline:
x = [1, 2, 3]
for x in x:
 	t.forward(400)
 	t.right(90)
  
# Creates vertical lines
def vertical_line():
  t.left(90)
  t.forward(40)
  t.backward(40)
  t.right(90)

  
# First Row:
t.forward(360)
t.right(90)
t.forward(120)
t.penup()
t.forward(40)
t.pendown()
t.forward(120)
t.left(90)
t.forward(40)
t.backward(40)
t.right(90)
t.forward(40)
t.penup()
t.forward(40)
t.pendown()
t.forward(40)

# Second Row:
t.penup()
t.setpos(-200, 120)
t.pendown()
t.forward(40)
t.penup()
t.forward(40)
t.pendown()
t.forward(160)
t.left(90)
t.forward(40)
t.backward(40)
t.right(90)
t.penup()
t.forward(80)
t.pendown()
t.forward(80)

# Third Row:
t.penup()
t.setpos(-200, 80)
t.pendown()
t.forward(120)
t.penup()
t.forward(40)
t.pendown()
t.forward(120)
t.left(90)
t.forward(40)
t.backward(40)
t.right(90)
t.forward(40)
t.penup()
t.forward(40)
t.pendown()
t.forward(40)
 
# Fourth row:

t.penup()
t.setpos(-200, 40)
t.pendown()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
vertical_line()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
vertical_line()
t.forward(120)

# fifth row:

t.penup()
t.setpos(-200, 0)
t.pendown()
t.forward(120)
t.penup()
t.forward(40)
t.pendown()
vertical_line()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
t.forward(120)

# sixth row:
t.penup()
t.setpos(-200, -40)
t.pendown()
t.forward(40)
t.penup()
t.forward(40)
t.pendown()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
vertical_line()
t.forward(120)
t.penup()
t.forward(40)
t.pendown()
vertical_line()

# seventh row:
t.penup()
t.setpos(-200, -80)
t.pendown()
t.forward(80)
vertical_line()
t.penup()
t.forward(40)
t.pendown()
t.forward(160)
vertical_line()
t.penup()
t.forward(40)
t.pendown()
t.forward(80)

# eight row
t.penup()
t.setpos(-200, -120)
t.pendown()
t.forward(120)
vertical_line()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
t.forward(80)
t.penup()
t.forward(40)
t.pendown()
t.forward(40)

# ninth row:
t.penup()
t.setpos(-200, -160)
t.pendown()
t.forward(160)
t.penup()
t.forward(40)
t.pendown()
vertical_line()
t.forward(80) 
t.penup()
t.forward(40)
t.pendown()
t.forward(80)

# creates goal:

t.penup()
t.setpos(-200, -200)
t.fillcolor("#00FFFF")

t.begin_fill()

g = [1,2,3,4]
for g in g:
  t.forward(40)
  t.left(90)
  
t.end_fill()
