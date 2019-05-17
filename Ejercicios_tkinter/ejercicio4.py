from tkinter import *
root = Tk()
v = IntVar()# crea una variable para ser usada a medida q se usa el codigo 
#muestra un mensaje para que elija UNA SOLA opcion
Label(root,text="""Choose a programming language:""",justify = LEFT,padx = 20).pack()
#crea el boton y le da nombre y le da una valuacion 1
Radiobutton(root,text="Python",padx = 20,variable=v,value=1).pack(anchor=W)
#crea otro boton y le da nombre y le da una valuacion 1
Radiobutton(root,text="Perl",padx = 20,variable=v,value=2).pack(anchor=W)
mainloop()