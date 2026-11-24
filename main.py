def conexionBD():
    try:
        con=sqlite3.connect("BaseDatosParcial.db") #LIBRERIA: SQLITE3, METODO: CONNECT
        return con
    except Error:
        print("Error")

def cerrar(con):
    con.close

def crearTablaColecciones(con):
    cursorObj=con.cursor()
    cad='''CREATE TABLE IF NOT EXISTS libros(
            Clasificacion text,
            Titulo text NOT NULL,
            Autor text NOT NULL,
            Genero text NOT NULL,
            FechaPublicacion date NOT NULL,
            Estado text NOT NULL,
            PRIMARY KEY(Clasificacion))
            '''
    cad2='''CREATE TABLE IF NOT EXISTS usuarios(
            Identificacion text,
            Nombre text NOT NULL,
            Apellido text NOT NULL,
            Direccion text NOT NULL,
            Telefono int NOT NULL,
            CorreoElectronico text NOT NULL,
            PRIMARY KEY (Identificacion))
            '''
    cad3='''CREATE TABLE IF NOT EXISTS prestamos(
            IdentificacionPrestamo text,
            IdentificacionUsuario text NOT NULL,
            IdentificacionLibro text NOT NULL,
            FechaInicio text NOT NULL,
            FechaDevolucion text NOT NULL,
            Estado text NOT NULL,
            PRIMARY KEY (IdentificacionPrestamo))
            '''
    cursorObj.execute(cad)
    cursorObj.execute(cad2)
    cursorObj.execute(cad3)
    con.commit()


def insertarLibro(con):
    Clasificacion=input("Clasificacion: ")
    Titulo=input("Titulo: ")
    Autor=input("Autor: ")
    Genero=input("Genero: ")
    FechaPublicacion=input("Fecha de Publicacion: ")
    PreguntaEstado=int(input("¿Cual es el estado del libro? (Introduzca un número) 1. Disponible. 2. Prestado. 3. En mantenimiento"))
    if PreguntaEstado==1:
        Estado="Disponible"
elif: PreguntaEstado==2:
        Estado="Prestado"
elif: PreguntaEstado==3:
        Estado="No disponible"
    cursorObj=con.cursor() #cursorObj es el objeto
    cad="INSERT INTO colecciones VALUES('"+Clasificacion+"','"+Titulo+"','"+Autor+"','"+Genero+"','"+FechaPublicacion+"','"+Estado+"')"
    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    con.commit()

def ActualizarInformacionEstadoLibro(con):
    ClasificacionT=input("Clasificacion: ")
    PreguntaEstadoT=int(input("¿Cual es el estado del libro? (Introduzca un número) 1. Disponible. 2. Prestado. 3. En mantenimiento"))
    if PreguntaEstado==1:
  EstadoT="Disponible"
elif: PreguntaEstado==2:
  EstadoT="Prestado"
elif: PreguntaEstado==3:
  EstadoT="No disponible"
else:
  print(“Respuesta no válida, inserte un número”)
    cursorObj=con.cursor()
    cad="UPDATE libros SET Estado="+EstadoT+" WHERE libros='"+ClasificacionT+"'"
    print("La cadena que se ejecutará sera: ",cad)
    cursorObj.execute(cad)
    con.commit()

def ConsutarDisponibilidadLibro(con):
    ClasificacionT=input("Clasificacion: ")
    cursorObj=con.cursor() #cursorObj es el objeto
    cad="SELECT Estado FROM libros WHERE libros='"+ClasificacionT+"'"
    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
     print("El estado actual del libro es: {filas[0]}")
    #print("El tipo de dato que devuelve el fetchall es",type(filas))

def ConsutarDatosLibro(con):
    ClasificacionT=input("Clasificacion: ")
    cursorObj=con.cursor() #cursorObj es el objeto
    cad="SELECT Titulo, Autor, FechaPublicacion, Edicion, Estado FROM libros WHERE libros='"+ClasificacionT+"'"

    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
    for fila in filas:
        print("La informacion del libro es: Clasificacion: {fila[0]}, Titulo: {fila[1]}, Autor: {fila[2]}, Genero: {fila[3]} Fecha: {fila[4]}, Estado: {fila[5]}")
    #print("El tipo de dato que devuelve el fetchall es",type(filas))

def Libros(con):
	miCon=conexionBD()
	print(“¿Que desearia consultar? 1)  Registrar un nuevo libro. 2) Actualizar informacion del estado de un libro. 3) Consultar los datos de la disponibilidad de un libro. 4) Consultar datos vigentes de un libro.”)
	opcionUsuario=input()
	if opcionUsuario==1:
		insertarLibro(miCon)
	elif opcionUsuario==2:
		ActualizarInformacionEstadoLibro(miCon)
	elif opcionUsuario==3:
		ConsutarDisponibilidadLibro(miCon)
	elif opcionUsuario==4:
		ConsutarDatosLibro(miCon)
	else:
  		print(“Respuesta no válida, inserte un numero”)
		opcionUsuario

def main():
    miCon=conexionBD()


#USUARIOS
def insertarUsuario(con):
    Identificacion=input("Identificacion: ")
    Nombre=input("Nombre: ")
    Apellido=input("Apellido: ")
    Direccion=input("Direccion: ")
    Telefono=input("Telefono: ")
    CorreoElectronico=input(“Correo electronico: “)
    cursorObj=con.cursor() #cursorObj es el objeto
    cad="INSERT INTO colecciones VALUES('"+Identificacion+"','"+Nombre+"','"+Apellido+"','"+Direccion+"','"+Telefono+"','"+CorreoElectronico+"')"
    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    con.commit()

def ActualizarContactoUsuario(con):
    IdentificacionT=input("Identificacion: ")
    PreguntacontactoT=int(input(“¿Cual dato desea actualizar: 1) Telefono 2) Correo Electronico”))
    if PreguntacontactoT==1:
  TelefonoT=input(“Inserte el nuevo numero de telefono: ”)
cursorObj=con.cursor()
cad="UPDATE usuarios SET Telefono="+TelefonoT+"” WHERE usuarios='"+IdentificacionT+"'"
cursorObj.execute(cad)
con.commit()
elif PreguntacontactoT==2:
  CorreoElectronicoT=input(“Inserte el nuevo correo: ”)
cursorObj=con.cursor()
cad="UPDATE usuarios SET CorreoElectronico="+CorreoElectronicoT+"” WHERE usuarios='"+IdentificacionT+"'"
cursorObj.execute(cad)
con.commit()
else:
  print(“Respuesta no válida, inserte un numero”)

def ConsutarDatosUsuario(con):
    IdentificacionT=input("Identificacion: ")
    cursorObj=con.cursor() #cursorObj es el objeto
    cad="SELECT Identificacion, Nombre, Apellido, Direccion, Telefono, CorreoElectronico FROM libros WHERE identificacion='"+IdentificacionT+"'"
    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
    for fila in filas:
        print("La informacion del usuario es: Identificacion: {fila[0]}, Nombre: {fila[1]},Apellido: {fila[2]}, Direccion: {fila[3]} Telefono: {fila[4]}, CorreoElectronico: {fila[5]}")
    #print("El tipo de dato que devuelve el fetchall es",type(filas))

def Usuarios(con):
	miCon=conexionBD()
	print(“¿Que desearia consultar? 1)  Registrar un nuevo usuario. 2) Actualizar informacion de contacto de un usuario. 3) Consultar datos vigentes de un usuario.”)
	opcionUsuario=input()
	if opcionUsuario==1:
		insertarUsuario(miCon)
	elif opcionUsuario==2:
		ActualizarContactoUsuario(miCon)
	elif opcionUsuario==3:
		ConsutarDatosUsuario(miCon)
	else:
  		print(“Respuesta no válida, inserte un numero”)
		opcionUsuario


def insertarPrestamo(con):

    IdentificacionPrestamo=input("Identificacion del Pestamo: ")
    IdentificacionUsuario=input("Identificacion del Usuario: ")
    IdentificacionLibro=input("Identificacion del Libro: ")
    FechaInicio=input("Fecha de Inicio del prestamo: ")
    FechaDevolucion=input("Fecha de Devolucion del prestamo: ")
    Estado=input(“Estado: ”) 
    cursorObj=con.cursor() #cursorObj es el objeto
    cad="INSERT INTO colecciones 

VALUES('"+Clasificacion+"','"+Titulo+"','"+Autor+"','"+Genero+"','"+FechaPublicacion+"','"+Estado+"')"
    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    con.commit()

cursorObj=con.cursor() #cursorObj es el objeto
    cad="SELECT Estado FROM libros WHERE libros='"+ClasificacionT+"'"
    print("La cadena que se ejecutara sera:",cad)
    cursorObj.execute(cad)
    filas=cursorObj.fetchall()
     print("El estado actual del libro es: {filas[0]}")
    esstado=”prestado”
    estado=”en mantenimiento”
    fila=filas[0]
    filas=fila.casefold()
    if filas[0] == 

#try:
#cad1=”SELECT Identificacion FROM prestamos WHERE #prestamos='"+IdentificacionUsuario+"'"
#except Error:


