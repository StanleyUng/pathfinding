import pygame
from node import *
from point import Point


 
# COLORS
EMPTY_COLOR = (255, 255, 255)
DESTINATION = (255, 255, 0) # Yellow
WALL_COLOR = (0, 0, 0) # Black
BACKGROUND_COLOR = (100, 100, 100)

PINK = (255, 102, 255)
BLUE = (102, 255, 255)
PATH_COLOR = (255, 255, 0) # Yellow

# SIZES
# This sets the WIDTH and HEIGHT of each grid location
WIDTH = 20
HEIGHT = 20
 
# This sets the margin between each cell
MARGIN = 5


GRID_SIZE = 20
# Set the HEIGHT and WIDTH of the screen
WINDOW_SIZE = [505, 505]

# Key points

# Loop until the user clicks the close button.
done = False

# A star pathfinding
openlist = []
closedlist = []
 
# Create a 2 dimensional array. A two dimensional
# array is simply a list of lists.
grid = []
for row in range(GRID_SIZE):
    # Add an empty array that will hold each cell
    # in this row
    grid.append([])
    for col in range(GRID_SIZE):
        # grid[row].append(0)  # Append a cell
        grid[row].append(Node(True, Point(row, col)))

# Set start and end points


grid[5][5].type = NodeType.START
start = grid[5][5]
grid[10][10].type = NodeType.END
end = grid[10][10]

for row in range(GRID_SIZE):
    for col in range(GRID_SIZE):
        if grid[row][col].type == NodeType.EMPTY:
            grid[row][col].calc_values(start.position, end.position)
 
# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(WINDOW_SIZE)
 
# Set title of screen
pygame.display.set_caption("Array Backed Grid")
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    for event in pygame.event.get():  # User did something
        if event.type == pygame.QUIT:  # If user clicked close
            done = True  # Flag that we are done so we exit this loop
        elif event.type == pygame.MOUSEBUTTONDOWN:
            # User clicks the mouse. Get the position
            pos = pygame.mouse.get_pos()
            # Change the x/y screen coordinates to grid coordinates
            col = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            # Set that location to one
            # grid[row][col].walkable = True
            # pos is the mouse coordinates, row col is the grid coordinates
            print("Click: ", pos, "({0}, {1})".format(row, col), "Type: ", grid[row][col].type)
            grid[row][col].display_cost()
 
    # Set the screen background
    screen.fill(BACKGROUND_COLOR)
 
    # Draw the grid
    for row in range(GRID_SIZE):
        for col in range(GRID_SIZE):

            tile = grid[row][col].type

            if tile == NodeType.EMPTY:
                color = EMPTY_COLOR

            elif tile == NodeType.WALL:
                color = WALL_COLOR

            elif tile == NodeType.START or tile == NodeType.END:
                color = DESTINATION
            
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * col + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    # Limit to 60 frames per second
    clock.tick(60)
 
    # Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
# Be IDLE friendly. If you forget this line, the program will 'hang'
# on exit.
pygame.quit()