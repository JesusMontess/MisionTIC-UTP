def generarTablaPosicion(nombre, cantPartidosGanados, cantPartidosPerdidos, 
cantPartidosEmpatados, numGolesFavor, numGolesContra):
    puntosPartidosGanados = cantPartidosGanados * 3
    puntosPartidosEmpates = cantPartidosEmpatados * 1
    puntosPartidosPerdidos = cantPartidosPerdidos * 0
    puntos = (puntosPartidosGanados + puntosPartidosEmpates + puntosPartidosPerdidos)
    diferencia = (numGolesFavor - numGolesContra)
    salida = f"Equipo: {nombre} Puntos: {puntos} Diferencia: {diferencia}"
    return salida
print(generarTablaPosicion("Colombia",1,0,0,1,0))
print(generarTablaPosicion("Brasil",1,0,0,3,0))

