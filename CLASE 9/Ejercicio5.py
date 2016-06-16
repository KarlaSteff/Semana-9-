import turtle
num= input("Ingrese un número: ")
numero = int(num)
t=turtle.Pen()
for x in range (1,numero+1):
	lados= 360/numero
	t.forward(100)
	t.left(lados)
turtle.getscreen()._root.mainloop()