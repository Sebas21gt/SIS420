
from Agent import Agent
from World import World
from Node import Node
import pygame
import math
import numpy as np
# from scipy.spatial import distance
def d_e(a,b):
    # return distance.euclidean(a,b)
    return math.sqrt(a*a - b*b)
def d(a,b):
    return sum(abs(val1-val2) for val1, val2 in zip(a,b))
#---------------------------------- Set up screen -----------------------------------------

print ("Setting up screen")
width = 1000
height = 1000
cell_size = 10                                                  #Change this to change grid size
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))

running  = 1

for i in range(1, math.floor(width / cell_size) + 1):
    pygame.draw.line(screen, (0, 0, 0), (i * cell_size, 0), (i * cell_size, height))
    pygame.display.flip()

for i in range(1, math.floor(height / cell_size) + 1):
    pygame.draw.line(screen, (0, 0, 0), (0, i * cell_size), (width, i * cell_size))
    pygame.display.flip()


#---------------------------------- Set up World ------------------------------------------
print ("Conjuring the Matrix")

end = (np.random.randint(80,100), np.random.randint(80,100))                                                        # Goal State

w = World(width, height,cell_size)
#wall_pos = [(0,5),(1,5),(2,5),(3,5),(4,5),(6,7)]
wall_pos = w.random_wall(40)                                        # Percentage of Walls in Grid

if end in wall_pos:
    wall_pos.remove(end)


#---------------------------------- Simulation --------------------------------------------

print ("Activating the Matrix")


#---------------------------------- Setting Up the World ----------------------------------


agent = Agent(w, 0, 0)                                              # State State
neighbors = agent.neighbor()
visited = [(0,0)]
current = (agent.pos_x,agent.pos_y)


#---------------------------------- Drawing Walls------------------------------------------

for wall in wall_pos:
    w.draw_rec(screen, wall, pygame.Color(0, 0, 0))
w.draw_rec(screen, end, pygame.Color(0, 255, 0))

#---------------------------------- Searching ---------------------------------------------


Start = (0,0)
end = end

StartNode = Node(Start[0],Start[1],parent=[Start],start=Start,end=end,world=World)
open_list = [StartNode]
close_list =[]

while(1):

    ################################## Pygame Stuff #######################################
    event = pygame.event.poll()
    if event.type == pygame.QUIT:
        pygame.quit()
        exit()
    
    w.draw_rec(screen, Start, pygame.Color(255, 0, 0))
    # w.draw_rec(screen, n.pos, pygame.Color(100, 100, 100))

    #######################################################################################

    ################################## Algorithm ##########################################
    ### A Star ####
    if len(open_list) != 0:
        n = open_list[0]
        del open_list[0]
        d = list(map(lambda x : x.pos,open_list))
        b = list(map(lambda x : x.pos,close_list))
        if n.pos not in d and n.pos not in b:
            print(list(map(lambda x:x.pos,n.neighbor()))) 
            for i in n.neighbor():
                if i.pos not in wall_pos:
                    open_list.append(i)




        open_list.sort(key = lambda x : x.cost,reverse=False)
        print(list(map(lambda x:x.cost,open_list)))
        close_list.append(n)

        ################################## Pygame Stuff #######################################
        w.draw_rec(screen, n.pos, pygame.Color(0, 255, 255))
        pygame.display.flip()
        #######################################################################################


        ################################## Pygame Stuff ###############################
        if n.pos != end:
            w.draw_rec(screen, n.pos, pygame.Color(175, 175, 175))
        else:
            w.draw_rec(screen, n.pos, pygame.Color(0, 175, 0))

            path = list(n.parent[1::])
            for i in path:
                w.draw_rec(screen, i, pygame.Color(255, 175, 0))
                pygame.time.delay(50)  

            pygame.image.save(screen, "last_img.jpeg")
            break
            ###############################################################################
        # pygame.time.delay(10)

    
pygame.time.delay(5000)                                 #Delay after completion