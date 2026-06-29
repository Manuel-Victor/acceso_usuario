def inicio_usuario():
    print("bienvenido al programa")
    name = input("ingresa tu nombre: ").strip()
    access = False
    counter = 0
    age = 0 
    while counter < 3:
        try: 
            age = int(input("ingresa tu edad: "))
            if age > 0 and age < 100:
                if age >= 18:
                    print (f"bievenido {name}")
                    access = True 
                    break
                else:
                    print (f"{name} no tienes la edad permititda")
                    access = False
                    break
            else:
                print("no es un rango de edad valido")
                counter += 1
        except ValueError:
            print("Solo puedes ingresar numeros para registrar tu edad")
            counter += 1
        if counter == 3:
            print("Intentos maximos permitidos")
    return access, name, age, counter


acceso_permitido, nombre_usuario, edad, numero_intentos = inicio_usuario()

print (acceso_permitido)
print (nombre_usuario)
print(edad)
print(numero_intentos)


                