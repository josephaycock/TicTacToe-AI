import pygame
from constants import *

class Button:
    def __init__(self, text, x, y, w, h):
        self.rect = pygame.Rect(x, y, w, h)
        self.text = text

    def draw(self, screen):
        mx, my = pygame.mouse.get_pos()
        color = BUTTON_HOVER if self.rect.collidepoint(mx, my) else BUTTON_COLOR
        pygame.draw.rect(screen, color, self.rect, border_radius=10)
        label = SMALL_FONT.render(self.text, True, BG_COLOR)
        screen.blit(label, (self.rect.centerx - label.get_width()//2, self.rect.centery - label.get_height()//2))

    def clicked(self, event):
        return self.rect.collidepoint(event.pos)

def draw_board(screen, board):
    screen.fill(BG_COLOR)
    for i in range(1, 3):
        pygame.draw.line(screen, LINE_COLOR, (0, SQUARE_SIZE * i), (WIDTH, SQUARE_SIZE * i), LINE_WIDTH)
        pygame.draw.line(screen, LINE_COLOR, (SQUARE_SIZE * i, 0), (SQUARE_SIZE * i, HEIGHT), LINE_WIDTH)

    for row in range(3):
        for col in range(3):
            if board[row][col] == "O":
                pygame.draw.circle(screen, CIRCLE_COLOR, (col * SQUARE_SIZE + SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), CIRCLE_RADIUS, CIRCLE_WIDTH)
            elif board[row][col] == "X":
                start1 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SPACE)
                end1 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start1, end1, CROSS_WIDTH)
                start2 = (col * SQUARE_SIZE + SPACE, row * SQUARE_SIZE + SQUARE_SIZE - SPACE)
                end2 = (col * SQUARE_SIZE + SQUARE_SIZE - SPACE, row * SQUARE_SIZE + SPACE)
                pygame.draw.line(screen, CROSS_COLOR, start2, end2, CROSS_WIDTH)