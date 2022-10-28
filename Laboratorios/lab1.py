import random

n_filas = int(input("Introducir cantidad de filas: "))
n_columnas = int(input("Introducir cantidad de columnas: "))
n_paredes = int(input("Introducir cantidad de paredes: "))
n_espacios = int((n_filas * n_columnas) - n_paredes)

#print(n_filas, n_columnas, n_paredes, n_espacios)
def crear_mapa_laberinto(n_filas, n_columnas, n_paredes, n_espacios):
    mapa_laberinto = []
    n_paredes_generadas = 0

    for fila in range (0, n_filas - 1):
        fila_laberinto = []
        for columna in range(0, n_columnas):
            if random.randrange(2) == 1 and n_paredes_generadas < n_paredes:
                fila_laberinto.append("#")
                n_paredes_generadas += 1
            else:
                fila_laberinto.append(" ")

    mapa_laberinto.append(fila_laberinto)
    return mapa_laberinto

laberinto = crear_mapa_laberinto(n_filas, n_columnas, n_paredes, n_espacios)

for fila_laberinto in laberinto:
    print(fila_laberinto)