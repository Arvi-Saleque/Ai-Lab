
import math

# ===================
# S0 : Initial State 
# ===================

def S0():
    return [[' ' for _ in range(3)] for _ in range(3)]

winlist = [
        ((0,0),(0,1),(0,2)),
        ((1,0),(1,1),(1,2)),
        ((2,0),(2,1),(2,2)),
        ((0,0),(1,0),(2,0)),
        ((0,1),(1,1),(2,1)),
        ((0,2),(1,2),(2,2)),
        ((0,0),(1,1),(2,2)),
        ((0,2),(1,1),(2,0))
    ]

def win(state):
    for i, j, k in winlist:
        if state[i[0]][i[1]] == state[j[0]][j[1]] == state[k[0]][k[1]] and state[i[0]][i[1]] != ' ':  # and state[i[0]][i[1]] != ' '
            return state[i[0]][i[1]]
    return 'c' 

# ========
# DISPLAY 
# =======

def display(state):
    print("\n".join(" | ".join(row) for row in state))
    print("-" * 5)

# =============
# PLAYER(state)
# =============
# Return whose turn it is: 'X' or 'O'

def PLAYER(state):
    cntx, cnto = 0, 0
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == 'X':
                cntx += 1
            elif state[i][j] == 'O':   # elif state[i][j] == 'O'
                cnto += 1
    if cntx == cnto: 
        return 'X'
    else:
        return 'O'

# ==============
# ACTIONS(state)
# ==============
# Return a list of all valid (row, col) moves

def ACTIONS(state):
    
    list = []

    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == ' ':
                list.append((i, j))

    return list

# =====================
# RESULT(state, action)
# =====================
# Return a new state after applying action

def RESULT(state, action):

    mark = PLAYER(state)

    newstate = [row[:] for row in state] # newstate = [row[:] for row in state]
    
    newstate[action[0]][action[1]] = mark

    return newstate
    


# ===============
# TERMINAL(state)
# ===============
# Return True if the game is over

def TERMINAL(state):
    if win(state) == 'X' or win(state) == 'O':
        return True
    
    for i in range(0, 3):
        for j in range(0, 3):
            if state[i][j] == ' ':
                return False
            
    return True

# ==============
# UTILITY(state)
# ==============
# Return:
#   1  if X wins
#  -1  if O wins
#   0  otherwise

def UTILITY(state):
    

    if win(state) == 'X':
        return 1
    elif win(state) == 'O':
        return -1   
    else:
        return 0



# =======================
# MINIMAX VALUE FUNCTIONS
# =======================

def MAX_VALUE(state):
    if TERMINAL(state):
        return UTILITY(state), None

    moves = ACTIONS(state)

    mx = -math.inf
    pp = None

    for action in moves:
        newstate = RESULT(state, action)

        # call MIN_VALUE only ONCE
        val, _ = MIN_VALUE(newstate)

        if val > mx:
            mx = val
            pp = action

    return mx, pp


def MIN_VALUE(state):
    if TERMINAL(state):
        return UTILITY(state), None

    moves = ACTIONS(state)

    mn = math.inf
    pp = None

    for action in moves:
        newstate = RESULT(state, action)

        # call MAX_VALUE only ONCE
        val, _ = MAX_VALUE(newstate)

        if val < mn:
            mn = val
            pp = action

    return mn, pp


def MINIMAX(state):
    # If player is X → maximize, If player is O → minimize
    if PLAYER(state) == 'X':
        return MAX_VALUE(state)[1]
    else:
        return MIN_VALUE(state)[1]


# =========
# GAME LOOP
# =========

def play():
    state = S0()
    print("Welcome to Tic-Tac-Toe")
    print("You are O, AI is X\n")

    display(state)

    while not TERMINAL(state):
        if PLAYER(state) == 'O':
            row, col = map(int, input("Enter row and column (0-2): ").split())
            if (row, col) not in ACTIONS(state):
                print("Invalid move. Try again.")
                continue
            state = RESULT(state, (row, col))
        else:
            action = MINIMAX(state)
            print(f"AI plays: {action}")
            state = RESULT(state, action)

        display(state)

    score = UTILITY(state)
    if score == 1:
        print("X wins!")
    elif score == -1:
        print("O wins!")
    else:
        print("Draw!")

# ====
# MAIN
# ====

if __name__ == "__main__":
    play()
