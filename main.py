import platform
import pygame
from src import board, pieces
from src.engine import calculate_moves, register_move, record_history, right_turn, undo


pygame.init()

WIDTH, HEIGHT = 560, 560
scale_x, scale_y = WIDTH/8, HEIGHT/8

if platform.system() == "Windows":
    img_src = "src\\images\\chess-icon.png"
else:
    img_src = "src/images/chess-icon.png"

icon = pygame.image.load(img_src)
print(platform.system())

pygame.display.set_caption("Chess")
pygame.display.set_icon(icon)
screen = pygame.display.set_mode((WIDTH, HEIGHT))

clock = pygame.time.Clock()

state = board.init()

board.draw(screen)
pieces.draw_pieces(screen, state)
running = True
mouse_button = False
moves = []
history = []
registered = False
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                state = undo(state, history)
                if len(history) > 0:
                    history.pop()
        if event.type == pygame.MOUSEBUTTONDOWN:
            pos = pygame.mouse.get_pos()
            col = int(pos[0]/scale_x)
            row = int(pos[1]/scale_y)
            mouse_button = True
            pos = col, row
            if right_turn(history, state[row][col]):
                moves = calculate_moves(state, pos)

    board.draw(screen)
    pieces.draw_pieces(screen, state)
    pieces.show_moves(screen, state, moves)
    if mouse_button:
        if len(moves) == 0:
            mouse_button = False
            continue
        x, y = moves[0]
        if state[row][col][0] != state[y][x][0]:
            history = record_history(state, history, moves, pos)
            state = register_move(state, moves, pos)
            moves = []
            registered = True
        mouse_button = False

    pygame.display.update()

    clock.tick(25)