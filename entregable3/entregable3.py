import sys
from typing import *
from dataclasses import dataclass

from bt_scheme import DecisionSequence, bt_vc_solve

# Tipos ----------------------------------------------------------------------

Board    = List[List[str]]  # Matriz como lista de listas, con un carácter por celda ['#', 'o', '.']
Pos      = Tuple[int, int]  # Posición en el tablero: (fila,col)
Step     = Tuple[Pos, Pos]  # Un movimiento del puzle
Solution = Tuple[Step,...]  # Tupla con los movimientos que resuelven el puzle


# Funciones principales ------------------------------------------------------

# Salida. Matriz como lista de listas, con un carácter por celda ['#', 'o', '.']
def read_data(f) -> Board:
    board = []
    for line in f.readlines():
        board.append(list(line[:-1]))       # -1 porque al final hay un caracter de salto de linea
    return board


# Salida. La solución como una tupla de Step (o None, si no hay solución).
def process(board: Board) -> Optional[Solution]:
    pass


def show_results(solution: Optional[Solution]):
    pass


# Programa principal ------------------------------------------------------

if __name__ == '__main__':
    board = read_data(sys.stdin)
    solution = process(board)
  #  show_results(solution)
