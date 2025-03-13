from tkinter import *
from tkinter import messagebox
from BaseDatos import *
from tkinter import ttk
import Login
import Favorito

def regresarLogin():
    ventana.withdraw()
    Login.mostrarLogin()

def pasarFavorito(usuario_id):
    ventana.withdraw()
    Favorito.mostrarVentanaFavorito(usuario_id)

def mostrarVentanaAgenda(usuario_id):
    global ventana
    global frame
    global colorLetra
    global PROPORCION_TABLA
    global etiquetaId
    global cajaId
    global etiquetaApellido
    global cajaApellido
    global etiquetaCategoria
    global etiquetaCorreo
    global etiquetaDireccion
    global cajaCorreo
    global cajaDireccion
    global etiquetaNombre
    global cajaNombre
    global etiquetaTelefono
    global cajaTelefono
    global botonActualizar
    global botonAgregar
    global botonBorrar
    global botonActualizar
    global botonFiltrar
    global botonEditar
    global botonBuscar
    global botonFavorito
    global botonVentaFavorito
    ANCHO = 750
    ALTO = 600
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
        cajaNombre.delete(0, END)
        cajaApellido.delete(0, END)
        cajaTelefono.delete(0, END)
        cajaDireccion.delete(0, END)
        cajaCorreo.delete(0, END)
        combo.current(0)
        text.delete('1.0', END)
    
    def Guardar(usuario_id):
        crearTabla()
        if cajaNombre.get() == "" or cajaApellido.get() == "":
            mostrarMensaje("Error", "Debes llenar los campos")
        else:
            categoria_seleccionada = combo.get()
            datos = (cajaNombre.get(), cajaApellido.get(), cajaTelefono.get(), cajaDireccion.get(), cajaCorreo.get(), categoria_seleccionada, usuario_id)
            mostrarMensaje("Guardar", "Contacto guardado")
            Agregar(datos)
            limpiarCampos()
            Mostrar(usuario_id)
    
    def GuardarFavorito(usuario_id):
        crearTablaFavorito()
        if cajaNombre.get() == "" or cajaApellido.get() == "":
            mostrarMensaje("Error", "Debes llenar los campos")
        else:
            categoria_seleccionada = combo.get()
            datos = (cajaNombre.get(), cajaApellido.get(), cajaTelefono.get(), cajaDireccion.get(), cajaCorreo.get(), categoria_seleccionada, usuario_id)
            mostrarMensaje("Guardar", "Favorito guardado")
            AgregarFavorito(datos)
            limpiarCampos()
            MostrarFavorito(usuario_id)

    def Modificar(usuario_id):
        crearTabla()
        if cajaId.get() == "" or cajaNombre.get() == "":
            mostrarMensaje("Error", "Debes llenar los campos")
        else:
            try:
                Editar(cajaId.get(), cajaNombre.get(), cajaApellido.get(), cajaTelefono.get(), cajaDireccion.get(), cajaCorreo.get(), combo.get(), usuario_id)
                mostrarMensaje("Editar", "Contacto modificado")
                limpiarCampos()
                Mostrar(usuario_id)
            except:
                mostrarMensaje("Error", "Id no encontrado")

    def Eliminar(usuario_id):
        if cajaId.get() == "":
            mostrarMensaje("Error", "Debes insertar un nombre")
        else:
            try:
                Borrar(cajaId.get(), usuario_id)
                mostrarMensaje("Borrar", "Contacto eliminado")
                limpiarCampos()
                Mostrar(usuario_id)
            except:
                mostrarMensaje("Error", "Id no encontrado")

    def MostrarTabla(usuario_id):
        listado = Mostrar(usuario_id)
        text.delete('1.0', END)
        text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format("Id", "Nombre", "Apellido", "Telefono", "Direccion", "Correo", "Categoria"))
        for elemento in listado:
            id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto = elemento
            text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format(id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto))

    def Buscar(usuario_id):
        if cajaId.get() == "" or cajaId.get() == 0:
            mostrarMensaje("Error", "Debes insertar un Id válido")
        else:
            contactos = BuscarContactos(cajaId.get(), usuario_id)
            if contactos:
                MostrarTablaConId(cajaId.get(), usuario_id)
            else:
                mostrarMensaje("Error", "No se encontró ningún contacto con ese Id")

    def MostrarTablaConId(id, usuario_id):
        listado = BuscarContactos(id, usuario_id)
        text.delete('1.0', END)
        text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format("Id", "Nombre", "Apellido", "Telefono", "Direccion", "Correo", "Categoria"))
        for contacto in listado:
            id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto = contacto
            text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format(id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto))
            cajaId.delete(0, END)
            cajaId.insert(0, id_contacto)
            cajaNombre.delete(0, END)
            cajaNombre.insert(0, nombre_contacto)
            cajaApellido.delete(0, END)
            cajaApellido.insert(0, apellido_contacto)
            cajaTelefono.delete(0, END)
            cajaTelefono.insert(0, telefono_contacto)
            cajaDireccion.delete(0, END)
            cajaDireccion.insert(0, direccion_contacto)
            cajaCorreo.delete(0, END)
            cajaCorreo.insert(0, correo_contacto)
            combo.set(categoria_contacto)

    def Filtrar(usuario_id):
        if combo.get() == "":
            mostrarMensaje("Error", "Debes seleccionar una categoria")
        else:
            contacto = BuscarCategoria(combo.get(), usuario_id)
            if contacto:
                MostrarTablaConCategoria(combo.get(), usuario_id)
            else:
                mostrarMensaje("Error", "No se encontró ningún contacto en esta categoría")

    def MostrarTablaConCategoria(categoria, usuario_id):
        listado = BuscarCategoria(categoria, usuario_id)
        text.delete('1.0', END)
        text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format("Id", "Nombre", "Apellido", "Telefono", "Direccion", "Correo", "Categoria"))
        for contacto in listado:
            id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto = contacto
            text.insert(INSERT, "{:<2} {:10} {:10} {:14} {:15} {:18} {:18}\n".format(id_contacto, nombre_contacto, apellido_contacto, telefono_contacto, direccion_contacto, correo_contacto, categoria_contacto))

    def pasar(usuario_id):
        pasarFavorito(usuario_id)
    #Widgets
    etiquetaId = Label(frame, text="Id: ", bg="light blue")
    etiquetaId.place(x=270, y=10)
    cajaId = Entry(frame)
    cajaId.place(x=310, y=10)
    etiquetaNombre = Label(frame, text="Nombre: ", bg="light blue")
    etiquetaNombre.place(x=240, y=50)
    cajaNombre = Entry(frame)
    cajaNombre.place(x=310, y=50)
    etiquetaApellido = Label(frame, text="Apellido: ", bg="light blue")
    etiquetaApellido.place(x=240, y=90)
    cajaApellido = Entry(frame)
    cajaApellido.place(x=310, y=90)
    etiquetaTelefono = Label(frame, text="Telefono: ", bg="light blue")
    etiquetaTelefono.place(x=240, y=130)
    cajaTelefono = Entry(frame)
    cajaTelefono.place(x=310, y=130)
    etiquetaDireccion = Label(frame, text="Dirección: ", bg="light blue")
    etiquetaDireccion.place(x=235, y=170)
    cajaDireccion = Entry(frame)
    cajaDireccion.place(x=310, y=170)
    etiquetaCorreo = Label(frame, text="Correo: ", bg="light blue")
    etiquetaCorreo.place(x=250, y=210)
    cajaCorreo = Entry(frame)
    cajaCorreo.place(x=310, y=210)
    etiquetaCategoria = Label(frame, text="Categoria: ", bg="light blue")
    etiquetaCategoria.place(x=234, y=250)
    combo = ttk.Combobox(frame)
    combo.place(x=310, y=250)
    combo['values'] = ('Familia', 'Amigos', 'Trabajo', 'Otros')
    text = Text(frame)
    text.place(x=25, y=290, width=700, height=200)
    botonAgregar = Button(frame, text="Guardar", fg="Black", bg="white", command=lambda: Guardar(usuario_id))
    botonAgregar.place(x=170, y=500)
    botonBorrar = Button(frame, text="Borrar", fg="Black", bg="white", command=lambda: Eliminar(usuario_id))
    botonBorrar.place(x=250, y=500)
    botonActualizar = Button(frame, text="Actualizar", fg="Black", bg="white", command=lambda: MostrarTabla(usuario_id))
    botonActualizar.place(x=330, y=500)
    botonEditar = Button(frame, text="Editar", fg="Black", bg="white",command=lambda: Modificar(usuario_id))
    botonEditar.place(x=435, y=500)
    botonBuscar = Button(frame, text="Buscar", fg="Black", bg="white", command=lambda: Buscar(usuario_id))
    botonBuscar.place(x=510, y=500)
    botonFiltrar = Button(frame, text="Filtrar categoria", fg="Black", bg="white", command=lambda: Filtrar(usuario_id))
    botonFiltrar.place(x=480, y=250)
    botonFavorito = Button(frame, text="Guardar Favorito", fg="Black", bg="white", command=lambda: GuardarFavorito(usuario_id))
    botonFavorito.place(x=580, y=250)
    botonVentaFavorito = Button(frame, text="Favorito", fg="Black", bg="white", command=lambda: pasar(usuario_id))
    botonVentaFavorito.place(x=680, y=10)
    botonAtras = Button(frame, text="Atras", fg="Black", bg="white", width=10, height=2, command=regresarLogin)
    botonAtras.place(x=350, y=550)
    ventana.mainloop()
