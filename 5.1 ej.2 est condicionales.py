#Desarrollar un programa en python em el que puede ver una pelicula si la persona es mayor de 18 años, 
#en caso de que sea mayor se imprime un cartel que diga "que disfrute la pelicula" 
#en caso de que no es mayor que imprima un carte que diga "no esta autorizado a ver la peiicula"

Edad = int(input("ingresar tu edad: "))
mayor_edad = 18

if Edad <= mayor_edad:

    print ("No estas autorizado a ver la pelicula")
else:
    print ("Que disfrutes la pelicula!!")
