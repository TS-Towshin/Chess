def knight(state: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:   # WARNING: Too inefficient, needs refactoring
    '''
    Calculate all the possible moves for a given knight
    '''
    x, y = pos
    moves = []
    color = state[y][x][0]

    for j in range(len(state)):
        for i in range(len(state[0])):
            del_x = abs(x-i)
            del_y = abs(y-j)
            if del_x+del_y != 3 or del_x*del_y == 0:
                continue
            if state[j][i][0] == color:
                continue
            moves.append((i, j))
    return moves

def rook(state: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]: # Just a prototype, needs refactoring
    '''
    Calculate all the possible moves for a given rook
    '''
    x, y = pos
    moves = []
    color = state[y][x][0]

    i = j = 1
    direction = 0
    while True:
        match direction:
            case 0:
                if x+i < len(state[0]):
                    if state[y][x+i] == '_':
                        moves.append((x+i, y))
                    elif state[y][x+i][0] != color:
                        moves.append((x+i, y))
                        direction += 1
                        i = 0
                    else:
                        direction += 1
                        i = 0
                else:
                    direction += 1
                    i = 0
                i += 1
            case 1:
                if y+j < len(state):
                    if state[y+j][x] == '_':
                        moves.append((x, y+j))
                    elif state[y+j][x][0] != color:
                        moves.append((x, y+j))
                        direction += 1
                        j = 0
                    else:
                        direction += 1
                        j = 0
                else:
                    direction += 1
                    j = 0
                j += 1
            case 2:
                if x-i >= 0:
                    if state[y][x-i] == '_':
                        moves.append((x-i, y))
                    elif state[y][x-i][0] != color:
                        moves.append((x-i, y))
                        direction += 1
                    else:
                        direction += 1
                else:
                    direction += 1
                i += 1
            case 3:
                if y-j >= 0:
                    if y-j < 0:
                        break
                    if state[y-j][x] == '_':
                        moves.append((x, y-j))
                    elif state[y-j][x][0] != color:
                        moves.append((x, y-j))
                        direction += 1
                    else:
                        direction += 1
                else:
                    direction += 1
                j += 1
            case 4:
                break

    return moves

def bishop(state: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]: # Just a prototype, needs refactoring
    '''
    Calculate all the possible moves for a given bishop
    '''
    x, y = pos
    moves = []
    color = state[y][x][0]
    row, col = len(state), len(state[0])

    i = j = 1
    direction = 0
    while True:
        match direction:
            case 0:
                if x+i < col and y+j < row:
                    if state[y+j][x+i] == '_':
                        moves.append((x+i, y+j))
                    elif state[y+j][x+i][0] != color:
                        moves.append((x+i, y+j))
                        direction += 1
                        i = j = 0
                    else:
                        direction += 1
                        i = j = 0
                else:
                    direction += 1
                    i = j = 0
                i += 1
                j += 1
            case 1:
                if y+j < row and x-i >= 0:
                    if state[y+j][x-i] == '_':
                        moves.append((x-i, y+j))
                    elif state[y+j][x-i][0] != color:
                        moves.append((x-i, y+j))
                        direction += 1
                        i = j = 0
                    else:
                        direction += 1
                        i = j = 0
                else:
                    direction += 1
                    i = j = 0
                i += 1
                j += 1
            case 2:
                if x-i >= 0 and row >= 0:
                    if state[y-j][x-i] == '_':
                        moves.append((x-i, y-j))
                    elif state[y-j][x-i][0] != color:
                        moves.append((x-i, y-j))
                        direction += 1
                        i = j = 0
                    else:
                        direction += 1
                        i = j = 0
                else:
                    direction += 1
                    i = j = 0
                i += 1
                j += 1
            case 3:
                if y-j >= 0 and x+i < col:
                    if y-j < 0:
                        break
                    if state[y-j][x+i] == '_':
                        moves.append((x+i, y-j))
                    elif state[y-j][x+i][0] != color:
                        moves.append((x+i, y-j))
                        direction += 1
                        i = j = 0
                    else:
                        direction += 1
                        i = j = 0
                else:
                    direction += 1
                    i = j = 0
                i += 1
                j += 1
            case 4:
                break

    return moves

def queen(state: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    '''
    Calculate all the possible moves for a given queen
    '''
    straight = rook(state, pos)
    diagonal = bishop(state, pos)
    moves = straight + diagonal
    return moves

def king(state: list[list[str]], pos: tuple[int, int], checks: list[tuple[int, int]] = []) -> list[tuple[int, int]]:
    '''
    Calculate all the possible moves for a given king
    '''
    moves = []
    for del_x in range(-1, 2):
        for del_y in range(-1, 2):
            if del_x == del_y == 0:
                continue
            x, y = del_x+pos[0], del_y+pos[1]
            if x < 0 or y < 0 or x >= len(state[0]) or y >= len(state):
                continue
            if state[y][x] != '_':
                if state[y][x][0] == state[pos[1]][pos[0]][0]:
                    continue
                else:
                    if (x, y) not in checks:
                        moves.append((x, y))
            else:
                if (x, y) not in checks:
                    moves.append((x, y))
    return moves

def pawn(state: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    '''
    Calculate all the possible moves for a given pawn
    '''
    x, y = pos
    moves = []
    color = state[y][x][0]
    for del_y in range(1, 3):
        match(state[y][x][0]):
            case 'w':
                if y-del_y < 0:
                    break
                elif state[y-del_y][x] == '_':
                    moves.append((x, y-del_y))
                    if y != 6:      # Check if the pawn is in the 7th rank
                        break
                else:
                    break
            case 'b':
                if y+del_y >= len(state):
                    break
                elif state[y+del_y][x] == '_':
                    moves.append((x, y+del_y))
                    if y != 1:      # Check if the pawn is in the 2nd rank
                        break
                else:
                    break
    match(color):
        case 'w':
            if y <= 0:
                return moves
            if x > 0:
                if state[y-1][x-1][0] == 'b':
                    moves.append((x-1, y-1))
            if x < len(state)-1:
                if state[y-1][x+1][0] == 'b':
                        moves.append((x+1, y-1))
        case 'b':
            if y >= len(state)-1:
                return moves
            if x > 0:
                if state[y+1][x-1][0] == 'w':
                    moves.append((x-1, y+1))
            if x < len(state)-1:
                if state[y+1][x+1][0] == 'w':
                        moves.append((x+1, y+1))
    return moves

def calculate_moves(state: list[list[str]], pos: tuple[int, int]) -> list[tuple[int, int]]:
    '''
    Return all possible moves for a given piece. First element of list will always be the position of the selected piece
    '''
    x, y = pos
    if state[y][x] == '_':
        return []
    piece = state[y][x][1]
    if piece == 'N':
        moves = knight(state, pos)
    elif piece == 'R':
        moves = rook(state, pos)
    elif piece == 'B':
        moves = bishop(state, pos)
    elif piece == 'Q':
        moves = queen(state, pos)
    elif piece == 'K':
        moves = king(state, pos)
    elif piece == 'P':
        moves = pawn(state, pos)
    else:
        return []
    moves.insert(0, pos)    # First element of the list represents the current position
    return moves

def is_valid(moves, destination):
    if len(moves) == 0:
        return False
    if destination in moves[1::]:
        return True
    return False

def right_turn(history: list, cell: str) -> bool:
    if cell == '_':
        return False
    elif len(history)%2 == 0 and cell[0] == 'w':
        return True
    elif len(history)%2 == 1 and cell[0] == 'b':
        return True
    return False

# def inCheck(state: list[list[str]], attacks: list[tuple[int, int]]):


def record_history(state: list[list[str]], history: list, moves, destination: tuple[int, int]):
    if is_valid(moves, destination):
        origin = moves[0]
        x, y = origin
        des_x, des_y = destination
        history.append([origin, destination, state[y][x], state[des_y][des_x]])
    return history

def undo(state: list[list[str]], history: list):
    if len(history) <= 0:
        return state
    origin, destination, current_piece, captured_piece = history[-1]
    x, y = origin
    des_x, des_y = destination
    state[y][x] = current_piece
    state[des_y][des_x] = captured_piece
    return state

def register_move(state: list[list[str]], moves: list[tuple[int, int]], destination: tuple[int, int]):
    '''
    Register the given move
    '''
    cur_x, cur_y = moves[0]
    if is_valid(moves, destination):
        x, y = destination
        moved_piece = state[cur_y][cur_x]
        if moved_piece[1] == 'K' or moved_piece[1] == 'R':
            moved_piece = moved_piece.replace('t', 'f')
        state[y][x] = moved_piece
        state[cur_y][cur_x] = '_'
    return state
