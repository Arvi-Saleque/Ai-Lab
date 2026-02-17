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
            if b[r][c] != 0:
                dom[(r, c)] = {b[r][c]}
            else:
                tmp: Set[int] = set()
                for i in range(1, 10):
                    if is_valid(b, r, c, i):
                        tmp.add(i)
                dom[(r, c)] = tmp

    return dom

def get_mrv(b : Board, dom : Domains) -> Optional[Cell]:
    best_cell:Cell = None
    best = 10
    for r in range(9):
        for c in range(9):
            if b[r][c] != 0:
                continue
            dlen = len(dom[(r, c)])
            if dlen == 0:
                return (r, c)
            if dlen < best:
                best = dlen
                best_cell = (r, c)
            if best == 1:
                return best_cell
    return best_cell

def forward_check(b : Board, dom : Domains, cell : Cell, val : int) -> Domains:
    new_dom: Domains = {k: set(v) for k, v in dom.items()}

    row, col = cell

    for c in range(9):
        if c != col and b[row][c] == 0 and val in new_dom[(row, c)]:
            new_dom[(row, c)].remove(val)
            if len(new_dom[(row, c)]) == 0:
                return None
            
    for r in range(9):
        if r != row and b[r][col] == 0 and val in new_dom[(r, col)]:
            new_dom[(r, col)].remove(val)
            if len(new_dom[(r, col)]) == 0:
                return None
            
    box_r = (row // 3) * 3
    box_c = (col // 3) * 3
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if (r, c) != (row, col) and b[r][c] == 0 and val in new_dom[(r, c)]:
                new_dom[(r, c)].remove(val)
                if len(new_dom[(r, c)]) == 0:
                    return None
    
    new_dom[(row, col)] = {val}
    
    return new_dom
                    


def backtrack(b : Board, dom : Domains) -> bool:
    cc = get_mrv(b, dom)
    if cc is None:
        return True
    r, c = cc

    if len(dom[cc]) == 0:
        return False
    
    for val in sorted(dom[cc]):
        new_dom = forward_check(b, dom, cc, val)
        if new_dom is not None:
            b[r][c] = val
            if backtrack(b, new_dom):
                return True
            b[r][c] = 0

    return False

def solve(b : Board) -> bool:
    dom = build_domains(b)
    return backtrack(b, dom)


def print_board(board: Board) -> None:
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            print(board[r][c], end=" ")
        print()


if __name__ == "__main__":
    board: Board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Before:")
    print_board(board)

    if solve(board):
        print("\nSolved (CSP):")
        print_board(board)
    else:
        print("\nNo solution exists.")