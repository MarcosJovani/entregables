import sys
from typing import *
infinity = float('infinity')

Score = int                 # El tipo de las puntuaciones
Decision = int              # Un índice de globo
Decisions = List[Decision]  # Lista con los índices de los globos explotados

SParams = Tuple[int, int]
Mem = Dict[SParams, Score]
MemPath = Dict[SParams, Tuple[Score, SParams, Decision]]
# ------------------------------------------------------------

# Salida: Una tupla con dos listas de enteros: (alturas de los globos, puntuaciones de los globos)
def read_data(f) -> Tuple[List[int], List[int]]:
    heights = []
    scores = []
    for line in f.readlines():
        height, score = line[:-1].split(' ')
        heights.append(int(height))
        scores.append(int(score))
    return heights, scores

# Salida: Una tupla (puntuación, lista con los índices de los globos explotados)
def process(heights: List[int], scores: List[int]) -> Tuple[Score, Decisions]:
    def S(a: int, s: int) -> Score:
        if s == 0: return 0
        if(a, s) not in mem:
            mem[a, s] = (-infinity, (-1, -1) ,1)

        return mem[a,s][0]

    mem: Dict[SParams, Tuple[Score, SParams, Decision]] = {}
    score = S(len(heights), len(scores))
    a, s = len(heights), len(scores)
    decisions = []
    while s != 0:
        _, (a, s), d = mem[a, s]
        decisions.append(d)
    decisions.reverse()
    return score, decisions

def show_results(score: int, decisions: List[int]):
    print(score)
    for decision in decisions:
        print(decision, end=' ')

# ------------------------------------------------------------

if __name__ == '__main__':
    g_heights, g_scores = read_data(sys.stdin)
    g_score, g_decisions = process(g_heights, g_scores)
    show_results(g_score, g_decisions)
