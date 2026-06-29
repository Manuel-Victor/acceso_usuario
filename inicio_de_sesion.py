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
    return access, name, age, counter

"""
Las siguientes variables permiten corroborar que se esten ejecutando de 
manera correcta las varibales   
"""
acceso_permitido, nombre_usuario, edad, numero_intentos = inicio_usuario()

print (f"acceso: {acceso_permitido}")
print (f"nombre del usuario: {nombre_usuario}")
print(f"edad del usuaio: {edad}")
print(f"intento realizados: {numero_intentos}")


