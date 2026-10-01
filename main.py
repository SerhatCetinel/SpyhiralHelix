import turtle

turtle_screen = turtle.Screen()
turtle_screen.bgcolor("white")
turtle_screen.title("Turtttle")

turtle.speed(10)

turtle_instance = turtle.Turtle()
turtle_instance.color("black")
turtle_colors = ["red","purple","blue","green","yellow"]

for i in range(15):
    turtle_instance.color(turtle_colors[i % 4])
    turtle_instance.circle(10 * i)
    turtle_instance.circle(-10 * i)
    turtle_instance.left(i)


turtle.mainloop()

