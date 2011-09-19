'''
Created on 19/set/2011

@author: Christian
'''

'''
Created on 11/set/2011

@author: Christian
'''

import pygame

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
        
        if (self.x < 0) or (self.x >= world.x_resolution) or (self.y < 0) or (self.y >= world.y_resolution):
            print "Center out of bounds @" + str(self.x) + ", " + str(self.y) 
            return False
        
        if self.current_orientation == 0:
            for (x, y) in self.scheme:
                x_pos, y_pos = self.calculate_mino_position(self.rotations[0], (x, y))
                if (x_pos[0] < 0) or (y_pos[1] < 0) or (x_pos[0] >= world.x_resolution) or (y_pos[1] >= world.y_resolution):
                    print "Mino out of bounds @" + str(x_pos) + ", " + str(y_pos)
                    return False 
                
        elif self.current_orientation == 1:
            for (x, y) in self.scheme:
                x_pos, y_pos = self.calculate_mino_position(self.rotations[1], (x, y))
                if (x_pos[0] < 0) or (y_pos[1] < 0) or (x_pos[0] >= world.x_resolution) or (y_pos[1] >= world.y_resolution):
                    print "Mino out of bounds @" + str(x_pos) + ", " + str(y_pos)
                    return False 
        
        elif self.current_orientation == 2:
            for (x, y) in self.scheme:
                x_pos, y_pos = self.calculate_mino_position(self.rotations[2], (x, y))
                if (x_pos[0] < 0) or (y_pos[1] < 0) or (x_pos[0] >= world.x_resolution) or (y_pos[1] >= world.y_resolution):
                    print "Mino out of bounds @" + str(x_pos) + ", " + str(y_pos)
                    return False 
        
        elif self.current_orientation == 3:
            for (x, y) in self.scheme:
                x_pos, y_pos = self.calculate_mino_position(self.rotations[3], (x, y))
                if (x_pos[0] < 0) or (y_pos[1] < 0) or (x_pos[0] >= world.x_resolution) or (y_pos[1] >= world.y_resolution):
                    print "Mino out of bounds @" + str(x_pos) + ", " + str(y_pos)
                    return False 

        return True
    
    def isAtBottom(self, world):
        
        x_pos, y_pos = self.calculate_mino_position(self.rotations[self.current_orientation], (0, 0))
        if (y_pos[1] >= world.y_resolution - 1):
            print "Mino at bottom @" + str(x_pos) + ", " + str(y_pos)
            return True
        elif (world.world_matrix[y_pos[1] + 1][x_pos[0]] == 3):
            print "Collision @" + str(x_pos) + ", " + str(y_pos)
            return True
        
        for (x, y) in self.scheme:
            x_pos, y_pos = self.calculate_mino_position(self.rotations[self.current_orientation], (x, y))
            if (y_pos[1] >= world.y_resolution - 1):
                print "Mino at bottom @" + str(x_pos) + ", " + str(y_pos)
                return True
            elif (world.world_matrix[y_pos[1] + 1][x_pos[0]] == 3):
                print "Collision @" + str(x_pos) + ", " + str(y_pos)
                return True
        
        return False
    
    #===========================================================================
    # def  render(self, world):
    #    
    #    try:    
    #        pygame.draw.rect(world.screen_surface, 
    #                     (255, 0, 0), 
    #                     (world.pos_matrix[self.x][self.y][0], 
    #                      world.pos_matrix[self.x][self.y][1], 
    #                      world.mino_width, 
    #                      world.mino_height), 
    #                     1)
    #    except IndexError:
    #        print "--------------> Error at (%i, %i)" % (world.pos_matrix[self.x][self.y][0], world.pos_matrix[self.x][self.y][1])
    #        
    #    if self.current_orientation == 0:
    #        for (x, y) in self.scheme:
    #            try:
    #                self.render_mino(world, self.rotations[0], (x, y))
    #            except IndexError:
    #                print "--------------> Error at (%i, %i)" % (x, y)
    #            
    #    elif self.current_orientation == 1:
    #        for (x, y) in self.scheme:
    #            self.render_mino(world, self.rotations[1], (x, y))
    #    
    #    elif self.current_orientation == 2:
    #        for (x, y) in self.scheme:
    #            self.render_mino(world, self.rotations[2], (x, y))
    #    
    #    elif self.current_orientation == 3:
    #        for (x, y) in self.scheme:
    #            self.render_mino(world, self.rotations[3], (x, y))
    #    
    #    self.last_stable_center = [self.x, self.y]
    #    self.last_stable_rotation = self.current_orientation
    #===========================================================================
        
    def  render(self, world):
        
        try:    
            pygame.draw.rect(world.screen_surface, 
                         (255, 0, 0), 
                         (world.pos_matrix[self.x][self.y][0], 
                          world.pos_matrix[self.x][self.y][1], 
                          world.mino_width, 
                          world.mino_height), 
                         1)
        except IndexError:
            print "--------------> Error at (%i, %i)" % (world.pos_matrix[self.x][self.y][0], world.pos_matrix[self.x][self.y][1])
            
        for mino in self.renders[self.current_orientation]:
            self.render_mino(world, rotation, pos)
       
        
    def render_mino(self, world, rotation, pos):
        
        x_pos, y_pos = self.calculate_mino_position(rotation, pos)
        try:
            #===================================================================
            # pygame.draw.rect(world.screen_surface, 
            #                 (255, 255, 255), 
            #                 (world.pos_matrix[x_pos[0]][x_pos[1]][0],
            #                  world.pos_matrix[y_pos[0]][y_pos[1]][1], 
            #                  world.mino_width, 
            #                  world.mino_height), 
            #                  1)
            #===================================================================
            
            pygame.draw.rect(world.screen_surface, 
                             (255, 255, 255), 
                             (world.pos_matrix[y_pos[1]][x_pos[0]][1],
                              world.pos_matrix[y_pos[1]][x_pos[0]][0], 
                              world.mino_width, 
                              world.mino_height), 
                              1)
        except IndexError:
            print "("+ str(x_pos) +")" + " ("+ str(y_pos) +")"
            raise IndexError
        
        
    #===========================================================================
    # def calculate_mino_position(self, rotation, pos):
    #    
    #    x_rotation = rotation[0]
    #    y_rotation = rotation[1]
    #    
    #    x_pos = [0, 0]
    #    y_pos = [0, 0]
    #    
    #    if x_rotation[0] == 0:
    #        if x_rotation[1] == 0:
    #            x_pos[0] = self.x + pos[0]
    #        elif x_rotation[1] == 1:
    #            x_pos[0] = self.x + pos[1]
    #    elif x_rotation[0] == 1:
    #        if x_rotation[1] == 0:
    #            x_pos[0] = self.x - pos[0]
    #        elif x_rotation[1] == 1:
    #            x_pos[0] = self.x - pos[1]
    #          
    #    if x_rotation[2] == 0:
    #        if x_rotation[3] == 0:
    #            x_pos[1] = self.y + pos[0]
    #        elif x_rotation[3] == 1:
    #            x_pos[1] = self.y + pos[1]
    #    elif x_rotation[2] == 1:
    #        if x_rotation[3] == 0:
    #            x_pos[1] = self.y - pos[0]
    #        elif x_rotation[3] == 1:
    #            x_pos[1] = self.y - pos[1]
    #    
    #    if y_rotation[0] == 0:
    #        if y_rotation[1] == 0:
    #            y_pos[0] = self.x + pos[0]
    #        elif y_rotation[1] == 1:
    #            y_pos[0] = self.x + pos[1]
    #    elif y_rotation[0] == 1:
    #        if y_rotation[1] == 0:
    #            y_pos[0] = self.x - pos[0]
    #        elif y_rotation[1] == 1:
    #            y_pos[0] = self.x - pos[1]
    #          
    #    if y_rotation[2] == 0:
    #        if y_rotation[3] == 0:
    #            y_pos[1] = self.y + pos[0]
    #        elif y_rotation[3] == 1:
    #            y_pos[1] = self.y + pos[1]
    #    elif y_rotation[2] == 1:
    #        if y_rotation[3] == 0:
    #            y_pos[1] = self.y - pos[0]
    #        elif y_rotation[3] == 1:
    #            y_pos[1] = self.y - pos[1]
    # 
    #    return x_pos, y_pos
    #===========================================================================
    
    def calculate_mino_position(self, rotation, pos):
        
        #Structure (sign for x, x or y, sign for y, x or y)
        # 0 = +    1 = -
        # 0 = x    1 = y
        
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
    
        return x_pos, y_pos
    
    def place(self, x, y):
        self.x = x
        self.y = y