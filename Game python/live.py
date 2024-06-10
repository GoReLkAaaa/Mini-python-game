import pygame
import numpy as np

pygame.init()
width, height = 800, 700
cols, rows = 200, 200
cell_width = width / cols
cell_height = height / cols
BLACK = (0, 0, 0)
WHITE = (57, 255, 20)
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('Игра в жизнь')
grid = np.random.choice([0, 1], size=(rows, cols))


def update_grid(grid):
    new_grid = np.copy(grid)
    for x in range(cols):
        for y in range(rows):
            neighbors = (grid[(x-1) % cols, (y-1) % rows]
                + grid[(x) % cols, (y-1) % rows]
                + grid[(x+1) % cols, (y-1) % rows]
                + grid[(x-1) % cols, (y) % rows]
                + grid[(x+1) % cols, (y) % rows]
                + grid[(x-1) % cols, (y+1) % rows]
                + grid[(x) % cols, (y+1) % rows]
                + grid[(x+1) % cols, (y+1) % rows])
            if grid[x, y] == 1 and (neighbors < 2 or neighbors > 3):
                new_grid[x, y] = 0
            elif grid[x, y] == 0 and neighbors == 3:
                new_grid[x, y] = 1
    return new_grid
running = True
while running:
    screen.fill(WHITE)
    for x in range(cols):
        for y in range(rows):
            if grid [x, y] == 1:
                pygame.draw.rect(screen, BLACK, (x * cell_width, y * cell_height, cell_width, cell_height))
    grid = update_grid(grid)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.flip()
pygame.quit()

