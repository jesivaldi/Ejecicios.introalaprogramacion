# Un pintor de casas debe hacer un presupuesto para un cliente. Lo

#que cobra se calcula de acuerdo a los metros cuadrados que debe pintar. El

#cliente le indica que necesita conocer el costo de mano de obra para pintar una

#pared rectangular de un galpón. El pintor cobra un monto ﬁjo por cada metro

#cuadrado. Puedes hacer un algoritmo para calcular el costo de mano de obra para

#pintar la pared.

lado1 = float(input("ingresar lado 1: "))
lado2 = float(input("ingresar lado 2: "))
precio_m2 = 5000
calculo_m2 = lado1 * lado2

precio_final = calculo_m2 * precio_m2

print( "el costo de la mano de obra de la pared es:$ ", precio_final)
