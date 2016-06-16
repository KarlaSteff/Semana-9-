from tkinter import *
tk= Tk()

canvas=Canvas(tk,width=800, height= 800)
canvas.pack()
my_image=PhotoImage(file = "ball.gif")
canvas.create_image(0,0, anchor=NW, image=my_image)
#canvas.create_image(10,10, anchor=NW, image=my_image)
#canvas.create_image(50,60, anchor=NW, image=my_image)
#canvas.create_image(80,20, anchor=NW, image=my_image)
tk.mainloop()
