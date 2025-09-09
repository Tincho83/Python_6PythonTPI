# -*- coding: utf-8 -*-
"""
TP I de Python para CoderHouse, creado 09/09/2025 09:21:32

@author: Martin Hernandez


"""

# Base de datos Diccionario (En memoria durante la ejecucion. No Persistente)
credenciales_db = {}

# Funcion para Registro de Usuario.
def registrar_usuario(db_usuario):
    """Registra un nuevo usuario en el diccionario."""
    
    while True:
        #Ingreso de Nombre de Usuario. ELiminamos los espacios en blanco al inicio y final del texto ingresado.
        usuario = input("Ingrese Nombre de Usuario: ").strip()

        # Comprobar longitud de usuario ingresado
        tamano_usuario = len(usuario)

        # Si usuario ingresado es vacio volvemos al inicio del bucle, para que ingrese los datos correctamentr
        if not usuario:  
            print(">Error: El nombre de usuario no puede estar vacio.\n")
            continue

        # Validamos que el usuario ingresdo no supere los 25 carcteres si no volvemos al inicio del bucle, para que ingrese los datos correctamentr
        if tamano_usuario > 25:
            print(">Error: Debe ingresar un Nombre de Usuario de hasta 25 caracteres.\n")
            continue
        else:
            # Validamos que si el usuario ingresdo ya existe en la DB, volvemos al inicio del bucle, para que ingrese otros datos correctamentr
            if usuario in db_usuario:
                print(">Error: No es posible el registro. El usuario ya existe.\n")
                continue
    
            #Ingreso de Contraseña. ELiminamos los espacios en blanco al inicio y final del texto ingresado.
            contrasena = input("Ingrese contraseña: ").strip()

            # Comprobar longitud de contraseña
            tamano_contrasena = len(contrasena)

            # Si contrasena es vacio volvemos al inicio del bucle, para que ingrese los datos correctamentr
            if not contrasena:
                print(">Error: La contraseña no puede estar vacía.\n")
                continue

            # Validamos que el contraseña ingresada no supere los 25 caracteres si no  volvemos al inicio del bucle, para que ingrese los datos correctamentr
            if tamano_contrasena > 25:
                print(">Error: La contraseña debe tener entre 1 y 25 caracteres.\n")
                continue

            # Guardar usuario y contraseña
            db_usuario[usuario] = contrasena
            # Notificamos por pantalla
            print(f"*** El Usuario '{usuario}' se registro correctamente.\n\n")
        
        #Salimos del bucle while
        break


# Funcion para Listar Usuarios.
def listar_usuarios(db_usuario):
    """Muestra solo los usuarios registrados."""

    #Comprobamos si existe al menos un usuario registrado en la BD
    if not db_usuario:
        print("No existen usuarios registrados en la base de datos.\n")
    else:
        # Imprimir multi linea
        print("""Listado de usuarios registrados:
┌─────────────────────────────┐
│    Nombre/s de Usuario/s    │
├─────────────────────────────┤""")
        
        # Recorremos los usuarios en la BD
        for usuario in db_usuario:
            
            # Realizamos calculos para armar el cierre de fila de la tabla
            tamano_usuario = len(usuario)
            espacios_linea_columna_usuario_tabla = 31 - 3 - tamano_usuario
            cadena_espacios_linea_columna_usuario_tabla = " " * espacios_linea_columna_usuario_tabla
            
            print(f"│ {usuario}{cadena_espacios_linea_columna_usuario_tabla}│")
            print("└─────────────────────────────┘\n\n")


# Funcion para listar Usuarios con contraseña (Solo modo prueba)
def listar_usuarios_contrasenas(db_usuario):
    """Muestra usuarios registrados con sus contraseñas."""
    
    #Comprobamos si existe al menos un usuario registrado en la BD
    if not db_usuario:
        print("No existen usuarios registrados en la base de datos.\n")
    else:
         # Imprimir multi linea
        print("""Listado de usuarios registrados:
┌─────────────────────────────┬──────────────────────────┐
│    Nombre/s de Usuario/s    │       Contraseña/s       │
├─────────────────────────────┼──────────────────────────┤""")

        # Recorremos los usuarios en la BD
        for usuario, contrasena in db_usuario.items():

             # Realizamos calculos para armar el cierre de fila de la tabla
            tamano_usuario = len(usuario)            
            espacios_linea_columna_usuario_tabla = 31 - 3 - tamano_usuario
            cadena_espacios_linea_columna_usuario_tabla = " " * espacios_linea_columna_usuario_tabla

            tamano_contrasena = len(contrasena)
            espacios_linea_columna_contrasena_tabla = 31 - 6 - tamano_contrasena
            cadena_espacios_linea_columna_contrasena_tabla = " " * espacios_linea_columna_contrasena_tabla
            
            print(f"│ {usuario}{cadena_espacios_linea_columna_usuario_tabla}│ {contrasena}{cadena_espacios_linea_columna_contrasena_tabla}│")
            print("└─────────────────────────────┴──────────────────────────┘\n\n")


def inicio_sesion(db_usuario):
    """Inicio de sesion de usuario y contraseña. Hasta 3 intentos"""
    
    #Comprobamos si existe al menos un usuario registrado en la BD
    if not db_usuario:
        print("No existen usuarios registrados en la base de datos.\n")
        return
    else:
        
        intentos_iniciosesion = 0
        usuario_sesioniniciada = False
        while intentos_iniciosesion < 3:
            usuario = input("Ingrese nombre de usuario: ").strip()
            contrasena = input("Ingrese contraseña: ").strip()

            #Comprobar si el usuario y la contraseña coinciden.
            if usuario in db_usuario and db_usuario[usuario] == contrasena:
                usuario_sesioniniciada = True                
                print(f"Bienvenido, {usuario}!\n\n")
                break
            else:
                intentos_iniciosesion += 1
                print("Usuario o contraseña incorrectos. Intente nuevamente.\n")

        if usuario_sesioniniciada == False:
            # 3 intentos incorrectos de inicio de sesion se termina el programa
            print(f"Demasiados intentos incorrectos de Inicio de sesion. Intentos fallidos: {intentos_iniciosesion}.\n")



#Informacion del TP I
print(__doc__)

# Llamada a la funcion para Registro de Usuario.
registrar_usuario(credenciales_db)

# Llamada a la funcion para listar Usuario/s.
listar_usuarios(credenciales_db)

# Llamada a la funcion para listar Usuario/s y contraseñas (Solo prueba).
listar_usuarios_contrasenas(credenciales_db)

# Llamada a la funcion para Iniciar sesion de Usuario.
inicio_sesion(credenciales_db)



#Recursos:
# https://www.asciitable.com/
# ASCII: ┌ ┘─ ├ ┬ ┴ └ ┐ ┤ │ ┼

#TP I
#Consignas:
#[x] Para tu primera entrega, crear un programa que permita emular el registro y almacenamiento de usuarios en una BBDD. 
#   Hazlo utilizando el concepto de funciones, diccionarios, bucles y condicionales.
#
#Objetivos:
#[x] Practicar el concepto de funciones.
#[x] Desarrollar la parte lógica para el registro de usuarios.
#
#Requisitos:
#[x] Diccionarios (guardado de datos)
#[x] Input (solicitud de datos)
#[x] Variables
#[x] If (chequeo de datos)
#[x] While (iteración para el programa, sea para agregar, loguear o mostrar)
#[x] For (recorrer datos y para búsqueda)
#[x] Print
#[x] Funciones separadas para registro, almacenamiento y muestra
#
#Recomendaciones:
#[x] El formato de registro es: Nombre de usuario y Contraseña.
#[x] Utilizar una función para almacenar la información y otra función para mostrar la información.
#[x] Utilizar un diccionario para almacenar dicha información, con el par usuario-contraseña (clave-valor).
#[x] Utilizar otra función para el login de usuarios, comprobando que la contraseña coincida con el usuario.
#
#Formato:
#[x] El proyecto debe compartirse utilizando Colab bajo el nombre “ArmaTuLogin+Apellido”, por ejemplo “ArmaTuLogin+Fernandez”
#[x] Para guiarte, te compartimos un video explicativo:
#
# https://colab.research.google.com/drive/1N7u5ifNhg5vVSajrBbQMM9-0SsLMIagv?usp=sharing