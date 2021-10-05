import sys
from typing import *

from algoritmia.datastructures.digraphs import UndirectedGraph

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


# - Tiene dos parámetros,
#   - El primero: una tupla con el tamaño del laberinto (num_rows, num_cols)
#   - El segundo: el grafo del laberinto.
# - Devuelve una tupla con tres elementos. Por orden:
#    - Una tupla (row, col) con la posición donde colocar el tesoro.
#    - Una lista de vértices con el camino desde la entrada hasta el tesoro.
#    - Una lista de vértices con el camino desde el tesoro hasta la salida.
def process(size: Pair, lab: UndirectedGraph) -> Tuple[Pair, Path, Path]:
    pass


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
    pass


# -----------------------------------------------------


if __name__ == '__main__':
    size, lab = read_data(sys.stdin)
    pos, path1, path2 = process(size, lab)
    show_results(pos, path1, path2)
