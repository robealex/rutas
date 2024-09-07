Algoritmo de Búsqueda de Rutas con Menor y Mayor Costo
Descripcion:Este proyecto implementa un algoritmo personalizado en Python para encontrar dos caminos distintos en una matriz de entrada: uno con el menor costo (suma más negativa) y otro con el mayor costo (suma más positiva).
No se usa Dijkstra sino Best first search

Descripcion de el codigo:
Camino con menor costo (suma más negativa):

La función negas utiliza una estructura de heap para priorizar las rutas con la menor suma acumulada.
Se evalúan las celdas vecinas (pad por que son los movimientos en ellos, arriba, abajo, izquierda, derecha) y se avanza en la dirección que minimiza la suma de los valores en la matriz.
Camino con mayor costo (suma más positiva):

La función posi invierte la lógica para priorizar las rutas con la mayor suma acumulada.
De manera similar, las celdas vecinas se exploran en cada paso, pero se busca maximizar la suma en este caso.
En ambos casos, se asegura que el algoritmo no revisita las coordenadas previamente exploradas.

Uso:
La matriz de entrada y los puntos de inicio y fin están definidos dentro del código:


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

Resultados:
El camino con la suma más negativa es: [(1, 2), (2, 2), (2, 1), (3, 1), (4, 1), (4, 2), (4, 3), (5, 3), (5, 4), (5, 5), (6, 5), (7, 5), (7, 6), (7, 7), (8, 7), (9, 7), (10, 7), (10, 6), (10, 5), (10, 4), (9, 4), 
(8, 4), (8, 3), (7, 3), (7, 2), (8, 2), (8, 1), (8, 0), (9, 0), (10, 0), (10, 1), (10, 2), (11, 2), (11, 1), (12, 1), (12, 2), (12, 3), (12, 4), (11, 4), (11, 5), (11, 6)]
Y la suma de los números en ese camino es: -52
Tiempo de ejecución para el camino más negativo: 0.0010 segundos

El camino con la suma más positiva es: [(1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (6, (12, 10), (12, 11), (12, 12), (11, 12), (11, 11), (10, 11), (9, 11), (9, 10), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), (3, 10), (3, 9), (2, 9), (2, 8), (2, 7), (2, 6), (1, 6), (1, 5), (2, 5), (2, 4), (3, 4), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), (8, 7), (8, 6), (9, 6), (9, 5), (10, 5), (11, 5), (11, 6)]
Y la suma de los números en ese camino es: 95
Tiempo de ejecución para el camino más positivo: 0.0010 segundos

Se agrega revision.py para que se copie le camino de las coordenadas, y se ejecute y asi poder saber si es correcto o no
