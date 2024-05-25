#Desarrollar en Python un módulo que gestione una agenda telefónica en un diccionario de Python utilizando los recursos ya vistos (variables, input, print, if, if - else, while, for) que consideren adecuados para cada uno de estos casos:

#Mostrar al usuario un menú de opciones

#Opción 1: Agregar una persona (apellido, nombre, dni, email y número de teléfono). Esta opción debe agregar al diccionario a la persona que el usuario ingrese

#Opción 2: Modificar una persona: dado su dni debe buscar la persona y preguntar si desea cambiar los demás campos de la persona, cambiando los que quiera.

#Opción 3: Eliminar una persona del diccionario. Elimina según el DNI

#Opción 4: Mostrar todos la agenda

#Opción 5: Salir

agenda = {}

while True:
    print("Bienvenido a la agenda de contactos, elija una de las siguientes opciones: ")
    print("1 Agregar una persona")
    print("2 Modificar una persona")
    print("3 Eliminar una persona")
    print("4 Mostrar toda la agenda")
    print("5 Salir")

    opcion = int(input(" Ingrese la opcion elegida: "))

    if opcion == "1":
        apellido = input("Ingrese el Apellido: ")
        nombre = input("Ingrese el Nombre: ")
        dni = input("Ingrese el DNI: ")
        email = input("Ingrese el email: ")
        telefono = input("Ingrese el Numero de telefono: ")

        persona = {
            "apellido": apellido,
            "nombre" : nombre,
            "dni" : dni,
            "email":email,
            "telefono": telefono
        }

        agenda [dni] = persona
        print("Se ha ingresado correctamente")

    elif opcion == "2":
        dni = input("Ingrese el dni de la persona que quiere modificar: ")

        if dni in agenda:
            persona = agenda[dni]

            print("datos de la persona ")
            print (persona)

            opcion_modificar = input("desear guardar los datos ingresados?ingrese s para si y n para no")

            if opcion_modificar.lower() == "s":
                apellido = input("ingrese el nuevo apellido: ")
                nombre = input("ingrese el nuevo nombre: ")
                email = input("ingrese el nuevo email: ")
                telefono = input("ingrese el nuevo telefono ")

                persona["apellido"] = apellido
                persona["nombre"] = nombre
                persona["email"] = email
                persona["telefono"] = telefono

                print("la persona ha sido modificada correctamente")
            else:
                ("la persona no ha podido ser modificada")
        else:
            ("no existe ese dni")
    elif opcion == "3":
        dni = input("Ingrese el dni de la persona que quiere eliminar: ")

        if dni in agenda:
            del agenda[dni]

        else:
            ("no existe ese dni")


