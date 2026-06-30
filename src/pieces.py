import pygame

class Piece(pygame.sprite.Sprite):
    def __init__(self, path: str, type: str, coordinate: tuple[int, int], size: tuple[float, float]):
        super().__init__()
        self.image = pygame.image.load(path)
        self.image = pygame.transform.scale(self.image, size)
        self.rect = self.image.get_rect()
        self.rect.topleft = (coordinate[0]*int(size[0]), coordinate[1]*int(size[1]))

    def draw(self, screen: pygame.Surface) -> None:
        screen.blit(self.image, self.rect.topleft)
        pygame.display.update()


def draw_pieces(screen: pygame.Surface, state: list[list[str]]):
    pieces = pygame.sprite.Group()
    size = screen.get_width()/8, screen.get_height()/8
    for i, row in enumerate(state):
        for j, cell in enumerate(row):
            if cell[0:2] == 'bR':
                pieces.add(Piece("src/images/bR.png", cell, (j, i), size))
            elif cell == 'bN':
                pieces.add(Piece("src/images/bN.png", cell, (j, i), size))
            elif cell == 'bB':
                pieces.add(Piece("src/images/bB.png", cell, (j, i), size))
            elif cell == 'bQ':
                pieces.add(Piece("src/images/bQ.png", cell, (j, i), size))
            elif cell[0:2] == 'bK':
                pieces.add(Piece("src/images/bK.png", cell, (j, i), size))
            elif cell[0:2] == 'bP':
                pieces.add(Piece("src/images/bP.png", cell, (j, i), size))
            elif cell[0:2] == 'wR':
                pieces.add(Piece("src/images/wR.png", cell, (j, i), size))
            elif cell == 'wN':
                pieces.add(Piece("src/images/wN.png", cell, (j, i), size))
            elif cell == 'wB':
                pieces.add(Piece("src/images/wB.png", cell, (j, i), size))
            elif cell == 'wQ':
                pieces.add(Piece("src/images/wQ.png", cell, (j, i), size))
            elif cell[0:2] == 'wK':
                pieces.add(Piece("src/images/wK.png", cell, (j, i), size))
            elif cell[0:2] == 'wP':
                pieces.add(Piece("src/images/wP.png", cell, (j, i), size))
    pieces.draw(screen)
    return pieces

def show_moves(screen: pygame.Surface, state: list[list[str]], moves: list[tuple[int, int]]) -> None:
    WIDTH, HEIGHT = screen.get_width(), screen.get_height()
    scale_x, scale_y = WIDTH/8, HEIGHT/8
    for move in moves:
        color = 'skyblue'
        if len(moves) <= 0:
            break
        cell = state[move[1]][move[0]]
        if cell != '_' and move != moves[0]:
            color = 'red'
        if move == moves[0]:
            color = 'green'
        pygame.draw.rect(screen, color, (move[0]*scale_x, move[1]*scale_y, scale_x, scale_y), 3)
