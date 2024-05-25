#Un profesor de matemática necesita generar la tabla de multiplicar de un número entero comprendido entre 1 y 10. Por ejemplo para el 3 debería aparecer como salida:
#3x1=3
#3x2=6
#3x3=9
#…. y así hasta 10

numero = int(input("Ingrese un número entero del 1 al 10: "))

while numero < 1 or numero > 10:
    print("Número inválido. Intente nuevamente.")
    numero = int(input("Ingrese un número entero del 1 al 10: "))
