#Import turtle module
import turtle as turtle
#Import randome module
import random

#In the console, print a welcome and instruct user to pick a shape to draw
print("Welcome to your drawing app! Select a shape you want to draw. After typing the number and hitting enter, go to the result tab!")

#In the result, pen appears on the screen and moves up, left, down and right
turtle.penup()
turtle.left(90)
turtle.forward(250)
turtle.left(90)
turtle.forward(300)
turtle.pendown()

#As the pen moves, the app title appears
turtle.write("Drawing App!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.left(90)
turtle.forward(50)
turtle.pendown()

#Instruct the user to pick a shape on the console tab
turtle.write("To draw a shape, go to the Console tab and choose an option!", font=("Arial", 16, "normal"))

turtle.penup()
turtle.forward(150)
turtle.left(90)
turtle.forward(150)
turtle.pendown()

#Define star function by looping through a range of 0 to 5 and drawing with the pen forward 110 pixels and left 216 pixels five times
def star():
  for i in range(0,5):
    turtle.forward(110)
    turtle.left(216)
  # Star

#Define square function by looping through a range of 0 to 4 and drawing with the pen forward 100 pixels and right 90 pixels four times
def square():
  for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)

  # Square

#Define hexagon function by looping through a range of 0 to 6 and drawing with the pen forward 100 pixels and right 60 pixels six times
def hexagon():
  for i in range(0,6):
    turtle.forward(100)
    turtle.right(60)
  # Hexagon

#Create a variable named selection that takes user input to determine wich shape to draw and instructs the user to see the drawing on the result tab
selection = input("1. Star\n2. Square\n3. Hexagon\nSelect a number: ")
if selection == "1":
  print("Excellent choice! Go to the result tab to see your creation.")
  star()
elif selection == "2":
  print("Excellent choice! Go to the result tab to see your creation.")
  square()
elif selection == "3":
  print("Excellent choice! Go to the result tab to see your creation.")
  hexagon()