'''
Created on 11/set/2011

@author: Christian
'''

import pygame
from sys import exit
from objects import *
from tetrisremake.main.objects.tetramine import Tetramine

def place_tetramine(world, pos, tetra):
    
    world[pos[0]][pos[1]] = 1
    
    #===========================================================================
    # for (x,y) in tetra:
    #    world[pos[0] + y][pos[1] + x] = 2
    #===========================================================================


SCREEN_SIZE = (1000, 1000)

pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

x_resolution = 10
y_resolution = 10

mino_width = int( SCREEN_SIZE[0] / x_resolution )
mino_height = int( SCREEN_SIZE[1] / y_resolution )



world_matrix = [[0 for i in range(x_resolution)] for j in range(y_resolution)]

pos_matrix = []
for x in range(0, SCREEN_SIZE[0], mino_width ):
    temp_pos_array = []
    for y in range(0, SCREEN_SIZE[1], mino_height ):
        temp_pos_array.append((x, y))
    pos_matrix.append(temp_pos_array)

print "----------------------------------------"    
for line in pos_matrix:
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
for line in world_matrix:
    print line

tetra = Tetramine([ (1, 0), (-1, 0), (0, -1) ])

tetra.place(6,4)

print "----------------------------------------"

for line in world_matrix:
    print line

while True:
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        
            