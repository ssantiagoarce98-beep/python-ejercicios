def analizar_equipos(jugadores):
    total_goles=0
    for i in range(len(jugadores)):
        print (jugadores[i]["nombre"])
        print (jugadores[i]["equipo"])
        print (jugadores[i]["goles"])
        if jugadores[i]["goles"]>=10:
            print ("Goleador")
            total_goles+=1
        else:
            print ("No es goleador")
    print ("Total de goleadores: ", total_goles)
