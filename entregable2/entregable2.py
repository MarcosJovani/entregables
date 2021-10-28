import sys
from typing import *


# Entrada: El descriptor de fichero. Podemos leer una línea de texto con f.readline().
#          El formato de la entrada se especifica en el apartado 2.1.
# Salida: Una lista de booleanos con True si la moneda está cara arriba (‘o’) o
#         False si está cara abajo (‘x’).
def read_data(f) -> List[bool]:
    stack = []
    for elem in list(f.readline()):
        if elem == 'o':
            stack.append(True)
        else:
            stack.append(False)
    return stack

# Entrada: Un parámetro, el mismo que devuelve la función read_data.
# Salida: Lista de enteros con las instrucciones para el robot.
def process(stack: List[bool]) -> List[int]:
    res = []
    if len(stack) != 0:
        referencia = stack.pop(0)
        cont = 1
        for siguiente in stack:
            if siguiente != referencia:
                res.append(cont)
                referencia = siguiente
            cont += 1
        if referencia == False:
            res.append(cont)
    return res


# Entrada: Un parámetro, el mismo que devuelve la función process.
# Salida: No devuelve nada. Solo muestra líneas de texto por la salida estándar
#         siguiendo el formato que se detalla en el apartado 2.2.
def show_results(solution: List[int]):
    for r in solution:
        print(r)


if __name__ == '__main__':
    my_stack = read_data(sys.stdin)
    my_solution = process(my_stack)
    show_results(my_solution)
