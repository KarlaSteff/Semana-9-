import turtle
num= int(input("Ingrese un número impar: "))
t=turtle.Pen()

for x in range (1,num+1):
	v=(180-(90+90)/num)

	t.forward(100)
	t.left(v)
turtle.getscreen()._root.mainloop()