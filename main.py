import pygame
import sys
from constants import *
from game import GameManager
from ui import Button, draw_board
from ai import RandomAI, MediumAI, MinimaxAI

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe AI")

start_btn = Button("Start Game", WIDTH//2 - 100, HEIGHT - 100, 200, 70)
easy_btn = Button("Easy", WIDTH//2 - 100, HEIGHT//2 - 120, 200, 70)
med_btn = Button("Medium", WIDTH//2 - 100, HEIGHT//2     , 200, 70)
hard_btn = Button("Hard", WIDTH//2 - 100, HEIGHT//2 + 120, 200, 70)
play_again_btn = Button("Play Again", WIDTH//2 - 100, HEIGHT//2 +  60, 200, 70)
change_diff_btn = Button("Change Difficulty", WIDTH//2 - 150, HEIGHT//2 + 140, 300, 70)
state = "menu"
game = GameManager()

while True:
    screen.fill(BG_COLOR)

    if state == "menu":
        title_lines = ["tic", "tac", "toe"]
        for idx, word in enumerate(title_lines):
            word_render = FONT.render(word, True, TEXT_COLOR)
            
            screen.blit(word_render, (WIDTH // 2 - word_render.get_width() // 2, 100 + idx * 100))
        start_btn.draw(screen)

    elif state == "difficulty":
        title = FONT.render("Select Difficulty", True, TEXT_COLOR)
        screen.blit(
            title,
            (WIDTH//2 - title.get_width()//2, HEIGHT//2 -250)
        )
        easy_btn.draw(screen)
        med_btn.draw(screen)
        hard_btn.draw(screen)

    elif state == "playing":
        draw_board(screen, game.board.board)
        if game.over:
            state = "end"

    elif state == "end":
        msg_lines = ["it's a", "draw!"] if game.winner == "Draw" else [f"{game.winner}", "wins!"]
        for idx, word in enumerate(msg_lines):
            msg_render = FONT.render(word, True, TEXT_COLOR)
            
            screen.blit(msg_render, (WIDTH // 2 - msg_render.get_width() // 2, 100 + idx * 100))
        play_again_btn.draw(screen)
        change_diff_btn.draw(screen)

    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if state == "menu" and event.type == pygame.MOUSEBUTTONDOWN:
            if start_btn.clicked(event):
                game.reset()
                state = "difficulty"

        elif state == "difficulty" and event.type == pygame.MOUSEBUTTONDOWN:
            if easy_btn.clicked(event):
                game.ai = RandomAI()
            elif med_btn.clicked(event):
                game.ai = MediumAI()
            elif hard_btn.clicked(event):
                game.ai = MinimaxAI()
            else:
                continue
            game.reset()
            state = "playing"

        elif state == "playing" and event.type == pygame.MOUSEBUTTONDOWN and not game.over:
            x, y = event.pos[0] // SQUARE_SIZE, event.pos[1] // SQUARE_SIZE
            game.make_move(y, x)

        elif state == "end" and event.type == pygame.MOUSEBUTTONDOWN:
            if play_again_btn.clicked(event):
                game.reset()
                state = "playing"
            elif change_diff_btn.clicked(event):
                game.reset()
                state = "difficulty"