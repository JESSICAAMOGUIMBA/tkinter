from tkinter import *
root = Tk()
v = IntVar()
v.set(1) # initializing the choice, i.e. Python
#hace un arreglo con las opc y un mensaje (numeros)
languages = [
("Python","1"),#le puedo poner entre comillas
("Perl",2),
("Java",3),
("C++",4),
("C",5)]

#nos perite hacer una eleccion
def ShowChoice():
	print (v.get())

Label(root,
	text="""Choose your favourite programming language:""",justify = LEFT,padx = 20).pack()
#crea un for en el cual a cada uno de las opc del arreglo le da su respectivo texto
for txt, val in languages:
	Radiobutton(root,text=txt,padx = 30,
		variable=v,command=ShowChoice,
		value=val).pack(anchor=W)
mainloop()