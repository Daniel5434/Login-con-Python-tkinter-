import tkinter as tk
from tkinter import Entry, Label, Tk, font, ttk
from tkinter.font import BOLD, ITALIC, families
from typing import Text
from time import *
#from login1 import ventanaUno
def ventanaDos():
    ventanaDos=tk.Tk()
    ventanaDos.title("REGISTRO DE ARTICULOS")
    ventanaDos.geometry("1199x600+50+20")
    lbltitulo=Label(ventanaDos, text="PRODUCTOS", font=("Arial", 50, BOLD))
    lbltitulo.place(x=400, y=20)

    lblproducto=Label(ventanaDos, text="Tipo de equipo", font=("Arial", 15, BOLD))
    lblproducto.place(x=50, y=130)  
    entryproducto=Entry(ventanaDos, justify="center")
    entryproducto.place(x=200, y=130)

    lblnumeroarticulos=Label(ventanaDos, text="N° productos: ",  font=("Arial", 15, BOLD))
    lblnumeroarticulos.place(x=50, y=190)
    entrynumeroarticulos=Entry(ventanaDos, justify="center")
    entrynumeroarticulos.place(x=200, y=190)

    lblnumseriearticulo=Label(ventanaDos, text="Número serie: ", font=("Arial", 15, BOLD))
    lblnumseriearticulo.place(x=50, y=250)
    entrnumseriearticulo=Entry(ventanaDos, justify="center")
    entrnumseriearticulo.place(x=200, y=250)
        
    ventanaDos.mainloop()
ventanaDos()