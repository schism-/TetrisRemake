'''
Created on 11/set/2011

@author: Christian
'''

import pygame

class Tetramine(object):
    '''
    classdocs
    '''


    def __init__(self, scheme, current_orientation, rotations):
        '''
        Constructor
        '''
        self.scheme = scheme
        self.current_orientation = current_orientation
        self.rotations = rotations
        self.x = 0
        self.y = 0
        self.last_stable_render = []
        self.current_render = []
        
    def  render(self, world):
        
        try:
            
            if (self.x >= 0) and (self.x < world.x_resolution) and (self.y >= 0) and (self.y < world.y_resolution):
                
                pygame.draw.rect(world.screen_surface, 
                                 (255, 255, 255), 
                                 (world.pos_matrix[self.x][self.y][0], 
                                  world.pos_matrix[self.x][self.y][1], 
                                  world.mino_width, 
                                  world.mino_height), 
                                 1)
                
                self.current_render.append( ([self.x, self.y], [self.x, self.y]) )
                
                if self.current_orientation == 0:
                    for (x, y) in self.scheme:
                        self.render_mino(world, self.rotations[0], (x, y))
                        
                elif self.current_orientation == 1:
                    for (x, y) in self.scheme:
                        self.render_mino(world, self.rotations[1], (x, y))
                
                elif self.current_orientation == 2:
                    for (x, y) in self.scheme:
                        self.render_mino(world, self.rotations[2], (x, y))
                
                elif self.current_orientation == 3:
                    for (x, y) in self.scheme:
                        self.render_mino(world, self.rotations[3], (x, y))
                
                self.last_stable_render = self.current_render[:]
                self.current_render = []
                
            else:           
                raise IndexError
            
        except IndexError:
            
            #===================================================================
            # if (self.x < 0):
            #    self.x = 0
            # if (self.x >= world.x_resolution):
            #    self.x = world.x_resolution
            # if (self.y < 0):
            #    self.y = 0
            # if (self.y >= world.y_resolution):
            #    self.y = world.y_resolution
            #===================================================================
            
            self.x = self.last_stable_render[0][0]
            self.render(world)
            
            #===================================================================
            # print "Out of Bounds!! (%i, %i)" % (self.x, self.y)
            # print "Center: " + str(self.last_stable_render[0])
            # for mino in self.last_stable_render:
            #    pygame.draw.rect(world.screen_surface, 
            #                     (255, 255, 255), 
            #                     (world.pos_matrix[mino[0][0]][mino[0][1]][0], 
            #                      world.pos_matrix[mino[1][0]][mino[1][1]][1], 
            #                      world.mino_width, 
            #                      world.mino_height), 
            #                     1)
            #===================================================================
            
            self.current_render = []
        
        
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
        
        if (x_pos[0] >= 0) and (y_pos[0] >= 0) and (x_pos[1] < world.x_resolution) and (y_pos[1] < world.y_resolution): 
            pygame.draw.rect(world.screen_surface, 
                             (255, 255, 255), 
                             (world.pos_matrix[x_pos[0]][x_pos[1]][0], 
                             world.pos_matrix[y_pos[0]][y_pos[1]][1], 
                             world.mino_width, 
                             world.mino_height), 
                             1)
            self.current_render.append( (x_pos, y_pos) )
        else:
            print "Mino out of bounds at (%i, %i) (%i, %i)" % (x_pos[0], x_pos[1], y_pos[0], y_pos[1])
            raise IndexError
        
    
    def place(self, x, y):
        self.x = x
        self.y = y