import sqlite3

def inicializar_base_de_datos(): #permite crear la base de datos 
    conexion = sqlite3.connect("control_acceso.db")
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS usuario_acceso (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   nombre TEXT NOT NULL,
                   edad INTEGER NOT NULL,
                   acceso_consedido INTERGER NOT NULL
                   )
    """)
    conexion.commit()
    conexion.close()
    print ("base de datos e infraestructura lista")



def inicio_usuario(): #Esta funcion permite que ingrese el nombre, y la edad de los usuarios
    #declaramos las funciones fuera del bucle while para poder acceder a todas las varibales
    print("bienvenido al programa")
    name = input("ingresa tu nombre: ").strip()
    access = False
    counter = 0 #esta variable permitira controlar el bucle while
    age = 0 
    while counter < 3:
    #Permite que se si el usuiro ingresa mal la edad pueda volver a intentarlo
        try: 
            age = int(input("ingresa tu edad: "))
            if age > 0 and age < 100:
            #limitamos a que la edad permitida sea solo de 0 a 100
                if age >= 18:
                    print (f"bievenido {name}")
                    access = True 
                    break
                else:
                    print (f"{name} no tienes la edad permititda")
                    access = False
                    break
            else:
             #si age esta fuera del rando de edad el counter comenzara
                print("no es un rango de edad valido")
                counter += 1
        except ValueError: 
            #en caso de que el usuario ingrese letras en edad, esta parte permite que no se rompa el codigo
            print("Solo puedes ingresar numeros para registrar tu edad")
            counter += 1
        if counter == 3:
            #en caso de intentos maximos permitidos permite enviar el mensaje el mensaje que los intentos se han terminado 
            print("Intentos maximos permitidos")
    return name, age, access, counter

def registrar_usuarios (name, age, access): #permite agragar datos a las tablas
    conexion =sqlite3.connect("control_acceso.db")
    cursor = conexion.cursor()
    acceso_entero = 1 if access == True else 0
    cursor.execute("""
        INSERT INTO usuario_acceso (nombre, edad, acceso_consedido)
        VALUES (?, ?, ?) 
    """, (name, age, acceso_entero)
                   )
    conexion.commit()
    conexion.close()
    print("resgistro guardado")


if __name__ == "__main__":
    inicializar_base_de_datos()
    name, age, access, counter = inicio_usuario()
    registrar_usuarios(name, age, access)