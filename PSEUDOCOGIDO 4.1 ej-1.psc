Algoritmo promedio_notas
	Definir promedionotas Como Real
	Definir suma_notas Como Real
	Escribir 'ingresar nota de la materia 1'
	Leer nota_materia1
	Escribir 'ingresar nota de la materia 2'
	Leer nota_materia2
	Escribir 'ingresar nota de la materia 3'
	Leer nota_materia3
	Escribir 'ingresar nota de la materia 4'
	Leer nota_materia4
	Escribir 'ingresar nota de la materia 5'
	Leer nota_materia5
	suma_notas <- nota_materia1+nota_materia2+nota_materia3+nota_materia4+nota_materia5
	Escribir 'La suma total de notas es: ', suma_notas
	promedionotas <- suma_notas/5
	Escribir ' el promedio de las notas es: ', promedionotas
FinAlgoritmo
