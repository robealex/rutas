#Este modulo proporciona una implementacion del algoritmo de montículos, tambien conocido como algoritmo de cola con prioridad.
#Tambien se le conoce como BEST FIRST SEARH
#https://www.analyticsvidhya.com/blog/2023/09/best-first-search-in-artificial-intelligence/
#https://docs.python.org/es/3/library/heapq.html

import heapq
import time

def heuristica(a, b):
    return 0
#Lectura de las coordenadas en la matriz (pero se escuha mejor con x)
def coordenadas(matrix, x, y):
    return matrix[x][y] if isinstance(matrix[x][y], int) else 0
#Matrix es la matriz nxm
#start el punto unicial y el end el punto final
#pad es <,^,>,v, los mov q hara
#n lo puse para q cuente nxn = 13

def negas(matrix, start, end):
    n = len(matrix)
    pad = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    #frontera es la lista q se usara como cola de prioridad
    #heapq.heappush(heap, item):Empujar el valor item en el heap, manteniendo el montículo invariable.
    #visitados son todos los puntos ya visitados
    #mejor valor es solo para guardar el mejor valor menor
    #mejor ruta es la suma de los valores 


    frontera = []
    heapq.heappush(frontera, (0, start, [start], 0))
    visitados = set()
    mejor_valor = float('inf')
    mejor_ruta = None
    
    #Este es un ciclo que se ejecutara siempre q haya nodos en la cola
    #https://rico-schmidt.name/pymotw-3/heapq/index.html
    while frontera:
        coste_actual, celda_actual, ruta_actual, suma_actual = heapq.heappop(frontera)
#la validacion de la suma acumulada del camino actual es menor 
# que el mejor valor encontrado, actualiza el mejor valor y la mejor ruta.
        if celda_actual == end:
            if suma_actual < mejor_valor:
                mejor_valor = suma_actual
                mejor_ruta = ruta_actual
            continue
#este fue el mayor problema, dado que si no pongo la restriccion
#el ciclo pasa por donde mismo ademas de que se tardara en ejecutar, incluso
#me di cuenta q si no lo valido se ejecuta infinito... comiendose la memoria...
#pobre de mi lap

#si ya lo visite pos lo salto
        if celda_actual in visitados:
            continue
#y lo agrego a la lista de q ya fue visitado
        visitados.add(celda_actual)
#Es la iteracion en el movimiento de el pad, se calcula la posicion en la matriz
#y validamos q no hayamos llegado ahi
#se agrega la a la suma de numeros
#el heapq.heappush lo q hace es q agrega el nodo a la cola para actualizar eñ acumulado
        for dx, dy in pad:
            nx, ny = celda_actual[0] + dx, celda_actual[1] + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visitados:
                nuevo_suma = suma_actual + coordenadas(matrix, nx, ny)
                heapq.heappush(frontera, (nuevo_suma, (nx, ny), ruta_actual + [(nx, ny)], nuevo_suma))
    
    return mejor_ruta, mejor_valor
#una vez q termine el mas negativo, el mas posotivo es igual y
#es mas facil, el mayor problemo es q si lo ejecutaba al mismo tiempo.
#se ejecutaba raro y no me daba numeros positivos, siendo q al hacer 
#cuentas manuales me da positivo, por eso lo separe, no veo diferencia en el contexto de gasto de memoria
def posi(matrix, start, end):
    n = len(matrix)
    pad = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    
    frontera = []
    heapq.heappush(frontera, (0, start, [start], 0))
    visitados = set()
    mejor_valor = float('-inf')
    mejor_ruta = None
    
    while frontera:
        coste_actual, celda_actual, ruta_actual, suma_actual = heapq.heappop(frontera)
        coste_actual = -coste_actual  # <--justo aqui invertimos para la suma

        if celda_actual == end:
            if suma_actual > mejor_valor:#aqui tambien invertimos el menor q a mayor, por q buscamos el numero mayor
                mejor_valor = suma_actual
                mejor_ruta = ruta_actual
            continue
#se valida q no lo hayamos visitado
        if celda_actual in visitados:
            continue

        visitados.add(celda_actual)

        for dx, dy in pad:
            nx, ny = celda_actual[0] + dx, celda_actual[1] + dy
            if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visitados:
                nuevo_suma = suma_actual + coordenadas(matrix, nx, ny)
                heapq.heappush(frontera, (-nuevo_suma, (nx, ny), ruta_actual + [(nx, ny)], nuevo_suma))
                #e igual lo mandamos a negativo para ejecutar la suma
    
    return mejor_ruta, mejor_valor

def imprimir_res(matrix, start, end):
    #camino más negativo
    inicio_tiempo = time.time()
    camino_minimo, suma_minima = negas(matrix, start, end)#estas son coordenadas
    fin_tiempo = time.time()#esto lo puse por q se me quedaba trabado, y queria saber cuanto tardaba
    print(f"El camino con la suma más negativa es: {camino_minimo}")
    print(f"Y la suma de los números en ese camino es: {suma_minima}")
    print(f"Tiempo de ejecución para el camino más negativo: {fin_tiempo - inicio_tiempo:.4f} segundos")

    #Camino más positivo 
    inicio_tiempo = time.time()
    camino_maximo, suma_maxima = posi(matrix, start, end)
    fin_tiempo = time.time()
    print(f"\nEl camino con la suma más positiva es: {camino_maximo}")
    print(f"Y la suma de los números en ese camino es: {suma_maxima}")
    print(f"Tiempo de ejecución para el camino más positivo: {fin_tiempo - inicio_tiempo:.4f} segundos")


matriz = [
    [-3, -3,  2, -3, 3, -2, -2, 1, 2, 0, 2, 0, 1],
    [ 2,  3, 'i', -1, -1, 3, 2, 0, -3, -3, 2, 2, 1],
    [ 1, -3, -3,  2,  3,  1,  3, 3, 2,  1, -2, -2,  3],
    [ 0,  0,  3,  0,  3, -3, -2, -3,  0,  2,  2,  1,  1],
    [ 2, -1, -1, -3,  3,  3,  0, -3,  1, -2,  2,  0,  1],
    [ 0,  3, -1,  1, -1, -2,  2, -2,  2, -1, -2, -3,  0],
    [ 0,  3,  2,  0,  1,  1,  2,  3, -1, -3,  0,  0, -2],
    [ 3,  3, -3, -2,  3, -3, -1, -3,  3, -2,  2, -2, -1],
    [-2, -2,  1,  0, -1,  0,  3,  0,  0, -2,  2, -3, -1],
    [-3,  3,  0, -1, -3,  1,  2, -3,  2, -3,  0,  2, -2],
    [-3, -3, -3,  3, -2,  0, -2, -3,  1,  2,  1, -1, -2],
    [-1,  0,  1,  2,  1,  0, 'f', 0, -3,  3,  3,  0, -1],
    [ 1, -3,  1,  0,  1,  2,  3,  1, -2,  3,  3,  0,  3]
]

inicio = (1, 2)
fin = (11, 6)

imprimir_res(matriz, inicio, fin)
# una disculpa pero no soy tam bueno agregando graficas por eso puse tambien q salieran las posiciones.
