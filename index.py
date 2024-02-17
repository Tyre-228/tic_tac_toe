import pygame

# screen set up
WINDOW_WIDTH = 600
WINDOW_HEIGHT = 600

pygame.init()
pygame.font.init()
screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Tic tac toe")
clock = pygame.time.Clock()

# loading graphics
board_image = pygame.transform.scale(pygame.image.load("./graphics/board.png").subsurface(pygame.Rect(0, 0, 31, 31)), (600, 600))
cell_image = pygame.transform.scale(pygame.image.load("./graphics/cell.png").subsurface(pygame.Rect(0, 0, 11, 11)), (200, 200))
circle_image = pygame.transform.scale(pygame.image.load("./graphics/circle.png").subsurface(pygame.Rect(0, 0, 11, 11)), (100, 100))
cross_image = pygame.transform.scale(pygame.image.load("./graphics/cross.png").subsurface(pygame.Rect(0, 0, 13, 12)), (100, 100))

# grid
grid = [
    [" ", " ", " "],
    [" ", " ", " "],
    [" ", " ", " "],
]

def display_signs(grid):
    for row_index, row in enumerate(grid):
        for cell_index, cell in enumerate(row):
            screen.blit(cell_image, (cell_index*200, row_index*200))
            if cell == "X":
                screen.blit(cross_image, (cell_index*200+51, row_index*200+51))
            elif cell == "O":
                screen.blit(circle_image, (cell_index*200+51, row_index*200+51))

def change_grid(grid, x, y):
    global sign
    clicked_cell = grid[y//200][x//200]
    if clicked_cell == " ":
        grid[y//200][x//200] = sign
        if sign == "X":
                sign = "O"
        else:
            sign = "X"

def is_grid_full(grid):
    for row in grid:
        for cell in row:
            if cell == " ":
                return False
    return True

def win_condition_checker(grid, sign):
    if grid[0][0] == sign and grid[0][1] == sign and grid[0][2] == sign:
        return True
    elif grid[1][0] == sign and grid[1][1] == sign and grid[1][2] == sign:
        return True
    elif grid[2][0] == sign and grid[2][1] == sign and grid[2][2] == sign:
        return True
    elif grid[0][0] == sign and grid[1][0] == sign and grid[2][0] == sign:
        return True
    elif grid[0][1] == sign and grid[1][1] == sign and grid[2][1] == sign:
        return True
    elif grid[0][2] == sign and grid[1][2] == sign and grid[2][2] == sign:
        return True
    elif grid[0][0] == sign and grid[1][1] == sign and grid[2][2] == sign:
        return True
    elif grid[2][0] == sign and grid[1][1] == sign and grid[0][2] == sign:
        return True
    return False

# game loop
running = True
sign = "X"
font = pygame.font.Font(None, 48)
message_surface = ""

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEBUTTONDOWN and message_surface == "":
            x, y = pygame.mouse.get_pos()
            change_grid(grid, x, y)
            if win_condition_checker(grid, "X") == True:
                message_surface = font.render("Player X has won", True, (250, 0, 0))
            elif win_condition_checker(grid, "O") == True:
                message_surface = font.render("Player O has won", True, (0, 250, 0))
            elif is_grid_full(grid):
                message_surface = font.render("Draw!", True, (255, 191, 0))
    display_signs(grid)
    if message_surface != "":
        screen.blit(message_surface, (WINDOW_WIDTH//2 - message_surface.get_width()//2, WINDOW_HEIGHT//2 - message_surface.get_height()//2))
            
    # screen.blit(board_image, (0, 0))
    pygame.display.flip()
    clock.tick(60)