# Aqui agregas las posiciones, para validar q no pasamos dos veces por donde mismo
recorrido = [
    (1, 2), (1, 1), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), (5, 1), (6, 1), (6, 2), 
    (6, 3), (6, 4), (7, 4), (8, 4), (8, 3), (8, 2), (9, 2), (9, 1), (10, 1), (11, 1), 
    (11, 2), (11, 3), (10, 3), (10, 4), (11, 4), (12, 4), (12, 5), (12, 6), (12, 7), 
    (12, 8), (12, 9), (11, 9), (11, 10), (12, 10), (12, 11), (12, 12), (11, 12), 
    (11, 11), (10, 11), (9, 11), (9, 10), (8, 10), (7, 10), (6, 10), (5, 10), (4, 10), 
    (3, 10), (3, 9), (2, 9), (2, 8), (2, 7), (2, 6), (1, 6), (1, 5), (2, 5), (2, 4), 
    (3, 4), (4, 4), (4, 5), (4, 6), (5, 6), (6, 6), (6, 7), (6, 8), (7, 8), (8, 8), 
    (8, 7), (8, 6), (9, 6), (9, 5), (10, 5), (11, 5), (11, 6)
]


ciclo = [par for 
                par in 
                recorrido if 
                recorrido.count(par) > 1]
res = list(set(ciclo)) 

if res:
    print(f"Repetidas: {res}")
else:
    print("Todo ok.")
