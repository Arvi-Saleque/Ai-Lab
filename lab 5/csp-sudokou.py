from typing import List, Optional, Tuple, Dict, Set

Board = List[List[int]]
Cell = Tuple[int, int]
Domains = Dict[Cell, Set[int]]

def is_valid(b : Board, row : int, col : int, val : int) -> bool:
    for c in range(9):
        if c != col and b[row][c] == val:
            return False
        
    for r in range(9):
        if r != row and b[r][col] == val:
            return False
        
    box_r = (row // 3) * 3
    box_c = (col // 3) * 3

    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if (r, c) != (row, col) and b[r][c] == val:
                return False

    return True



def build_domains(b : Board) -> Domains:
    dom:Domains = {}

    for r in range(9):
        for c in range(9):
            tmp: Set = {}
            for i in range(1, 10):
                if is_valid(b, r, c, i):
                    tmp.add(i)
            dom[(r, c)] = tmp

    return dom

def get_mrv(b : Board, dom : Domains) -> Cell:
    c:Cell = {}
    len = 10
    for r in range(9):
        for c in range(9):
            if len(dom[(r, c)] )




def backtrack(b : Board, dom : Domains) -> bool:
    r, c = get_mrv(b. dom)


def solve(b : Board):
    dom = build_domains(b)
    backtrack(b, dom)

