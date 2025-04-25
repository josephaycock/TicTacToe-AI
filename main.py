import pygame
import sys
from constants import *
from game import GameManager
from ui import Button, draw_board

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")

start_btn = Button("Start Game", WIDTH//2 - 100, HEIGHT - 100, 200, 70)
play_again_btn = Button("Play Again", WIDTH//2 - 100, HEIGHT - 100, 200, 70)
state = "menu"
game = GameManager()

while True:
    screen.fill(BG_COLOR)

    if state == "menu":
        title_lines = ["tic", "tac", "toe"]
        for idx, word in enumerate(title_lines):
            word_render = FONT.render(word, True, TEXT_COLOR)
            # Spacing adjusted for bigger font
            screen.blit(word_render, (WIDTH // 2 - word_render.get_width() // 2, 100 + idx * 100))
        start_btn.draw(screen)

    elif state == "playing":
        draw_board(screen, game.board.board)
        if game.over:
            state = "end"

    elif state == "end":
        msg_lines = ["it's a", "draw!"] if game.winner == "Draw" else [f"{game.winner}", "wins!"]
        for idx, word in enumerate(msg_lines):
            msg_render = FONT.render(word, True, TEXT_COLOR)
            # Spacing adjusted for bigger font
            screen.blit(msg_render, (WIDTH // 2 - msg_render.get_width() // 2, 100 + idx * 100))
        play_again_btn.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.clicked(event):
                game.reset()
                state = "playing"

        elif state == "playing" and event.type == pygame.MOUSEBUTTONDOWN and not game.over:
            x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
            game.make_move(y, x)

        elif state == "end" and event.type == pygame.MOUSEBUTTONDOWN:
            if play_again_btn.clicked(event):
                game.reset()
                state = "playing"