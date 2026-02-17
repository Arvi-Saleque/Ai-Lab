from typing import List, Optional, Tuple 

Board = List[List[int]]

def find_empty(board : Board) -> Optional[Tuple[int, int]]:
    for r in range(9):
        for c in range(9):
            if(board[r][c] == 0):
                return (r, c)
            
    return None
            

def is_valid(board: Board, row : int, col : int, val : int) -> bool:
    for c in range(9):
        if(board[row][c] == val):
            return False
    
    for r in range(9):
        if(board[r][col] == val): 
            return False
        

    box_r = (row // 3) * 3
    box_c = (col // 3) * 3

    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if(board[r][c] == val):
                return False
            
    return True


def solve(board : Board) -> bool:
    empty = find_empty(board)

    if(empty is None):
        return True
    
    row, col = empty

    for val in range(1, 10):
        if(is_valid(board, row, col, val)):
            board[row][col] = val
            if solve(board):
                return True
            
            board[row][col] = 0

    return False

def print_board(board: Board) -> None:
    for r in range(9):
        if r % 3 == 0 and r != 0:
            print("-" * 21)
        for c in range(9):
            if c % 3 == 0 and c != 0:
                print("|", end=" ")
            print(board[r][c], end=" ")
        print()

# Example usage:
if __name__ == "__main__":
    board = [
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
        print("\nSolved:")
        print_board(board)
    else:
        print("\nNo solution exists.")