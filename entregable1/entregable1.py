import sys
from typing import *
import itertools

from algoritmia.datastructures.digraphs import UndirectedGraph
from algoritmia.datastructures.queues import Fifo

Vertex = Tuple[int, int]
Edge = Tuple[Vertex, Vertex]
Path = List[Vertex]
Pair = Tuple[int, int]


# -----------------------------------------------------


# - Recibe un descriptor de fichero que contiene lineas de texto que
#   representan un laberinto.
# - Devuelve una tupla de dos elementos:
#   - El primero: una tupla con el tamaño del laberinto: (num_rows, num_cols)
#   - El segundo: el grafo del laberinto.
def read_data(f) -> Tuple[Pair, UndirectedGraph]:
    dd = {'n': (-1, 0), 's': (1, 0), 'e': (0, 1), 'w': (0, -1)}
    m = []
    for line in f.readlines():
        m.append(line.strip().split(','))
    rows = len(m)
    cols = len(m[0])
    e = [((r, c), (r + dd[d][0], c + dd[d][1])) for r in range(rows)
         for c in range(cols) for d in 'nsew' if d not in m[r][c]]
    return (rows, cols), UndirectedGraph(E=e)

def crea_matriz(rows:int, cols: int) -> List[List[int]]:
    matriz = []
    for i in range(rows):
        a = [0]*cols
        matriz.append(a)
    return matriz

def matriz_distancia_desde_origen(size: Pair, grafo: UndirectedGraph) -> List[List[int]]:
    queue = Fifo()
    seen = set()
    queue.push(((0, 0), (0, 0)))
    seen.add((0, 0))
    matriz = crea_matriz(size[0],size[1])
    matriz[0][0] = 0
    u, v = queue.pop()
    matriz[v[0]][v[1]] = 1
    queue.push((u, u))
    while len(queue)>0:
        u, v = queue.pop()
        padre = matriz[v[0]][v[1]]
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                matriz[suc[0]][suc[1]] = padre + 1
                queue.push((v, suc))
    return matriz

def matriz_distancia_desde_destino(size: Pair, grafo: UndirectedGraph) -> List[List[int]]:
    queue = Fifo()
    seen = set()
    queue.push(((size[0]-1, size[1]-1), (size[0]-1, size[1]-1)))
    seen.add((size[0]-1, size[1]-1))
    matriz = crea_matriz(size[0], size[1])
    matriz[size[0]-1][size[1]-1] = 0
    u, v = queue.pop()
    matriz[v[0]][v[1]] = 1
    queue.push((u, u))
    while len(queue)>0:
        u, v = queue.pop()
        padre = matriz[v[0]][v[1]]
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                matriz[suc[0]][suc[1]] = padre + 1
                queue.push((v, suc))
    return matriz

def recorredor_aristas_anchura(grafo: UndirectedGraph, v_inicial: Vertex) -> List[Edge]:
    aristas = []
    queue = Fifo()
    seen = set()
    queue.push((v_inicial, v_inicial))
    seen.add(v_inicial)
    while len(queue)>0:
        u, v = queue.pop()
        aristas.append((u, v))
        for suc in grafo.succs(v):
            if suc not in seen:
                seen.add(suc)
                queue.push((v, suc))
    return aristas

def recuperador_camino(lista_aristas: List[Edge], v: Vertex) -> List[Vertex]:
    bp = {}
    for orig,dest in lista_aristas:
        bp[dest] = orig
    camino = []
    camino.append(v)
    while v != bp[v]:
        v = bp[v]
        camino.append(v)
    camino.reverse()
    return camino

# - Tiene dos parámetros,
#   - El primero: una tupla con el tamaño del laberinto (num_rows, num_cols)
#   - El segundo: el grafo del laberinto.
# - Devuelve una tupla con tres elementos. Por orden:
#    - Una tupla (row, col) con la posición donde colocar el tesoro.
#    - Una lista de vértices con el camino desde la entrada hasta el tesoro.
#    - Una lista de vértices con el camino desde el tesoro hasta la salida.
def process(size: Pair, lab: UndirectedGraph) -> Tuple[Pair, Path, Path]:
    distancia_origen = matriz_distancia_desde_origen(size, lab)
    distancia_destino = matriz_distancia_desde_destino(size, lab)
    max = distancia_origen[0][0]
    maxr = 0
    maxc = 0
    size0 = list(range(size[0]))
    size1 = list(range(size[1]))

    for r, c in itertools.product(size0, size1):
        distancia = distancia_origen[r][c] + distancia_destino[r][c]
        if distancia > max:
            max = distancia
            maxr = r
            maxc = c
        else:
            if distancia == max and r < maxr:
                max = distancia
                maxr = r
                maxc = c
            else:
                if distancia == max and r == maxr and c < maxc:
                    max = distancia
                    maxr = r
                    maxc = c

    camino_origen = recuperador_camino(recorredor_aristas_anchura(lab, (0, 0)), (maxr, maxc))
    camino_destino = recuperador_camino(recorredor_aristas_anchura(lab, (maxr, maxc)), (size[0] - 1, size[1] - 1))
    return (maxr, maxc), camino_origen, camino_destino


# - Tiene tres parámetros:
#    - una tupla (row, col).
#    - lista de vértices desde la entrada hasta el tesoro
#    - lista de vértices desde el tesoro hasta la salida
# - Muestra cuatro líneas por la salida estándar. Por orden:
#    - Fila del tesoro
#    - Columna del tesoro
#    - Longitud del camino desde la entrada hasta el tesoro (nº de vertices menos 1)
#    - Longitud del camino desde el tesoro hasta la salida (nº de vertices menos 1)
def show_results(pos: Pair, c1: Path, c2: Path):
    print(pos[0])
    print(pos[1])
    print(len(c1) - 1)
    print(len(c2) - 1)

# -----------------------------------------------------

if __name__ == '__main__':
    size, lab = read_data(sys.stdin)
    pos, path1, path2 = process(size, lab)
    show_results(pos, path1, path2)
