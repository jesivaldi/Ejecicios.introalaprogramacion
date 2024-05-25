#Pedir al usuario que ingrese 10 nombres de personas (input en un ciclo) no repetidas, guardarlos en una lista y mostrarlos. 

lista =[]
nombre = input("ingrese el nombre: ")

while len(lista) < 10:
    if nombre not in lista:
        lista.append(nombre)
    nombre = input("ingrese el nombre: ")

print(lista)
