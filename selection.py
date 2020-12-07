import pygame


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

def save(grid):
    file = open("grid.csv","w")
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            file.write(str(grid[i][j]))
        file.write("\n")
    file.close
 

WIDTH = 10
HEIGHT = 10
 

MARGIN = 1
 

grid = []
for row in range(90):
    grid.append([])
    for column in range(90):
        grid[row].append(0)  
 


 

pygame.init()
 

WINDOW_SIZE = [990, 990]
screen = pygame.display.set_mode(WINDOW_SIZE)
 

pygame.display.set_caption("selection")
 

end = False
 

clock = pygame.time.Clock()
 

while not end:
    for event in pygame.event.get():  
        if event.type == pygame.QUIT:
            save(grid)
            end = True  
        elif event.type == pygame.MOUSEBUTTONDOWN:
            
            pos = pygame.mouse.get_pos()
            
            column = pos[0] // (WIDTH + MARGIN)
            row = pos[1] // (HEIGHT + MARGIN)
            
            grid[row][column] = 1
            print("Click ", pos, "Grid coordinates: ", row, column)
 
    
    screen.fill(BLACK)

    
    for row in range(90):
        for column in range(90):
            color = WHITE
            if grid[row][column] == 1:
                color = BLACK
            pygame.draw.rect(screen,
                             color,
                             [(MARGIN + WIDTH) * column + MARGIN,
                              (MARGIN + HEIGHT) * row + MARGIN,
                              WIDTH,
                              HEIGHT])
 
    
    clock.tick(60)
 
    
    pygame.display.flip()
 

pygame.quit()
