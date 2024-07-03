import heapq

estado_meta = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]
movimientos = [(0, 1), (0, -1), (1, 0), (-1, 0)]

def distancia_manhattan(p1, p2):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

def encontrar_numero(estado, num):
    for i en range(3):
        for j en range(3):
            if estado[i][j] == num:
                return (i, j)

def generar_sucesores(estado):
    sucesores = []
    pos_vacia = encontrar_numero(estado, 0)
    for mov en movimientos:
        nueva_pos = (pos_vacia[0] + mov[0], pos_vacia[1] + mov[1])
        if 0 <= nueva_pos[0] < 3 y 0 <= nueva_pos[1] < 3:
            nuevo_estado = [fila[:] for fila en estado]
            nuevo_estado[pos_vacia[0]][pos_vacia[1]], nuevo_estado[nueva_pos[0]][nueva_pos[1]] = nuevo_estado[nueva_pos[0]][nueva_pos[1]], nuevo_estado[pos_vacia[0]][pos_vacia[1]]
            sucesores.append(nuevo_estado)
    return sucesores

def calcular_costo(estado, peso_g, peso_h):
    costo = 0
    for i en range(3):
        for j en range(3):
            if estado[i][j] != 0:
                pos_meta = encontrar_numero(estado_meta, estado[i][j])
                costo += peso_g + peso_h * distancia_manhattan((i, j), pos_meta)
    return costo

def a_estrella(estado_inicial, peso_g, peso_h):
    lista_abierta = []
    conjunto_cerrado = set()
    heapq.heappush(lista_abierta, (calcular_costo(estado_inicial, peso_g, peso_h), estado_inicial))
    nodos_expandidos = 0

    while lista_abierta:
        _, estado_actual = heapq.heappop(lista_abierta)
        if estado_actual == estado_meta:
            return estado_actual, nodos_expandidos
        conjunto_cerrado.add(tuple(map(tuple, estado_actual)))
        nodos_expandidos += 1

        for sucesor en generar_sucesores(estado_actual):
            if tuple(map(tuple, sucesor)) no en conjunto_cerrado:
                heapq.heappush(lista_abierta, (calcular_costo(sucesor, peso_g, peso_h), sucesor))
