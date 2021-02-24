'''
definimos la función de a* con el nombre de aStar
n0 es el nodo desde el que queremos empezar a realizar la búsqueda

A es la matriz de adyacencia

T es el nodo terminal al que queremos llegar

Q (queue) es una lista en donde vamos a enlistar los nodos pendientes a través de cada iteración
al inicio añadimos nuestro nodo inicial n0 a Q

g(n0) va a ser 0 al inicio porque la distancia del nodo inicial al nodo inicial es 0

al inicio fe (funcion de evaluacion) es la heurística del nodo inicial n0
Etiquetamos el nodo con nuestra funcion fe

para todo nodo que no sea el inicial al inicio su fe es infinita

El ciclo de iteraciones:
Si no tenemos un nodo en nuestra Q que sea igual a T, no hemos encontrado la solución y la Q debe ser diferente de vacio
    'u' va a ser el primer nodo de nuestra lista (al inicio obviamente será n0)
    Expandemos 'u':
        Suprimimos u de Q
        Iteramos en los vecinos de u
        Calculamos fe'
        Si fe' es menor que fe (que era infinito porque así los inicializamos a todos)
            Actualizamos la etiqueta de v con fe'(v)
            Insertamos v en Q (como priority queue porque  ponemos el que tenga la fe de menor a mayor)
        Sino
            Dejamos la etiqueta de v con su valor original 
        
   
El algoritmo termina si: 
    Q es igual a vacío (no tenemos la solución)
    Q tiene interseccion con T (encontramos la solucion y mostramos el camino para llegar a T)

Algo que hay que aclarar: tenemos una lista 'p' donde agregamos los nodos a los que ya visitamos
'''

import math

visitados = []

def fe(g,h):    #funcion de evaluacion, g(n) indica la distancia del nodo origen hasta el nodo n
    return (g+h)    # h(n) heurística, indica la distancia estimada desde el nodo n hasta el nodo destino





def intercambiar(array, p1, p2):    #para intercambiar valores en arreglos
    tmp = array[p1]
    array[p1] = array[p2]
    array[p2] = tmp

class Nodo:
    def __init__(self,array,padre):
        self.padre = padre
        self.izquierdo = None
        self.derecho = None
        self.arriba = None
        self.abajo = None
        self.array = array
        self.etiqueta = math.inf

    def heuristica(self):  # comprobamos cuantos nuemros no están en su posicion
        self.array

    def expandir(u):
        #iteramos en los vecinos de u
        if(u.array[0] == 0):    #aqui la posicion 0 del array es cero, por lo que solo se puede intercambiar con la derecha y abajo
            #intercambiando 0 con su derecho
            u.derecho = Nodo(u, True)
            intercambiar(u.derecho.array,0,1)
            # intercambiando 0 con abajo
            u.abajo = Nodo(u, True)
            intercambiar(u.abajo.array,0,3)

        if (u.array[1] == 0):  # aqui la posicion 1 del array es cero, por lo que solo se puede intercambiar con izquierda, abajo y derecha
            # intercambiando 1 con su izquierdo
            u.izquierdo = Nodo(u, True)
            intercambiar(u.izquierdo.array, 1, 0)
            # intercambiando 1 con abajo
            u.abajo = Nodo(u, True)
            intercambiar(u.abajo.array, 1, 4)
            # intercambiando 1 con derecho
            u.derecho = Nodo(u, True)
            intercambiar(u.derecho.array, 1, 2)

        if (u.array[2] == 0):  # aqui la posicion 2 del array es cero, por lo que solo se puede intercambiar con izquierda y abajo
            # intercambiando 0 con su izquierda
            u.izquierdo = Nodo(u, True)
            intercambiar(u.izquierdo.array, 2, 1)
            # intercambiando 0 con abajo
            u.abajo = Nodo(u, True)
            intercambiar(u.abajo.array, 2, 5)

        if (u.array[3] == 0):  # pos 3 de array es 0, se puede intercambiar con arribo, derecha abajo
            # intercambiando 0 con su arriba
            u.arriba = Nodo(u, True)
            intercambiar(u.arriba.array, 3, 0)
            # intercambiando 0 con derecho
            u.derecho = Nodo(u, True)
            intercambiar(u.derecho.array, 3, 4)
            # intercambiando 0 con abajo
            u.abajo = Nodo(u, True)
            intercambiar(u.abajo.array, 3, 6)

        if (u.array[4] == 0):  # pos 4 de array es 0, se puede intercambiar con todos
            # intercambiando 0 con su arriba
            u.arriba = Nodo(u, True)
            intercambiar(u.arriba.array, 4, 1)
            # intercambiando 0 con abajo
            u.abajo = Nodo(u, True)
            intercambiar(u.abajo.abajo, 4, 7)
            # intercambiando 0 con izquierda
            u.izquierdo = Nodo(u, True)
            intercambiar(u.izquierdo.array, 4, 3)
            # intercambiando 0 con derecha
            u.derecho = Nodo(u, True)
            intercambiar(u.derecho.array, 4, 5)

        if (u.array[5] == 0):  # pos 5 de array es 0, se puede intercambiar con arriba, izquierda y abajo
            # intercambiando 0 con su arriba
            u.arriba = Nodo(u, True)
            intercambiar(u.arriba.array, 5, 2)
            # intercambiando 0 con abajo
            u.abajo = Nodo(u, True)
            intercambiar(u.abajo.abajo, 5, 8)
            # intercambiando 0 con izquierda
            u.izquierdo = Nodo(u, True)
            intercambiar(u.izquierdo.array, 5, 4)

        if (u.array[6] == 0):  # pos 6 de array es 0, se puede intercambiar con arriba y derecha
            # intercambiando 0 con su arriba
            u.arriba = Nodo(u, True)
            intercambiar(u.arriba.array, 6, 3)
            # intercambiando 0 con derecha
            u.derecho = Nodo(u, True)
            intercambiar(u.derecho.array, 6, 7)

        if (u.array[7] == 0):  # pos 7 de array es 0, se puede intercambiar con izquierda, arriba, derecha
            # intercambiando 0 con su arriba
            u.arriba = Nodo(u, True)
            intercambiar(u.arriba.array, 7, 4)
            # intercambiando 0 con izquierda
            u.izquierdo = Nodo(u, True)
            intercambiar(u.izquierdo.array, 7, 6)
            # intercambiando 0 con derecha
            u.derecho = Nodo(u, True)
            intercambiar(u.derecho.array, 7, 8)

        if (u.array[8] == 0):  # pos 8 de array es 0, se puede intercambiar con izquierda y arriba
            # intercambiando 0 con su arriba
            u.arriba = Nodo(u, True)
            intercambiar(u.arriba.array, 8, 5)
            # intercambiando 0 con izquierda
            u.izquierdo = Nodo(u, True)
            intercambiar(u.izquierdo.array, 8, 7)

        #Calculamos la funcion fe, cuyo resultado quedará en la tiqueta de cada uno de nuestros vecinos

        #primero comprobamos heuristica
        heuristica()



def aStar(n0, T):
    print("holi")
    Q = []
    Q.append(n0)

    while 1:
        #revisamos si hay interseccion con T
        if(T == w.array):
            iguales = True  #si la hay, iguales = True
        else:
            iguales = False #si no la hay

        #buscamos interseccion de T con Q
        if (Q == None) and (iguales == True):
            print("holi3")
            u = Q[0]    #tomamos el primer elñemento de Q
            Q.pop(0)    #eliminamos el primer elemento de Q
            expandir(u)


n0a = [0,1,2,
       3,4,5,
       6,7,8]

T = [1,2,3,
     8,0,4,
     7,6,5]

n0 = Nodo(n0a, True)
n0.etiqueta = 0
iguales = False
w = Nodo(T, False)

#aStar(n0,T)





#f=fe(1,3)
