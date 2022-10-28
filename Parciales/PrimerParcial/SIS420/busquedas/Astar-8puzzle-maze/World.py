from this import d
import pygame
import random

class World:
    agent_list = {}
    width = 200
    height = 200
    cell_size = 0


    def __init__(self, width, height,cell_size):

        self.width = width/cell_size -1
        self.height = height/cell_size -1
        self.cell_size = cell_size

    def d(self,a,b):
        return sum(abs(val1-val2) for val1, val2 in zip(a,b))

    def draw_rec(self, screen, pos, color = pygame.Color(0,255,0)):
        pygame.draw.rect(screen,color, (pos[0]*self.cell_size +1, pos[1]*self.cell_size +1, self.cell_size -1, self.cell_size -1))
        pygame.init()
        weight = self.d(pos,(0,0))
        font = pygame.font.SysFont('Arial', 20)
        # screen.blit(font.render(str(weight), True, (0,0,0)), (pos[0]*self.cell_size + 2 , pos[1]*self.cell_size ))
        pygame.display.flip()

    def random_wall(self, num):
        walls = []
        for i in range(int(num/100 * (self.width*self.height))):
            x = int(random.random()*self.width)
            y = int(random.random()*self.height)
            if x != 0 and y != 0:
                walls.append((x,y))
        return walls