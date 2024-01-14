from tkinter import *


def esconder():
    texto.place_forget()



root = Tk()

texto = Label(root, text = 'Exemplo')
texto.place(x=200, y=200)

bt = Button(root, text = 'Esconder', command = esconder)
bt.pack()


root.geometry('400x400')
root.mainloop()