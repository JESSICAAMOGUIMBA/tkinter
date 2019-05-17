from tkinter import *
#mensaje con modificaciones
master = Tk()
whatever_you_do = "What ever you do will be insignificant, but it is very important that you do it.\n(Mahatma Gandhi)"
msg = Message(master, text = whatever_you_do)
msg.config(bg='lightgreen', font=('times', 24, 'italic'))#da color de fondo,tipo de letra,tamaño,cursiva
msg.pack( )
mainloop( )