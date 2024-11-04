import turtle
import time

t = turtle.Turtle()
t.speed(0) 

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

# player movement: thanks rubber ducky

screen = turtle.Screen()
player = turtle.Turtle()

player.penup()
player.setpos(-200, 180)

def move_up():
    player.setheading(90)
    player.forward(20)

def move_down():
    player.setheading(270)
    player.forward(20)

def move_left():
    player.setheading(180)
    player.forward(20)

def move_right():
    player.setheading(0)
    player.forward(20)

# Bind keys to movement
screen.listen()
screen.onkey(move_up, "Up")
screen.onkey(move_down, "Down")
screen.onkey(move_left, "Left")
screen.onkey(move_right, "Right")

screen.mainloop()

t.penup()
t.setpos(-200, -200)

color = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

w = 5
while w == 5:
    if player.xcor() == -200 and player.ycor() == -200:
        for i in range(5000):
          t.pendown()
          t.forward(i)
          t.color(color[i % len(color)])
          t.left(500)
        break  # Exit the while loop after drawing the star
    time.sleep(0.1)  # Add a small delay to prevent crashing
    

