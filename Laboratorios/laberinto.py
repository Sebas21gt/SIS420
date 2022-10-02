import random

def hay_espacio(laberinto, n_fila, n_columna):
    n_espacios = 0
    if n_fila > 0 and laberinto[n_fila - 1][n_columna - 1] == " ":
        n_espacios += 1
    elif n_fila < len(laberinto) and laberinto[n_fila + 1][n_columna] == " ":
        n_espacios += 1
    elif n_columna < len(laberinto) and laberinto[n_fila][n_columna - 1] == " ":
        n_espacios += 1
    elif n_fila < len(laberinto[0][:]) and laberinto[n_fila][n_columna + 1] == " ":
        n_espacios += 1

    if n_espacios > 0:
        return True

n_filas = int(input("Ingrese el numero de filas: "))
n_columnas = int(input("Ingrese el numero de columnas: "))

n_paredes = int(input("Ingrese el numero de paredes: "))
n_espacios = (n_filas * n_columnas) - n_paredes

laberinto = []

for i in range(0, n_filas):
    fila = []
    for j in range(0, n_columnas):
        #hay_espacio(laberinto, n_filas, n_columnas)
        if random.randrange(2) == 1:
            fila.append("#")
        else:
            fila.append(" ")

    laberinto.append(fila)
for fila in laberinto:
    print(fila)