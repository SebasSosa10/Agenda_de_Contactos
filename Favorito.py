from tkinter import *
from tkinter import messagebox
from BaseDatos import *
import Agenda

def regresarAgenda(usuario_id):
    ventana.withdraw()
    Agenda.mostrarVentanaAgenda(usuario_id)

def mostrarVentanaFavorito(usuario_id):
    global ventana
    global frame
    global colorLetra
    global PROPORCION_TABLA
    
    ANCHO = 750
    ALTO = 350
    colorVentana = "light blue"
    colorLetra = "white"
    PROPORCION_TABLA = 0.7 
    
    ventana = Tk()
    ventana.config(bg=colorVentana)
    ventana.title("Agenda Digital")
    
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
        cajaId.delete(0, END)
    
    def eliminarFavorito(usuario_id):
        if cajaId.get() == "":
            mostrarMensaje("Error", "Debes insertar un id")
        else:
            try:
                BorrarFavorito(cajaId.get(), usuario_id)
                mostrarMensaje("Borrar", "favorito eliminado")
                limpiarCampos()
                MostrarFavorito(usuario_id)
            except:
                mostrarMensaje("Error", "Id no encontrado")
    
    def mostrarTablaFavorito(usuario_id):
        listado = MostrarFavorito(usuario_id)
        text.delete('1.0', END)
        text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format("Id", "Nombre", "Apellido", "Telefono", "Direccion", "Correo", "Categoria"))
        for elemento in listado:
            id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto = elemento
            text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format(id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto))

    def regresar(usuario_id):
        regresarAgenda(usuario_id)

    etiquetaId = Label(frame, text="Id: ", bg="light blue")
    etiquetaId.place(x=270, y=10)
    cajaId = Entry(frame)
    cajaId.place(x=310, y=10)   
    text = Text(frame)
    text.place(x=25, y=50, width=700, height=200)
    botonEliminar = Button(frame, text="Eliminar", fg="Black", bg="white",command=lambda: eliminarFavorito(usuario_id))
    botonEliminar.place(x=310, y=255)
    botonBuscar = Button(frame, text="Actualizar", fg="Black", bg="white", command=lambda: mostrarTablaFavorito(usuario_id))
    botonBuscar.place(x=380, y=255)
    botonAtras = Button(frame, text="Atras", fg="Black", bg="white", width=10, height=2, command=lambda: regresar(usuario_id))
    botonAtras.place(x=330, y=290)
    ventana.mainloop()