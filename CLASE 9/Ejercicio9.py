import turtle

def funcion(numero, diametro):
	t=turtle.Pen()
	angulo=360/numero
	for x in range (1,numero+1):
		t.forward(diametro)
		t.left(angulo)
	turtle.getscreen()._root.mainloop()

num=int(input("Ingrese el número de lados: "))
dia=int(input("Ingrese la longitud: "))		

funcion(num,dia)
