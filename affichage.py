import pygame
import numpy as np

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)


file= open("grid.csv")


grid=[]

for row in range(90):
    grid.append([])
    for column in range(90):
        grid[row].append(0)



count=0
count2=0




for row in file:
    count2=0
    for x in range(0,len(row)):
        if row[x].isdigit():
            #print(row[x])
            print(count,count2)
            grid[count][count2]=int(row[x])
            count2+=1
    count+=1
    

print(grid)




WIDTH = 10
HEIGHT = 10 
MARGIN = 1
 



 
def update(plateau):
        global grid
        nouveauplateau=[]

        for i in range(len(plateau)):
            nouveauplateau.append([])
            for j in range(len(plateau[0])):
                nouveauplateau[i].append(0)



        for i in range(len(plateau)):
            for j in range(len(plateau[i])):
                voisin=0

                if plateau[i][j]==1:
                    if i>=1 and i+2<len(plateau) and j>=1 and j+2<len(plateau[i]):
                        for k in range(i-1,i+2):                    
                                for t in range(j-1,j+2):

                                    if plateau[k][t]==1:
                                        voisin+=1
                                        print(voisin,i,j,k,t)



                    if i==0 and j>=1 and j+2<len(plateau[i]):
                            for k in range(i,i+2):                    
                                for t in range(j-1,j+2):

                                    if plateau[k][t]==1:
                                        voisin+=1
                                        print(voisin,i,j,k,t)

                    if i>=1 and i+2<len(plateau) and j==0:
                        for k in range(i-1,i+2):                    
                            for t in range(j,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)


                    if i==0 and j==0:
                        for k in range(i,i+2):                    
                            for t in range(j,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)



                    if  i+2==len(plateau) and j>=1 and j+2<len(plateau[i]):
                        for k in range(i-1,i+1):                    
                            for t in range(j-1,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)
                                

                    if i>=1 and i+2<len(plateau)  and j+2==len(plateau[i]):
                        for k in range(i-1,i+2):                    
                            for t in range(j-1,j+1):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)

                    if  i+2==len(plateau)  and j+2==len(plateau[i]):
                        for k in range(i-1,i+1):                    
                            for t in range(j-1,j+1):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)           
                       
                    if voisin > 4 :
                        nouveauplateau[i][j]=0
                    if voisin < 3 :
                        nouveauplateau[i][j]=0
                    if voisin==3 or voisin==4:
                        nouveauplateau[i][j]=1


                if plateau[i][j]==0:
                    if i>=1 and i+2<len(plateau) and j>=1 and j+2<len(plateau[i]):
                        for k in range(i-1,i+2):                    
                                for t in range(j-1,j+2):

                                    if plateau[k][t]==1:
                                        voisin+=1
                                        print(voisin,i,j,k,t)



                    if i==0 and j>=1 and j+2<len(plateau[i]):
                        for k in range(i,i+2):                    
                            for t in range(j-1,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)

                    if i>=1 and i+2<len(plateau) and j==0:
                        for k in range(i-1,i+2):                    
                            for t in range(j,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)


                    if i==0 and j==0:
                        for k in range(i,i+2):                    
                            for t in range(j,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)



                    if  i+2==len(plateau) and j>=1 and j+2<len(plateau[i]):
                        for k in range(i-1,i+1):                    
                            for t in range(j-1,j+2):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)
                                

                    if i>=1 and i+2<len(plateau)  and j+2==len(plateau[i]):
                        for k in range(i-1,i+2):                    
                            for t in range(j-1,j+1):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)

                    if  i+2==len(plateau)  and j+2==len(plateau[i]):
                        for k in range(i-1,i+1):                    
                            for t in range(j-1,j+1):

                                if plateau[k][t]==1:
                                    voisin+=1
                                    print(voisin,i,j,k,t)           
                       
                    if voisin == 3 :
                        nouveauplateau[i][j]=1
                    else :
                        nouveauplateau[i][j]=0



    #afficher(nouveauplateau)
    #x = input("voulez vous continuer yes or no : ")
    #if x == "yes":
        #update(nouveauplateau)
        grid=nouveauplateau
        return grid

 

pygame.init() 
WINDOW_SIZE = [990, 990]
screen = pygame.display.set_mode(WINDOW_SIZE)
pygame.display.set_caption("Array Backed Grid")
 

done = False
clock = pygame.time.Clock()
 

while not done:
   for event in pygame.event.get():  
            if event.type == pygame.QUIT:  
                done = True  

 
    
   screen.fill(BLACK)
   update(grid)
   
   for row in range(90):
            for column in range(90):
                color = WHITE
                if int(grid[row][column]) == 1:
                    color = BLACK
                pygame.draw.rect(screen,
                                color,
                                [(MARGIN + WIDTH) * column + MARGIN,
                                (MARGIN + HEIGHT) * row + MARGIN,
                                WIDTH,
                                HEIGHT])
 
   
   clock.tick(60)
 
    
   pygame.display.flip()
 

