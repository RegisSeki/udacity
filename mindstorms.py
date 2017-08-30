import turtle

def perform():
  window = turtle.Screen()
  window.bgcolor("black")
  draw_square()
  draw_circle()
  draw_triangle()
  window.exitonclick()

def draw_square():
  square = turtle.Turtle()
  square.shape("turtle")
  square.color("green")
  for x in range(0, 4):
   square.forward(150)
   square.right(90)  

def draw_circle():
  circle = turtle.Turtle()
  circle.shape("circle")
  circle.color("red")
  circle.circle(50)

def draw_triangle():
  triangle = turtle.Turtle()
  triangle.shape("arrow")
  triangle.color("white")
  for x in range(0, 3):
    triangle.forward(240)
    triangle.left(480)

perform()
