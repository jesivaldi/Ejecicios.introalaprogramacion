#Eliminar la tercer y la última persona de la lista del ejercicio 1, luego ordenar la lista y mostrarlo

lista =[]
nombre = input("ingrese el nombre: ")

while len(lista) < 10:
    if nombre not in lista:
        lista.append(nombre)
    nombre = input("ingrese el nombre: ")

lista.pop(2)
lista.pop(-1)
lista.sort()

print(lista)