from logging import log
from os import error
from tkinter import * 
from tkinter import ttk, PhotoImage, messagebox
from tkinter.font import BOLD, ITALIC
from PIL import ImageTk
import mysql.connector as mysql
from mysql.connector.errors import Error

def ventanaUno():
    #Configuración inicial de la ventana
    ventana=Tk()   #Creamos la ventana
    ventana.geometry("1199x600+50+20") #Dimensiones de la pantalla y posición al abrir
    imagenLogin=ImageTk.PhotoImage(file='fondo1.jpg') 
    labelImagenLogin=Label(ventana, image=imagenLogin)
    labelImagenLogin.place(x=0, y=0)
    ventana.iconbitmap("icono.ico")
    ventana.title("Login")
    #Login Frame
    frame_login=Frame(ventana, bg="white") #Cuadro blanco en el centro
    frame_login.place(x=330, y=100, width=450, height=440)

    #Label(s) y Entr(s) de la ventana prinicpal
    label_principal=Label(frame_login, text="LOGIN", font=("Impact", 30, BOLD), bg="white", fg="green") #Título
    label_principal.place(x=175, y=10)

    lbl_msg_login=Label(frame_login, text="Inicie sesión con su cuenta", font=("Arial", 12, ITALIC), bg="white", fg="gray")
    lbl_msg_login.place(x=125, y=80)

    labelnombre=Label(frame_login, text="Usuario ", font=("Arial", 14,BOLD), bg="white", fg="green") #Nombre
    labelnombre.place(x=100, y=130)
    entrynombre=Entry(frame_login, font=("Arial", 14, ITALIC), justify="center", fg="gray",  bg="#E7E6E5")
    entrynombre.place(x=100, y=165,width=280, height=35)

    labelpass=Label(frame_login, text="Contraseña ", font=("Arial", 14, BOLD), bg="white", fg="green") #Password
    labelpass.place(x=100, y=220)
    entrypass=Entry(frame_login, show="*",justify="center", font=("Arial", 14, ITALIC), fg="gray", bg="#E7E6E5")
    entrypass.place(x=100, y=255, width=280, height=35)


    ######################################
    def btnclick():
        nmbre=entrynombre.get()
        pswd=entrypass.get()

        if entrynombre.get()=='' or entrypass.get()=='':
            if entrynombre.get()=='' and entrypass.get()=='':
                messagebox.showwarning(title="WARNING", message="Ingrese su usuario y contraseña.")
            elif entrynombre.get()=='':
                messagebox.showwarning("WARNING", "Ingrese su nombre.")
            elif entrypass.get()=='':
                messagebox.showwarning("WARNING", "Ingrese su contraseña.")
            else:
                messagebox.showerror("ERROR", "Ha ocurrido un error, intentelo mas tarde.")
        else:
            try:
                con = mysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password="123456789",
                    database="AplicacionR")
                cursor = con.cursor()
                cursor.execute("insert into usuarios(id, nombre, contraseña) values (Null, '"+ entrynombre.get() +"', '"+ entrypass.get() +"')")
                cursor.execute("commit")
                messagebox.showinfo("Estado de registro", "Usuario registrado exitosamente.")
                entrynombre.delete(0, END)
                entrypass.delete(0, END)
                con.close()
            except Error as error:
                messagebox.showerror(title="Error", message="Intentelo mas tarde, estamos teniendo problemas.")
                #print("Error en: ", error)
    ######################################
    ######################################
    def btnlogin():
        if entrynombre.get()=='' or entrypass.get()=='':
            if entrynombre.get()=='' and entrypass.get()=='':
                messagebox.showwarning(title="WARNING", message="Ingrese su usuario y contraseña.")
            elif entrynombre.get()=='':
                messagebox.showwarning("WARNING", "Ingrese su nombre.")
            elif entrypass.get()=='':
                messagebox.showwarning("WARNING", "Ingrese su contraseña.")
            else:
                messagebox.showerror("ERROR", "Ha ocurrido un error, intentelo mas tarde.")
        else:
            try:
                con = mysql.connect(
                    host="127.0.0.1",
                    user="root",
                    password="123456789",
                    database="AplicacionR")
                cursor = con.cursor()
                cursor.execute("select * from usuarios where nombre='"+entrynombre.get()+"' and contraseña='"+entrypass.get()+"'")
                result = cursor.fetchone()
                cursor.execute("commit")
                if result:
                    entrynombre.delete(0, END)
                    entrypass.delete(0, END) 
                    messagebox.showinfo("Bienvenido", "Bienvenido.")
                    from ventana2 import ventanaDos
                    #ventanaDos()
                else:
                    messagebox.showerror("WARNING", "Usuario o contraseña incorrectos.")
                entrynombre.delete(0, END)
                entrypass.delete(0, END)                
                con.close()
                cursor.close()
            except Error as error:
                messagebox.showerror(title="Error", message="Intentelo mas tarde, estamos teniendo problemas.")
                entrynombre.delete(0, END)
                entrypass.delete(0, END)  
                print("Error en: ", error)
    ######################################


    #Botones de la ventana de LOGIN
    btn_recuperar_pass=Button(frame_login, command=btnclick ,text="Crear una cuenta", bd=0, bg="white", cursor="hand2", fg="gray", activebackground="white", activeforeground="gray")  #Botón para recuperar contraseña
    btn_recuperar_pass.place(x=175, y=310)

    btn_ingresar=Button(frame_login, command=btnlogin , text="Ingresar",font=("Arial", 11) ,cursor="hand2",bg="green", fg="white", activeforeground="white", activebackground="green")
    btn_ingresar.place(x=175, y=350, width=120, height=30)

    #Loop para que no se cierre una vez ejecutada
    ventana.mainloop() 
ventanaUno()