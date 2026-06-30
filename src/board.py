import pygame

'''
Pawn = P
Knight = N
Bishop = B
Rook = R
Queen = Q
King = K
black = b
white = w
first move = t
not first move = f
'''

def init() -> list[list[str]]:
    state = [["_" for _ in range(8)] for _ in range(8)]
    state[0] = ["bRt", "bN", "bB", "bQ", "bKt", "bB", "bN", "bRt"]
    state[1] = [f"bP" for _ in range(8)]
    state[6] = [f"wP" for _ in range(8)]
    state[7] = ["wRt", "wN", "wB", "wQ", "wKt", "wB", "wN", "wRt"]
    return state


def draw(screen: pygame.Surface) -> None:
    white = '#eeeed5'
    black = '#7d945d'
 
    scale_x = screen.get_width()/8
    scale_y = screen.get_height()/8
    for row in range(8):
        for cell in range(8):
            if (row+cell)%2 == 0:
                color = white
            else:
                color = black
            x = scale_x*cell
            y = scale_y*row
            pygame.draw.rect(screen, color, (x, y, scale_x, scale_y))
