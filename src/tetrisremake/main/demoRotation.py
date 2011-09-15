'''
Created on 11/set/2011

@author: Christian

'''

import pygame
from sys import exit
import objects
from objects import default_tetra
from tetrisremake.main.objects.tetramine import Tetramine
from random import randint

SCREEN_SIZE = (1000, 1000)


class GameWorld(object):
    
    def __init__(self, screen_surface, x_resolution, y_resolution):
        self.x_resolution = x_resolution
        self.y_resolution = y_resolution
        
        self.mino_width = int( SCREEN_SIZE[0] / self.x_resolution )
        self.mino_height = int( SCREEN_SIZE[1] / self.y_resolution )
        
        self.current_tetra = None
        
        self.screen_surface = screen_surface
        
        self.world_matrix = [[0 for i in range(self.x_resolution)] for j in range(self.y_resolution)]
        
        self.pos_matrix = []
        for x in range(0, SCREEN_SIZE[0], self.mino_width ):
            temp_pos_array = []
            for y in range(0, SCREEN_SIZE[1], self.mino_height ):
                temp_pos_array.append((x, y))
            self.pos_matrix.append(temp_pos_array)
        
    def add_tetramino(self, tetra):
        self.current_tetra = tetra

    def render(self):
        
        #TODO: render grid
        
        #TODO: Render non moving blocks
        
        #TODO: Render current tetramino
        self.current_tetra.render(self)
    


pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

tetris = GameWorld(screen, 10, 10)

print "----------------------------------------"    
for line in tetris.pos_matrix:
    print line
    
#===============================================================================
# 
#    0 = empty block
#    1 = center of moving block
#    2 = non-center of moving block
#    3 = filled block, non-moving
# 
#===============================================================================

print "----------------------------------------"
for line in tetris.world_matrix:
    print line

tetra_list = default_tetra.Classic_Tetra()

#FIX THIS SHITTTTTTT

x = randint(0,6)
print "Tetra no " + str(x)
random_tetra, random_rotations = tetra_list.get_tetra(6)

current_tetra = Tetramine(random_tetra, 0, random_rotations)

current_tetra.place(4,4)

tetris.add_tetramino(current_tetra)


print "----------------------------------------"

for line in tetris.world_matrix:
    print line

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation - 1) % 4
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation + 1) % 4
            elif event.key == pygame.K_RIGHT:
                tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation + 1) % 4
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation - 1) % 4
            elif event.key == pygame.K_a:
                tetris.current_tetra.x -= 1
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.x += 1
            elif event.key == pygame.K_d:
                tetris.current_tetra.x += 1 
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.x -= 1
            elif event.key == pygame.K_w:
                tetris.current_tetra.y -= 1
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.y += 1
            elif event.key == pygame.K_s:
                tetris.current_tetra.y += 1 
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.y -= 1
            
        screen.fill((0, 0, 0))  
          
        tetris.render()
        
        pygame.display.update()
            