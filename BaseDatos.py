import sqlite3

def conectar():
    conexion = sqlite3.connect("agenda.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTabla():
    conexion, cursor = conectar()
    sql = """
        CREATE TABLE IF NOT EXISTS agenda(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(20) NOT NULL,
            telefono VARCHAR (14) NOT NULL,
            direccion VARCHAR (20) NOT NULL,
            correo VARCHAR (20) NOT NULL,
            categoria VARCHAR(10) NOT NULL,
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuario(usuario)
        )
    """
    if(cursor.execute(sql)):
        print("Tabla creada")
    else:
        print("No se pudo crear la tabla")
    conexion.close()


def Agregar(datos):
    conexion, cursor = conectar()
    sql = """
    INSERT INTO agenda (nombre, apellido, telefono, direccion, correo, categoria, usuario_id) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(sql, datos)
        conexion.commit()
        print("Datos guardados")
    except sqlite3.Error as e:
        print("Error al insertar datos:", e)
    finally:
        conexion.close()



def Mostrar(usuario_id):
    conexion, cursor = conectar()
    sql = "SELECT id,nombre,apellido,telefono,direccion,correo,categoria FROM agenda WHERE usuario_id = ?"
    cursor.execute(sql, (usuario_id,))
    listado = []
    for fila in cursor:
        listado.append(fila)
    listado.sort()
    conexion.close()
    return listado

def BuscarContactos(id, usuario_id):
    conexion, cursor = conectar()
    sql = "SELECT id, nombre, apellido, telefono, direccion, correo, categoria FROM agenda WHERE id = ? AND usuario_id = ?"
    cursor.execute(sql, (id, usuario_id))
    contacto = cursor.fetchall()
    conexion.close()
    return contacto

def Editar(id, nombre, apellido, telefono, direccion, correo, categoria, usuario_id):
    conexion, cursor = conectar()
    sql = "UPDATE agenda SET nombre=?, apellido=?, telefono=?, direccion=?, correo=?, categoria=? WHERE id=? AND usuario_id=?"
    cursor.execute(sql, (nombre, apellido, telefono, direccion, correo, categoria, id, usuario_id))
    conexion.commit()
    conexion.close()

def Borrar(id, usuario_id):
    conexion, cursor = conectar()
    sql = "DELETE FROM agenda WHERE id=? AND usuario_id=?"
    cursor.execute(sql, (id, usuario_id))
    conexion.commit()
    conexion.close()

def BuscarCategoria(categoria, usuario_id):
    conexion, cursor = conectar()
    sql = "SELECT id, nombre, apellido, telefono, direccion, correo, categoria FROM agenda WHERE categoria = ? AND usuario_id = ?"
    cursor.execute(sql, (categoria, usuario_id))
    contacto = cursor.fetchall()
    conexion.close()
    return contacto

# -------------------------CRUD DE REGISTRO-------------------------------------------

def conectarUsuario():
    conexion = sqlite3.connect("usuario.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTablaUsuario():
    conexion, cursor = conectarUsuario()
    sql = """
        CREATE TABLE IF NOT EXISTS usuario(
            cedula INTEGER PRIMARY KEY NOT NULL,
            nombre TEXT NOT NULL,
            apellido TEXT NOT NULL,
            telefono TEXT NOT NULL,
            usuario TEXT NOT NULL,
            contrasenia TEXT NOT NULL
        )
    """
    try:
        cursor.execute(sql)
        conexion.commit()
        print("Tabla 'usuario' creada correctamente")
    except Exception as e:
        print("Error al crear la tabla 'usuario':", e)
    finally:
        conexion.close()

def agregarUsuario(datos):
    conexion, cursor = conectarUsuario()
    sql = "INSERT INTO usuario (cedula, nombre, apellido, telefono, usuario, contrasenia) VALUES (?,?,?,?,?,?)"
    try:
        cursor.execute(sql, datos)
        conexion.commit()
        print("Datos de usuario guardados correctamente")
    except:
        print("Error al guardar los datos del usuario:")
    finally:
        conexion.close()

def mostrarUsuario():
    conexion, cursor = conectarUsuario()
    sql = "SELECT * FROM usuario"
    try:
        cursor.execute(sql)
        listado = cursor.fetchall()
        print("Listado de usuarios:")
        for usuario in listado:
            print(usuario)
        return listado
    except:
        print("Error al mostrar los usuarios:")
    finally:
        conexion.close()

def buscarUsuarioPorCedula(cedula):
    conexion, cursor = conectarUsuario()
    sql = "SELECT * FROM usuario WHERE cedula = ?"
    try:
        cursor.execute(sql, (cedula,))
        usuario = cursor.fetchone()
        return usuario
    except:
        print("Error al buscar usuario por cedula:")
    finally:
        conexion.close()

def editarUsuario(cedula, nombre, apellido, telefono, usuario, contrasenia):
    conexion, cursor = conectarUsuario()
    sql = "UPDATE usuario SET nombre=?, apellido=?, telefono=?, usuario=?, contrasenia=? WHERE cedula=?"
    try:
        cursor.execute(sql, (nombre, apellido, telefono, usuario, contrasenia, cedula))
        conexion.commit()
        print("Usuario modificado correctamente")
    except:
        print("Error al modificar usuario:")
    finally:
        conexion.close()

def borrarUsuario(cedula):
    conexion, cursor = conectarUsuario()
    sql = "DELETE FROM usuario WHERE cedula = ?"
    cursor.execute(sql, (cedula,))
    cursor.close()
    conexion.commit()
    conexion.close()

# -------------------------FAVORITO-------------------------------------------
def conectarFavorito():
    conexion = sqlite3.connect("favorito.db")
    cursor = conexion.cursor()
    return conexion, cursor

def crearTablaFavorito():
    conexion, cursor = conectarFavorito()
    sql = """
        CREATE TABLE IF NOT EXISTS favorito(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre VARCHAR(20) NOT NULL,
            apellido VARCHAR(20) NOT NULL,
            telefono VARCHAR(14) NOT NULL,
            direccion VARCHAR(50) NOT NULL,
            correo VARCHAR(50) NOT NULL,
            categoria VARCHAR(10) NOT NULL,
            usuario_id INTEGER NOT NULL,
            FOREIGN KEY(usuario_id) REFERENCES usuario(usuario_id)
        )
    """
    try:
        cursor.execute(sql)
        conexion.commit()
        print("Tabla 'favorito' creada correctamente")
    except Exception as e:
        print("Error al crear la tabla 'favorito':", e)
    finally:
        conexion.close()

def AgregarFavorito(datos):
    conexion, cursor = conectarFavorito()
    sql = """
    INSERT INTO favorito (nombre, apellido, telefono, direccion, correo, categoria, usuario_id) VALUES (?, ?, ?, ?, ?, ?, ?)
    """
    try:
        cursor.execute(sql, datos)
        conexion.commit()
        print("Favorito guardado")
    except sqlite3.Error as e:
        print("Error al insertar datos:", e)
    finally:
        conexion.close()

def MostrarFavorito(usuario_id):
    conexion, cursor = conectarFavorito()
    sql = "SELECT id,nombre,apellido,telefono,direccion,correo,categoria FROM favorito WHERE usuario_id = ?"
    cursor.execute(sql, (usuario_id,))
    listado = []
    for fila in cursor:
        listado.append(fila)
    listado.sort()
    conexion.close()
    return listado

def BorrarFavorito(id,usuario_id):
    conexion, cursor = conectarFavorito()
    sql = "DELETE FROM favorito WHERE id=? AND usuario_id=?"
    cursor.execute(sql, (id, usuario_id))
    conexion.commit()
    conexion.close()
# -------------------------LOGIN-------------------------------------------
def loginUsuarioContrasenia(usuario, contrasenia):
    conexion, cursor = conectarUsuario()
    sql = "SELECT * FROM usuario WHERE usuario = ? AND contrasenia = ?"
    cursor.execute(sql, (usuario, contrasenia))
    contacto = cursor.fetchall()
    conexion.close()
    return contacto