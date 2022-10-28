import turtle
from math import dist
from numpy import cumsum


class Grafo:
    def __init__(self):
        self.aristas = {}
        self.pesos = {}

    def vecinos(self, id):
        return self.aristas[id]


def costofcamino(camino, Grafo):
    # Returns the cumulated cost of camino
    costos_acumulados = [0]
    for i in range(len(camino) - 1):
        costos_acumulados += [1]
    return cumsum(costos_acumulados)


def draw_square(node_id, color="medium sea green", scale=1,
                correction=345, ts=None, text=None):
    if ts is None:
        ts = turtle.Turtle(shape="square")
    ts.shapesize(0.5, 0.5)
    ts.color(color)
    ts.penup()
    x, y = geo_pos(node_id)
    ts.goto(x * scale, correction - y * scale)
    if text is not None:
        ts.write(str(text), font=("Arial", 20, "normal"))


def drawLaberintoSection(t):
    correction = 345
    scale = 1
    for i in range(1, 51):
        x, y = geo_pos(str(i))
        t.goto(x * scale, correction - y * scale)


def buscar_menor_F(nodos):
    """
    Encuentra el nodo con menos F en oL (cola)
    Esto es equivalente a construir una cola de prioridad
    """
    mF = min(getF(nodos))
    for ni in range(len(nodos)):
        if nodos[ni][1] == mF:
            return nodos.pop(ni)[0]


def getF(nodos):
    """
    Devuelve los costes de la cola F = C + H
    C: costo de la ruta
    H: costo de la heuristica 
    """
    return [i[1] for i in nodos]


def camino_desde_origen(origen, n, padres):
    # Builds shortest camino from search result (padres)
    if origen == n:
        return []
    caminoO = [n]
    i = n
    while True:

        i = padres[i]
        caminoO.insert(0, i)
        if i == origen:
            return caminoO


def aStar(grafo, inicio, objetivo):
    frontera = []
    frontera.append((inicio, 0))
    padres = {}
    costo_hasta_ahora = {}
    padres[inicio] = None
    costo_hasta_ahora[inicio] = 0

    while bool(len(frontera)):
        actual = buscar_menor_F(frontera)
        draw_square(actual)  # Draw search expansion
        if actual == objetivo:
            break
        for sucesor in grafo.vecinos(actual):
            costo_nuevo = costo_hasta_ahora[actual] + 1
            if sucesor not in costo_hasta_ahora or costo_nuevo < costo_hasta_ahora[sucesor]:
                costo_hasta_ahora[sucesor] = costo_nuevo
                prioridad = costo_nuevo + heuristic(sucesor)
                frontera.append((sucesor, prioridad))
                padres[sucesor] = actual
        print(frontera)
    return padres

#function greedy algoritmo
def greedy(grafo, inicio, objetivo):
    frontera = []
    frontera.append((inicio, 0))
    padres = {}
    costo_hasta_ahora = {}
    padres[inicio] = None
    costo_hasta_ahora[inicio] = 0

    while bool(len(frontera)):
        actual = buscar_menor_F(frontera)
        draw_square(actual)  # Draw search expansion
        
        if actual == objetivo:
            break
        
        for sucesor in grafo.vecinos(actual):
            costo_nuevo = costo_hasta_ahora[actual] + 1
            if sucesor not in costo_hasta_ahora or costo_nuevo < costo_hasta_ahora[sucesor]:
                costo_hasta_ahora[sucesor] = costo_nuevo
                prioridad = heuristic(sucesor)
                frontera.append((sucesor, prioridad))
                padres[sucesor] = actual
                
        print(frontera)
        
    return padres

def dfs_non_recursive(Grafo, origen, nodo_fin):
    padres = {}
    padres[origen] = None
    # if origen is None or origen not in Grafo.vecinos(origen):
    #    return "Invalid input"
    camino = []
    pila = [origen]
    while len(pila) != 0:
        s = pila.pop()
        draw_square(s)
        if s == nodo_fin:
            break
        if s not in camino:
            camino.append(s)
        if s not in Grafo.aristas.keys():
            # leaf node
            continue

        for vecino in Grafo.vecinos(s):
            if vecino not in camino:
                pila.append(vecino)
                padres[vecino] = s
    return padres


def bfs_non_recursive(grafo, origen, nodo_fin):
    padres = {}
    padres[origen] = None
    # if origen is None or origen not in Grafo.vecinos(origen):
    #    return "Invalid input"
    camino = []
    pila = [origen]
    while len(pila) != 0:
        s = pila.pop(0)
        if s == nodo_fin:
            draw_square(s)
            break
        if s not in camino:
            camino.append(s)
            draw_square(s)
        if s not in grafo.aristas.keys():
            # leaf node
            continue

        for vecino in grafo.vecinos(s):
            if vecino not in camino:
                pila.append(vecino)
                padres[vecino] = s
    return padres


def geo_pos(id):
    """
    Builds Laberinto's cities positional information 
    The map is a png image used as backgroud, 
    the position corresponds to an approximated pixel
    for each city
    """
    G = {
        '1': (56, 56),
        '2': (112, 56),
        '3': (168, 56),
        '4': (168, 112),
        '5': (112, 112),
        '6': (56, 112),
        '7': (56, 168),
        '8': (112, 168),
        '9': (112, 224),
        '10': (168, 224),
        '11': (168, 168),
        '12': (224, 168),
        '13': (56, 224),
        '14': (56, 280),
        '15': (112, 280),
        '16': (168, 280),
        '17': (224, 280),
        '18': (224, 224),
        '19': (280, 224),
        '20': (280, 280),
        '21': (336, 280),
        '22': (280, 168),
        '23': (280, 112),
        '24': (224, 112),
        '25': (224, 56),
        '26': (292, 56),
        '27': (349, 56),
        '28': (349, 112),
        '29': (405, 56),
        '30': (390, 112),
        '31': (402, 168),
        '32': (453, 168),
        '33': (460, 112),
        '34': (461, 56),
        '35': (526, 56),
        '36': (561, 56),
        '37': (562, 112),
        '38': (512, 112),
        '39': (515, 168),
        '40': (518, 224),
        '41': (568, 224),
        '42': (570, 168),
        '43': (471, 224),
        '44': (464, 280),
        '45': (412, 280),
        '46': (512, 280),
        '47': (564, 280),
        '48': (346, 168),
        '49': (352, 224),
        '50': (401, 224)
    }

    return G[id]


def heuristic(id):
    """
    Builds Laberinto heuristic
    """
    H = {
        '1': 555.1936599061628,
        '2': 504.4601074416093,
        '3': 454.9637348185018,
        '4': 430.1627598944381,
        '5': 482.21157182299146,
        '6': 535.0588752651432,
        '7': 520.1999615532472,
        '8': 465.66941063376714,
        '9': 455.45581563967323,
        '10': 399.93999549932494,
        '11': 411.53371672318667,
        '12': 357.9720659492861,
        '13': 511.0772935672255,
        '14': 508.0,
        '15': 452.0,
        '16': 396.0,
        '17': 340.0,
        '18': 344.58090486850836,
        '19': 289.4684784220901,
        '20': 284.0,
        '21': 228.0,
        '22': 305.28675044947494,
        '23': 329.9696955782455,
        '24': 379.24134795668044,
        '25': 407.1559897631373,
        '26': 352.3634487287239,
        '27': 310.4851043125902,
        '28': 272.85344051340087,
        '29': 274.6943756249844,
        '30': 241.8677324489565,
        '31': 196.9466932954194,
        '32': 157.6863976378432,
        '33': 197.5854245636555,
        '34': 246.54614172604687,
        '35': 227.20035211240318,
        '36': 224.0200883849482,
        '37': 168.01190434013893,
        '38': 175.86358349584486,
        '39': 122.24974437601085,
        '40': 72.47068372797375,
        '41': 56.1426753904728,
        '42': 112.16059914247961,
        '43': 108.55873986004076,
        '44': 100.0,
        '45': 152.0,
        '46': 52.0,
        '47': 0.0,
        '48': 245.08773939142694,
        '49': 219.2715211786519,
        '50': 172.35138525698017
    }

    return H[id]


def main():
    """
    EJEMPLO DE USO:
        python deber2.py 1 1
        argumento 1: Nodo inicial
        argumento 2: Algoritmo a usar>>
        1>> A*
        2>> DFS
        3>> BFS
        4>> Greddy
    """
    nodo_inicio = '1'
    algoritmo = '2'

    # Always Bucarest due to heuristic is given for this end city
    nodo_fin = '47'
    Laberinto = Grafo()  # Builds Laberinto Grafo

    # Adding aristas (adjacency list)
    Laberinto.aristas = {
        '1': ['2', '6'],
        '2': ['1', '3'],
        '3': ['2', '4'],
        '4': ['3', '5'],
        '5': ['4'],
        '6': ['1', '7'],
        '7': ['6', '8'],
        '8': ['7', '9'],
        '9': ['8', '10', '13'],
        '10': ['9', '11'],
        '11': ['10', '12'],
        '12': ['11'],
        '13': ['9', '14'],
        '14': ['13', '15'],
        '15': ['14', '16'],
        '16': ['15', '17'],
        '17': ['16', '18'],
        '18': ['17', '19'],
        '19': ['18', '20', '22'],
        '20': ['19', '21'],
        '21': ['20'],
        '22': ['19', '23', '48'],
        '23': ['22', '24'],
        '24': ['23', '25'],
        '25': ['24', '26'],
        '26': ['25', '27'],
        '27': ['26', '28', '29'],
        '28': ['27', '30'],
        '29': ['27', '30', '34'],
        '30': ['28', '29', '31'],
        '31': ['30', '32'],
        '32': ['31', '33'],
        '33': ['32'],
        '34': ['29', '35'],
        '35': ['34', '36'],
        '36': ['35', '37'],
        '37': ['36', '38'],
        '38': ['37', '39'],
        '39': ['38', '40'],
        '40': ['39', '41', '43'],
        '41': ['40', '42'],
        '42': ['41'],
        '43': ['40', '44'],
        '44': ['43', '45', '46'],
        '45': ['44'],
        '46': ['44', '47'],
        '47': ['46'],
        '48': ['22', '49'],
        '49': ['48', '50'],
        '50': ['49']
    }

    if nodo_inicio not in Laberinto.aristas.keys():
        print("Nodo no existe")
        return

    # Define screen and World Wide coordinates
    screen = turtle.Screen()
    screen.setup(600, 327)
    turtle.setworldcoordinates(0, 0, 600, 327)

    # Use image as backgroud (image is 600x327 pixels)
    turtle.bgpic('Picture1.png')

    # Get image anchored to left-bottom corner (sw: southwest)
    canvas = screen.getcanvas()
    canvas.itemconfig(screen._bgpic, anchor="sw")

    if algoritmo == '1':
        # Building aStar camino of padres
        padres = aStar(Laberinto, nodo_inicio, nodo_fin)
    if algoritmo == '2':
        padres = dfs_non_recursive(Laberinto, nodo_inicio, nodo_fin)
    if algoritmo == '3':
        padres = bfs_non_recursive(Laberinto, nodo_inicio, nodo_fin)
    if algoritmo == '4':
        padres = greedy(Laberinto, nodo_inicio, nodo_fin)    
    # padres = dfs(visited, Laberinto, '1',padresDfs)

    # Calculating and printing the shortest camino
    camino_mas_corto = camino_desde_origen(nodo_inicio, nodo_fin, padres)
    print(camino_mas_corto)

    # Calculating the cost of the shortest camino
    cost_tsp = costofcamino(camino_mas_corto, Laberinto)

    # Draw shortest camino
    for ni in camino_mas_corto:
        draw_square(ni, color="salmon")

    # Animate shortest camino agent and include cost
    tsp = turtle.Turtle(shape="square")

    for i, ni in enumerate(camino_mas_corto):
        draw_square(ni, color="dodger blue", ts=tsp, text=cost_tsp[i])

    turtle.exitonclick()  # Al hacer clic sobre la ventana grafica se cerrara


if __name__ == "__main__":
    import sys
    # main(sys.argv[1:])
    main()