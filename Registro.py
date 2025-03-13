from tkinter import *
from tkinter import messagebox
from BaseDatos import *
import Login

def regresarLogin():
    ventana.withdraw()
    Login.mostrarLogin()

def mostrarRegistro():
    global ventana
    global frame
    global colorLetra
    global PROPORCION_TABLA
    global etiquetaApellido
    global etiquetaCedula
    global etiquetaContrasenia
    global etiquetaNombre
    global etiquetaTelefono
    global etiquetaUsuario
    global cajaApellido
    global cajaCedula
    global cajaContrasenia
    global cajaTelefono
    global cajaNombre
    global cajaUsuario
    ANCHO = 500
    ALTO = 400
    colorVentana = "light blue"
    colorLetra = "white"
    PROPORCION_TABLA = 0.7 
    
    ventana = Tk()
    ventana.config(bg=colorVentana)
    ventana.title("Registrar Nuevos Usuarios")
    
    screen_width = ventana.winfo_screenwidth()
    screen_height = ventana.winfo_screenheight()
    
    x = (screen_width - ANCHO) // 2
    y = (screen_height - ALTO) // 2
    
    ventana.geometry(f"{ANCHO}x{ALTO}+{x}+{y}")
    
    frame = Frame(ventana, width=ANCHO, height=ALTO, bg=colorVentana)
    frame.pack()
    
    def mostrarMensaje(titulo, mensaje):
        messagebox.showinfo(titulo, mensaje)
    
    def limpiarCampos():
        cajaCedula.delete(0, END)
        cajaNombre.delete(0, END)
        cajaApellido.delete(0, END)
        cajaTelefono.delete(0, END)
        cajaUsuario.delete(0, END)
        cajaContrasenia.delete(0, END)
    
    def guardarUsuario():
        crearTablaUsuario()
        
        if ((cajaCedula.get() == "") or (cajaNombre.get() == "") or (cajaApellido.get() == "") or (cajaTelefono.get() == "") or (cajaUsuario.get() == "") or (cajaContrasenia.get() == "")): 
            mostrarMensaje("Error", "Debes llenar los campos")
        else:
            datos = (cajaCedula.get(), cajaNombre.get(), cajaApellido.get(), cajaTelefono.get(), cajaUsuario.get(), cajaContrasenia.get())
            agregarUsuario(datos)
            limpiarCampos()
            mostrarUsuario()
    
    def modificarUsuario():
        crearTablaUsuario()
        if((cajaNombre.get() == "") or (cajaApellido.get() == "") or (cajaTelefono.get() == "") or (cajaUsuario.get() == "") or (cajaContrasenia.get() == "")):
            mostrarMensaje("Error", "Debes llenar todos los campos")
        else:
            try:
                editarUsuario(cajaCedula.get(), cajaNombre.get(), cajaApellido.get(), cajaTelefono.get(), cajaUsuario.get(), cajaContrasenia.get())
                mostrarMensaje("Editar", "Usuario modificado")
                limpiarCampos()
                mostrarUsuario()
            except:
                mostrarMensaje("Error", "El usuario no puede ser modificado")
    
    def eliminarUsuario():
        if cajaCedula.get() == "":
            mostrarMensaje("Error", "Debes insertar una Cedula válida")
        else:
            try:
                cedula = cajaCedula.get() 
                borrarUsuario(cedula)
                mostrarMensaje("Borrar", "Contacto eliminado")
                limpiarCampos()
                mostrarUsuario()
            except Exception as e:
                print(e)

    
    def buscarUsuario():
        if cajaCedula.get() == "":
            mostrarMensaje("Error", "Debes insertar una Cedula válida")
        else:
            usuario = buscarUsuarioPorCedula(cajaCedula.get())
            if usuario:
                MostrarUsuarioCedula(cajaCedula.get())
            else:
                mostrarMensaje("Error", "No se encontró ningún Usuario con esa Cedula")
    
    def MostrarUsuarioCedula(cedula):
        usuario = buscarUsuarioPorCedula(cedula)
        if usuario:
            cajaCedula.delete(0, END)
            cajaCedula.insert(0, usuario[0])
            cajaNombre.delete(0, END)
            cajaNombre.insert(0, usuario[1])
            cajaApellido.delete(0, END)
            cajaApellido.insert(0, usuario[2])
            cajaTelefono.delete(0, END)
            cajaTelefono.insert(0, usuario[3])
            cajaUsuario.delete(0, END)
            cajaUsuario.insert(0, usuario[4])
            cajaContrasenia.delete(0, END)
            cajaContrasenia.insert(0, usuario[5])
    
    # Widgets
    etiquetaCedula = Label(frame, text="Cedula:",bg = "light blue")
    etiquetaCedula.place(x=150, y=10)
    cajaCedula = Entry(frame)
    cajaCedula.place(x=220, y=10)
    etiquetaNombre = Label(frame, text="Nombre:",bg = "light blue")
    etiquetaNombre.place(x=150, y=50)
    cajaNombre = Entry(frame)
    cajaNombre.place(x=220, y=50)
    etiquetaApellido = Label(frame, text="Apellido:",bg = "light blue")
    etiquetaApellido.place(x=150, y=90)
    cajaApellido = Entry(frame)
    cajaApellido.place(x=220, y=90)
    etiquetaTelefono = Label(frame, text="Telefono:",bg = "light blue")
    etiquetaTelefono.place(x=150, y=130)
    cajaTelefono = Entry(frame)
    cajaTelefono.place(x=220, y=130)
    etiquetaUsuario = Label(frame, text="Usuario:",bg = "light blue")
    etiquetaUsuario.place(x=150, y=170)
    cajaUsuario = Entry(frame)
    cajaUsuario.place(x=220, y=170)
    etiquetaContrasenia = Label(frame, text="Contraseña:",bg = "light blue")
    etiquetaContrasenia.place(x=150, y=210)
    cajaContrasenia = Entry(frame)
    cajaContrasenia.place(x=220, y=210)
    botonRegresar = Button(frame, text="Atras",fg="Black" ,bg = "white",width=10,height=2, command=regresarLogin)
    botonRegresar.place(x=210, y=350)
    botonAgregar = Button(frame, text="Agregar",fg="Black" ,bg = "white", command=guardarUsuario)
    botonAgregar.place(x=115, y=280)
    botonBorrar = Button(frame, text="Borrar",fg="Black" ,bg = "white", command=eliminarUsuario)
    botonBorrar.place(x=315, y=280)
    botonEditar = Button(frame, text="Editar",fg="Black" ,bg = "white", command=modificarUsuario)
    botonEditar.place(x=250, y=280)
    botonBuscar = Button(frame, text="Buscar",fg="Black" ,bg = "white", command=buscarUsuario)
    botonBuscar.place(x=180, y=280)
    ventana.mainloop
