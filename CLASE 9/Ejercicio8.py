import turtle
num= int(input("Ingrese un número  "))
t=turtle.Pen()
for x in range (1,5):
	t.forward(num)
	t.left(90)

turtle.getscreen()._root.mainloop()