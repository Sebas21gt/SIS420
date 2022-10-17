# datos = estado
class Nodo:
    def __init__(self, datos, hijo=None):
        self.datos = datos
        self.hijos = []
        self.padre = None
        self.costo = None
        self.set_hijo(hijo)
        
    def set_hijo(self, hijo):
        if (hijo is not None):
            self.hijos.append(hijo)
            if self.hijos is not None:
                for h in self.hijos:
                    h.padre = self
                
    def get_hijos(self):
        return self.hijos
    
    def set_padre(self, padre):
        self.padre = padre
        
    def get_padre(self):
        return self.padre

    def set_datos(self, datos):
        self.datos = datos
    
    def get_datos(self):
        return self.datos
    
    def set_costo(self, costo):
        self.costo = costo
        
    def get_costo(self):
        return self.costo
    
    def equal(self, nodo):
        if self.get_datos() == nodo.get_datos():
            return True
        else:
            return False
    
    def en_lista(self, lista_nodos):
        enlistado = False
        for n in lista_nodos:
            if self.equal(n):
                enlistado = True
        return enlistado
    
    def __str__(self):
        return str(self.get_datos())

#GONZALES TITO SEBASTIAN
#LINK REPOSITORIO
#https://github.com/Sebas21gt/SIS420/tree/main/Laboratorios
"""
1.-Implementar una funcion que permita expandir nodos hijos para n caracteres, los cuales deben ser establecidos al momento de iniciar el programa.
2.-Describir cual es el nivel maximo de numero de digitos que el rompecabezas se puede resolver en su maquina, explicando a que se deberia este limite y como se lo podria superara.
3.-Hacer correr el mismo programa, pero utilizando una lista LIFO para la lista frontera."""


"""En este caso mi programa solo funciona hasta 7 digitos con una respuesta de 4min 
Debido a la memoria de la computadora, esta implementado con 2 ciclos for para recorrer el rompecabezas y una lista FIFO
ya que con las listas LIFO en este caso tarda mas, pero se puede modificar en la parte donde comente 
Para generar los numeros que me da al iniciar el programa esta detallado en el Main con ciclo for y funcion sorted y reverse para crear otra lista y darle reversa para generar el PEOR CASO para el rompecabezas"""


def bpa(estado_inicio, estado_solucion):
    resuelto = False
    nodos_visitados = []
    nodos_frontera = []
    nodo_inicio = Nodo(estado_inicio)
    nodos_frontera.append(nodo_inicio)
    
    while resuelto == False and len(nodos_frontera) != 0:
        #Sacar el cero 0 de la funcion pop para que se vuelva lista LIFO
        nodo_actual = nodos_frontera.pop(0)
        nodos_visitados.append(nodo_actual)
        if nodo_actual.get_datos() == estado_solucion:
            resuelto = True
            return nodo_actual
        else:
            #Bucle para recorrer 
            for i in range(0, len(estado_solucion)-1):
              elemento = estado_solucion[i]
              for j in range(0, len(estado_inicio)-1):
                indice = estado_inicio.index(elemento)
                
                hijo_datos = nodo_actual.get_datos().copy()
                temp = hijo_datos[indice-1]
                hijo_datos[indice-1] = hijo_datos[indice]
                hijo_datos[indice] = temp
                hijo = Nodo(hijo_datos)
                
                if not hijo.en_lista(nodos_visitados) and not hijo.en_lista(nodos_frontera):
                    nodo_actual.set_hijo(hijo)
                    nodos_frontera.append(hijo)

if __name__ == "__main__":
    tamano = int(input("Ingrese la cantidad de numeros para el rompecabezas: "))
    solucion = []
    
    #Ciclo para generar la solucion del tamaño de un numero dado
    for i in range(1, tamano+1):
        solucion = solucion + [i]

    """Con esta linea de codigo genero el estado inicial PEOR CASO
    tomando como base la solucion y colocandolo de reversa
    y con la funcion sorted genero otra nueva lista"""
    estado_inicial = sorted(solucion, reverse=True)
    print("Estado Inicial", estado_inicial)
    print("Solucion", solucion)

    nodo_solucion = bpa(estado_inicial, solucion)

    # mostrar resultado
    resultado = []
    nodo_actual = nodo_solucion
    while nodo_actual.get_padre() is not None:
        resultado.append(nodo_actual.get_datos())
        nodo_actual = nodo_actual.get_padre()

    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)