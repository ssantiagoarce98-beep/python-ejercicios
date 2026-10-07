def analizar_jugadores(jugadores):
        total_goles=0
        total_asistencias=0
        total_goleadores=0
        for i in range(len(jugadores)):
            print ("Jugador: ", jugadores[i]["nombre"])
            print ("Equipo: ", jugadores[i]["equipo"])
            print ("Cantidad de goles:", jugadores[i]["goles"])
            print ("Cantidad de asistencias:", jugadores[i]["asistencias"])
            if jugadores[i]["goles"]>=10:
                print ("Goleador")
                total_goleadores+=1
        for i in range(len(jugadores)):
            total_goles+=jugadores[i]["goles"]
            total_asistencias+=jugadores[i]["asistencias"]
        print("Cantidad total de goles:", total_goles)
        print ("Cantidad total de asistencias:", total_asistencias)
        print("Total de goleadores:", total_goleadores)
