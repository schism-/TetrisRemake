'''
Created on 11/set/2011

@author: Christian
'''

import pygame
import math

class Tetramine(object):
    '''
    classdocs
    '''


    def __init__(self, scheme, current_orientation, rotations, renders):
        '''
        Constructor
        '''
        self.scheme = scheme
        self.current_orientation = current_orientation
        self.rotations = rotations
        self.renders = renders
        self.x = 0
        self.y = 0
        self.last_stable_center = None
        self.last_stable_rotation = None
    
    
    def checkBoundaries(self, world):
        
        if (self.x < 0) or\
            (self.x >= world.x_resolution) or\
            (self.y < 0) or\
            (self.y >= world.y_resolution):
            #print "Center out of bounds @" + str(self.x) + ", " + str(self.y) 
            return False
        
        for mino_offset in self.renders[self.current_orientation]:
            x_pos, y_pos = self.calculate_mino_position(mino_offset)
            if (x_pos < 0) or\
                (y_pos < 0) or\
                (x_pos >= world.x_resolution) or\
                (y_pos >= world.y_resolution):
                    #print "Mino out of bounds @" + str(x_pos) + ", " + str(y_pos)
                    return False 

        return True
    
    def checkCollisions(self, world):
        
        if  world.world_matrix[self.x][self.y] == 3:
            #print "Center out of bounds @" + str(self.x) + ", " + str(self.y) 
            return False
        
        for mino_offset in self.renders[self.current_orientation]:
            x_pos, y_pos = self.calculate_mino_position(mino_offset)
            if world.world_matrix[x_pos][y_pos] == 3:
                    #print "Mino out of bounds @" + str(x_pos) + ", " + str(y_pos)
                    return False 

        return True
    
    def isAtBottom(self, world):
        
        x_pos, y_pos = self.calculate_mino_position((0, 0))
        
        if (y_pos >= world.y_resolution - 1):
            #print "Mino at bottom @" + str(x_pos) + ", " + str(y_pos)
            return True
        elif (world.world_matrix[x_pos][y_pos + 1] == 3):
            #print "Collision @" + str(x_pos) + ", " + str(y_pos)
            return True
        
        for mino_offset in self.renders[self.current_orientation]:
            x_pos, y_pos = self.calculate_mino_position(mino_offset)
            if (y_pos >= world.y_resolution - 1):
                #print "Mino at bottom @" + str(x_pos) + ", " + str(y_pos)
                return True
            elif (world.world_matrix[x_pos][y_pos + 1] == 3):
                #print "Collision @" + str(x_pos) + ", " + str(y_pos)
                return True
        
        return False
        
    def  render(self, world, center_color = (255, 0, 0), mino_color = (255, 255, 255)):
        
        border_thickness = 5
        
        #=======================================================================
        # try:    
        #    pygame.draw.rect(world.screen_surface, 
        #                 center_color, 
        #                 (world.pos_matrix[self.x][self.y][0] + int(math.ceil(border_thickness / 2.0)), 
        #                  world.pos_matrix[self.x][self.y][1] + int(math.ceil(border_thickness / 2.0)), 
        #                  world.mino_width - border_thickness, 
        #                  world.mino_height - border_thickness), 
        #                 border_thickness)
        # except IndexError:
        #    print "--------------> Error at (%i, %i)" % (world.pos_matrix[self.x][self.y][0], world.pos_matrix[self.x][self.y][1])
        #=======================================================================
        
        self.render_mino(world, [0, 0], mino_color)
        
        for mino_offset in self.renders[self.current_orientation]:
            self.render_mino(world, mino_offset, mino_color)
       
        
    def render_mino(self, world, mino_offset, color):
        
        border_thickness = 11
        border_offset = int(math.ceil(border_thickness / 2.0))
        
        x_pos, y_pos = self.calculate_mino_position(mino_offset)
        try:
            pygame.draw.rect(world.screen_surface, 
                             color, 
                             (world.pos_matrix[x_pos][y_pos][0] + border_offset,
                              world.pos_matrix[x_pos][y_pos][1] + border_offset,
                              world.mino_width - border_thickness, 
                              world.mino_height - border_thickness), 
                              border_thickness)
        except IndexError:
            print "("+ str(x_pos) +")" + " ("+ str(y_pos) +")"
            raise IndexError
        
    def calculate_mino_position(self, mino_offset):
        
        x_pos = self.x + mino_offset[0]
        y_pos = self.y + mino_offset[1]
    
        return x_pos, y_pos
    
    def place(self, x, y):
        self.x = x
        self.y = y