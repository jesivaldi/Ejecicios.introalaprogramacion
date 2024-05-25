#Un hincha de fútbol desea conocer la cantidad de puntos que su

#equipo lleva acumulados en el campeonato, para ello recibe cada semana la

#información de la cantidad total de partidos, desde el inicio del campeonato, que

#el equipo ha perdido, ha empatado y ha ganado. Por cada partido empatado

#recibe un punto, por cada partido ganado tres puntos y por los perdidos cero

#puntos.

partidos_perdidos = int(input("Ingresar partidos perdidos: "))
partidos_empatados = int(input("Ingresra partidos empatados: "))
partidos_ganados = int(input("Ingresar partidos ganados: "))

puntos_acumulados = (partidos_perdidos*0) + (partidos_empatados*1) + (partidos_ganados*3)

print("los puntos acumulados hasta el momento son: ",puntos_acumulados)