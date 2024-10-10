import pygame
import sys

# Initialize Pygame
pygame.init()

# Set display dimensions
width, height = 300, 300
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Tic-Tac-Toe')

# Colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (213, 50, 80)

# Game settings
board = [' ' for _ in range(9)]
current_player = 'X'

def draw_board():
    display.fill(white)
    for i in range(1, 3):
        pygame.draw.line(display, black, (0, i * 100), (width, i * 100), 2)
        pygame.draw.line(display, black, (i * 100, 0), (i * 100, height), 2)

    for i in range(9):
        if board[i] == 'X':
            pygame.draw.line(display, red, (i % 3 * 100 + 20, i // 3 * 100 + 20), (i % 3 * 100 + 80, i // 3 * 100 + 80), 2)
            pygame.draw.line(display, red, (i % 3 * 100 + 80, i // 3 * 100 + 20), (i % 3 * 100 + 20, i // 3 * 100 + 80), 2)
        elif board[i] == 'O':
            pygame.draw.circle(display, black, (i % 3 * 100 + 50, i // 3 * 100 + 50), 40, 2)

def check_winner():
    winning_combinations = [(0, 1, 2), (3, 4, 5), (6, 7, 8),
                            (0, 3, 6), (1, 4, 7), (2, 5, 8),
                            (0, 4, 8), (2, 4, 6)]
    for combo in winning_combinations:
        if board[combo[0]] == board[combo[1]] == board[combo[2]] != ' ':
            return board[combo[0]]
    return None

def is_draw():
    return ' ' not in board

def game_loop():
    global current_player
    while True:
        draw_board()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                index = (y // 100) * 3 + (x // 100)
                if board[index] == ' ':
                    board[index] = current_player
                    winner = check_winner()
                    if winner:
                        print(f"{winner} wins!")
                        pygame.quit()
                        sys.exit()
                    if is_draw():
                        print("Game is a draw!")
                        pygame.quit()
                        sys.exit()
                    current_player = 'O' if current_player == 'X' else 'X'
        
        pygame.display.flip()

game_loop()
