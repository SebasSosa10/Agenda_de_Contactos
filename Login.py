from tkinter import *
from tkinter import messagebox
from BaseDatos import *
import Agenda
import Registro

def pasarAgenda(id_Usuario):
    ventana.withdraw()
    Agenda.mostrarVentanaAgenda(id_Usuario)
    
def pasarRegistro():
    ventana.withdraw()
    Registro.mostrarRegistro()

def mostrarLogin():
    global ventana
    global frame
    global colorLetra
    global PROPORCION_TABLA
    global etiquetaContrasenia
    global etiquetaUsuario
    global cajaContrasenia
    global cajaUsuario
    global botonIniciar
    global botonRegistrar
    
    ANCHO = 300
    ALTO = 300
    colorVentana = "light blue"
    colorLetra = "white"
    PROPORCION_TABLA = 0.7 
    
    ventana = Tk()
    ventana.config(bg=colorVentana)
    ventana.title("Inicio sesión")
    
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    
    x = (screen_width - ANCHO) // 2
    y = (screen_height - ALTO) // 2
    
    ventana.geometry(f"{ANCHO}x{ALTO}+{x}+{y}")
    
    frame = Frame(ventana, width=ANCHO, height=ALTO, bg=colorVentana)
    frame.pack()
    
    def mostrarMensaje (titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
        
    def buscarUsuarioContrasenia():
        global Usuario
        global Contrasenia
        usuario = cajaUsuario.get()
        contrasenia = cajaContrasenia.get()
        if usuario == "" or contrasenia == "":
            mostrarMensaje("Error", "Debes insertar un Usuario y Contraseña válida")
        else:
            contacto = loginUsuarioContrasenia(usuario, contrasenia)
            if contacto:
                pasarAgenda(usuario)
            else:
                mostrarMensaje("Error", "No está registrado")
    

    
    # Widgets
    etiquetaUsuario = Label (frame, text="Usuario: ",bg = "light blue")
    etiquetaUsuario.place(x=60, y=100)
    cajaUsuario = Entry (frame)
    cajaUsuario.place(x=130, y=100)
    etiquetaContrasenia = Label (frame, text="Contraseña: ",bg = "light blue")
    etiquetaContrasenia.place(x=40, y=140)
    cajaContrasenia = Entry (frame)
    cajaContrasenia.place(x=130, y=140)
    botonIniciar = Button(frame, text="Iniciar sesión",fg="Black" ,bg = "white",width=10,height=2,command=buscarUsuarioContrasenia)
    botonIniciar.place(x=60, y=200)
    botonRegistrar = Button(frame, text="Registrarse",fg="Black" ,bg = "white",width=10,height=2, command=pasarRegistro)
    botonRegistrar.place(x=170, y=200)
    
    ventana.mainloop()
