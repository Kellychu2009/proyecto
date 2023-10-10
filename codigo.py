


import tkinter as tk
from tkinter import ttk,Button,Label,Tk,messagebox

Ventana = Tk()
Ventana.title("Convertidor")
Ventana.geometry("500x200")
Ventana.config(background="#D1F19C")

def selecion():
    selec = combo.get()
    if selec == "Metros a centimetros":
        dat = int(entradaUno.get())
        r = dat*100
        messagebox.showinfo(
        message=f"el numero de centimetros es de : {r}",
        title="Metros a centimetros"
    )
    if selec == "Centimetros a metros":
        dat = int(entradaUno.get())
        r = dat/100
        messagebox.showinfo(
        message=f"el numero de metros es de : {r}",
        title="Centimetros a metros"
    )

titulo = Label(Ventana,text="Bienvenido",background="#D1F19C",width=10,height=3).pack()

combo = ttk.Combobox(
    state="readonly",
    values=["Metros a centimetros","Centimetros a metros"]
)
combo.place(x=10,y=50)


b1 = Button(Ventana,text="eject",width=4,height=1,command=selecion)
b1.place(x=290,y=50)

entradaUno = tk.Entry(Ventana,background="#64724D",foreground="White")
entradaUno.place(x=170,y=50,height=20,width=100)

Ventana.mainloop()
