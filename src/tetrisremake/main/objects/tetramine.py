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
        
        
        #Structure (sign for x, x or y, sign for y, x or y)
        # 0 = +    1 = -
        # 0 = x    1 = y
        
        rotation_modes = [
                          [(0, 0, 0, 1), (0, 0, 0, 1)],
                          [(1, 1, 1, 0), (1, 1, 0, 0)],
                          [(1, 0, 1, 1), (1, 0, 1, 1)],
                          [(0, 1, 0, 0), (0, 1, 1, 0)]
                          ]
        
        #rotations = (rotation_modes[0], rotation_modes[1], rotation_modes[2], rotation_modes[3])
        rotations = (rotation_modes[0], rotation_modes[1], rotation_modes[0], rotation_modes[1])
        
        if self.orientation == 0:
            for (x, y) in self.scheme:
                self.render_mino(world, rotations[0], (x, y))
                
        elif self.orientation == 1:
            for (x, y) in self.scheme:
                self.render_mino(world, rotations[1], (x, y))
        
        elif self.orientation == 2:
            for (x, y) in self.scheme:
                self.render_mino(world, rotations[2], (x, y))
        
        elif self.orientation == 3:
            for (x, y) in self.scheme:
                self.render_mino(world, rotations[3], (x, y))
    
    def render_mino(self, world, rotation, pos):
        
        x_rotation = rotation[0]
        y_rotation = rotation[1]
        
        x_pos = [0, 0]
        y_pos = [0, 0]
        
        if x_rotation[0] == 0:
            if x_rotation[1] == 0:
                x_pos[0] = self.x + pos[0]
            elif x_rotation[1] == 1:
                x_pos[0] = self.x + pos[1]
        elif x_rotation[0] == 1:
            if x_rotation[1] == 0:
                x_pos[0] = self.x - pos[0]
            elif x_rotation[1] == 1:
                x_pos[0] = self.x - pos[1]
              
        if x_rotation[2] == 0:
            if x_rotation[3] == 0:
                x_pos[1] = self.y + pos[0]
            elif x_rotation[3] == 1:
                x_pos[1] = self.y + pos[1]
        elif x_rotation[2] == 1:
            if x_rotation[3] == 0:
                x_pos[1] = self.y - pos[0]
            elif x_rotation[3] == 1:
                x_pos[1] = self.y - pos[1]
        
        if y_rotation[0] == 0:
            if y_rotation[1] == 0:
                y_pos[0] = self.x + pos[0]
            elif y_rotation[1] == 1:
                y_pos[0] = self.x + pos[1]
        elif y_rotation[0] == 1:
            if y_rotation[1] == 0:
                y_pos[0] = self.x - pos[0]
            elif y_rotation[1] == 1:
                y_pos[0] = self.x - pos[1]
              
        if y_rotation[2] == 0:
            if y_rotation[3] == 0:
                y_pos[1] = self.y + pos[0]
            elif y_rotation[3] == 1:
                y_pos[1] = self.y + pos[1]
        elif y_rotation[2] == 1:
            if y_rotation[3] == 0:
                y_pos[1] = self.y - pos[0]
            elif y_rotation[3] == 1:
                y_pos[1] = self.y - pos[1]
            
        pygame.draw.rect(world.screen_surface, 
                                 (255, 255, 255), 
                                 (world.pos_matrix[x_pos[0]][x_pos[1]][0], 
                                  world.pos_matrix[y_pos[0]][y_pos[1]][1], 
                                  world.mino_width, 
                                  world.mino_height), 
                                  1)
    
    def place(self, x, y):
        self.x = x
        self.y = y