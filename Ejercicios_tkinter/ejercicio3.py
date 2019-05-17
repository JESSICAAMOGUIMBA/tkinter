from tkinter import *
#ejercico de una ventana con botones de opcion
class App:
	def __init__(self, master):
		frame = Frame(master)
		frame.pack()
		self.button = Button(frame, text="SALIR",fg="red",command=frame.quit)#BOTON SALI CON LETRA ROJA
		self.button.pack(side=LEFT)
		self.slogan = Button(frame,text="ENTRAR",command=self.write_slogan)#BOTON ENTRAR EL CUAL EJECUTA 
																			#UN MENSAJE "Estamos aprendiendo a usar Tkinter!"
		self.slogan.pack(side=LEFT)

	def write_slogan(self):
 		print ("Estamos aprendiendo a usar Tkinter!")

root = Tk()
app = App(root)
root.mainloop()