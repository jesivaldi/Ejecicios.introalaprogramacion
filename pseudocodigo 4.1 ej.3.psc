Algoritmo puntos_acumulados
	Escribir 'Ingresar la cantidad de partidos perdidos: '
	Leer partidos_perdidos
	Escribir 'ingresar la cantidad de partidos empatados: '
	Leer partidos_empatados
	Escribir 'ingresar la cantidad de partidos ganados: '
	Leer partidos_ganados
	puntosacumulados <- (partidos_perdidos*0)+(partidos_empatados*1)+(partidos_ganados*3)
	Escribir ' El total de puntos acumulados es: ', puntosacumulados
FinAlgoritmo
