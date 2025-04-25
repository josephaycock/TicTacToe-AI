import pygame

# Screen setup
WIDTH, HEIGHT = 600, 600
SQUARE_SIZE = WIDTH // 3

# Colors
BG_COLOR = (255, 87, 51)       # #FF5733
LINE_COLOR = (255, 195, 15)    # #FFC30F
CIRCLE_COLOR = LINE_COLOR      # O
CROSS_COLOR = (255, 255, 255)  # X
BUTTON_COLOR = LINE_COLOR
BUTTON_HOVER = (255, 215, 40)
TEXT_COLOR = LINE_COLOR

# Fonts (larger + bold)
pygame.font.init()
FONT = pygame.font.SysFont(None, 70, bold=True)       # Increased size
SMALL_FONT = pygame.font.SysFont(None, 45, bold=True) # Increased size

# Sizes (bold X/O strokes)
LINE_WIDTH = 15
CIRCLE_RADIUS = SQUARE_SIZE // 3
CIRCLE_WIDTH = 18
CROSS_WIDTH = 28
SPACE = SQUARE_SIZE // 4