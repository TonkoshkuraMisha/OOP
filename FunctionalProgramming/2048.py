"""Инициализация и настройки: В начале кода инициализируются Pygame и задаются основные константы, такие как размер
игрового поля, размеры плиток, цвета и шрифты. Функции рисования и обновления: Функция draw_board отвечает за
отображение игрового поля и плиток. Она заполняет фон и рисует каждую плитку с соответствующим цветом и значением.
Функции движения и объединения: move_left, merge_left и rotate_board обрабатывают логику движения и объединения
плиток. move отвечает за поворот доски и перемещение в нужном направлении. Главная функция: В main происходит
основной цикл игры, где обрабатываются события (нажатия клавиш) и обновляется состояние игры."""

import pygame
import sys
import random

# Инициализация Pygame
pygame.init()

# Константы
SIZE = 4
WIDTH = 400
HEIGHT = 400
TILE_SIZE = WIDTH // SIZE
FONT_SIZE = 40
BACKGROUND_COLOR = (187, 173, 160)
TILE_COLORS = {
    0: (205, 193, 180),
    2: (238, 228, 218),
    4: (237, 224, 200),
    8: (242, 177, 121),
    16: (245, 149, 99),
    32: (246, 124, 95),
    64: (246, 94, 59),
    128: (237, 207, 114),
    256: (237, 204, 97),
    512: (237, 200, 80),
    1024: (237, 197, 63),
    2048: (237, 194, 46)
}
FONT_COLOR = (119, 110, 101)

# Инициализация окна
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('2048')
font = pygame.font.Font(None, FONT_SIZE)


def draw_board(board):
    screen.fill(BACKGROUND_COLOR)
    for row in range(SIZE):
        for col in range(SIZE):
            value = board[row][col]
            color = TILE_COLORS.get(value, (60, 58, 50))
            rect = pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE)
            pygame.draw.rect(screen, color, rect)
            if value != 0:
                text = font.render(str(value), True, FONT_COLOR)
                text_rect = text.get_rect(center=rect.center)
                screen.blit(text, text_rect)
    pygame.display.update()


def add_new_tile(board):
    empty_tiles = [(r, c) for r in range(SIZE) for c in range(SIZE) if board[r][c] == 0]
    if empty_tiles:
        row, col = random.choice(empty_tiles)
        board[row][col] = 2 if random.random() < 0.9 else 4


def move_left(board):
    new_board = [[0] * SIZE for _ in range(SIZE)]
    for row in range(SIZE):
        col_pos = 0
        for col in range(SIZE):
            if board[row][col] != 0:
                new_board[row][col_pos] = board[row][col]
                col_pos += 1
    return new_board


def merge_left(board):
    for row in range(SIZE):
        for col in range(SIZE - 1):
            if board[row][col] != 0 and board[row][col] == board[row][col + 1]:
                board[row][col] *= 2
                board[row][col + 1] = 0
    return board


def rotate_board(board):
    return [list(row) for row in zip(*board[::-1])]


def move(board, direction):
    for _ in range(direction):
        board = rotate_board(board)
    board = move_left(board)
    board = merge_left(board)
    board = move_left(board)
    for _ in range(-direction % 4):
        board = rotate_board(board)
    return board


def main():
    board = [[0] * SIZE for _ in range(SIZE)]
    add_new_tile(board)
    add_new_tile(board)

    while True:
        draw_board(board)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    board = move(board, 0)
                elif event.key == pygame.K_UP:
                    board = move(board, 1)
                elif event.key == pygame.K_RIGHT:
                    board = move(board, 2)
                elif event.key == pygame.K_DOWN:
                    board = move(board, 3)
                add_new_tile(board)
                draw_board(board)


if __name__ == '__main__':
    main()
