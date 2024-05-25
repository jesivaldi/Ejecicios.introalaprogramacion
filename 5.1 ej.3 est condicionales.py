
#Desarrollar un programa en python en el que una impresora solo imprime un minimo de 50 hojas y un mayor de 300 hojas en caso contrario 
#no se puede imprimir el libro

Total_hojas = int(input("Ingresar el total de hojas a imprimir: "))


if Total_hojas >= 50 and Total_hojas <= 300:
    print("Su libro se está imprimiendo correctamente")
else:
    print("Disculpe, no es posible imprimir el libro")
