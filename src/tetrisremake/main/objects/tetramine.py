'''
Created on 11/set/2011

@author: Christian
'''

import pygame

class Tetramine(object):
    '''
    classdocs
    '''


    def __init__(self, scheme, orientation):
        '''
        Constructor
        '''
        self.scheme = scheme
        self.orientation = orientation
        self.x = 0
        self.y = 0
        
    def  render(self, world):
        
        pygame.draw.rect(world.screen_surface, (255, 255, 255), (world.pos_matrix[self.x][self.y][0], world.pos_matrix[self.x][self.y][1], world.mino_width, world.mino_height), 1)
        
        if self.orientation == 0:
            for (x, y) in self.scheme:
                pygame.draw.rect(world.screen_surface, 
                                 (255, 255, 255), 
                                 (world.pos_matrix[self.x + x][self.y + y][0], 
                                  world.pos_matrix[self.x + x][self.y + y][1], 
                                  world.mino_width, 
                                  world.mino_height), 
                                  1)
        elif self.orientation == 1:
            for (x, y) in self.scheme:
                pygame.draw.rect(world.screen_surface, 
                                 (255, 255, 255), 
                                 (world.pos_matrix[self.x - y][self.y - x][0], 
                                  world.pos_matrix[self.x - y][self.y + x][1], 
                                  world.mino_width, 
                                  world.mino_height), 
                                  1)
        elif self.orientation == 2:
            for (x, y) in self.scheme:
                pygame.draw.rect(world.screen_surface, 
                                 (255, 255, 255), 
                                 (world.pos_matrix[self.x - x][self.y - y][0], 
                                  world.pos_matrix[self.x - x][self.y - y][1], 
                                  world.mino_width, 
                                  world.mino_height), 
                                  1)
        elif self.orientation == 3:
            for (x, y) in self.scheme:
                pygame.draw.rect(world.screen_surface, 
                                 (255, 255, 255), 
                                 (world.pos_matrix[self.x + y][self.y + x][0], 
                                  world.pos_matrix[self.x + y][self.y - x][1], 
                                  world.mino_width, 
                                  world.mino_height), 
                                  1)
        
    def place(self, x, y):
        self.x = x
        self.y = y