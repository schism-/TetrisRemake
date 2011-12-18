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

SCREEN_SIZE = (600, 700)
#PLATFORM_SIZE = (500, 900)


class GameWorld(object):
    
    def __init__(self, screen_surface, screen_size, x_resolution, y_resolution, mino_dim):
        
        self.screen_size = screen_size
        
        self.x_resolution = x_resolution
        self.y_resolution = y_resolution
        
        self.current_tetra = None
        
        self.screen_surface = screen_surface
        
        self.platform_pos, self.platform_width, self.platform_height = self.calculate_platform()
        
        self.mino_width = int(self.platform_width / x_resolution)
        self.mino_height = int(self.platform_height / y_resolution)
                
        self.world_matrix = [[0 for i in range(self.y_resolution)] for j in range(self.x_resolution)]
        
        self.pos_matrix = []
        for x in range(self.platform_pos[0], self.platform_width + self.platform_pos[0] , self.mino_width ):
            temp_pos_array = []
            for y in range(self.platform_pos[1], self.platform_height + self.platform_pos[1], self.mino_height ):
                temp_pos_array.append((x, y))
            self.pos_matrix.append(temp_pos_array)
            
        print "World Matrix: " + str(len(self.world_matrix)) + " x " + str(len(self.world_matrix[0]))
        print "Pos Matrix: " + str(len(self.pos_matrix)) + " x " + str(len(self.pos_matrix[0]))
        
        self.default_font = pygame.font.SysFont("arial", 18) 
        
        self.points = 0
        
        self.game_over = False
        
    def calculate_platform(self):
        #min_dimension = self.screen_size[0] if (self.screen_size[0] < self.screen_size[1]) else self.screen_size[1]
        
        min_dimension = self.screen_size[1]
        
        platform_height = int( 0.9 * min_dimension )
        platform_width = int((platform_height / 18) * 10)
        
        platform_offset = int((self.screen_size[1] - platform_height) / 2) 
        
        platform_pos = (platform_offset, platform_offset)
        
        return platform_pos, platform_width, platform_height
    
    def add_tetramino(self, tetra):
        self.current_tetra = tetra

    def render(self):
        
        #TODO: render grid
        self.render_grid()
        #Render additional GUI        
        self.render_gui()
        #TODO: Render non moving blocks
        self.render_non_moving_blocks()
        #TODO: Render current tetramino
        if self.current_tetra is not None:
            self.current_tetra.render(self)
            
            self.render_shadow_block()
    
    def render_grid(self):
        for col in self.pos_matrix:
            temp_end = (col[-1][0], col[-1][1] + self.mino_height)
            pygame.draw.line(self.screen_surface, (62, 62, 62), col[0], temp_end, 2)
            
        temp_beg = (self.pos_matrix[-1][0][0] + self.mino_width, self.pos_matrix[-1][0][1])
        temp_end = (self.pos_matrix[-1][-1][0] + self.mino_width, self.pos_matrix[-1][-1][1] + self.mino_height)
        pygame.draw.line(self.screen_surface, (62, 62, 62), temp_beg, temp_end, 2)
        
        for row in range(len(self.pos_matrix[0])):
            temp_end = (self.pos_matrix[-1][row][0] + self.mino_width, self.pos_matrix[-1][row][1])
            pygame.draw.line(self.screen_surface, (62, 62, 62), self.pos_matrix[0][row], temp_end, 2)
            
        temp_beg = (self.pos_matrix[0][len(self.pos_matrix[0]) - 1][0], 
                    self.pos_matrix[0][len(self.pos_matrix[0]) - 1][1] + self.mino_height)
         
        temp_end = (self.pos_matrix[-1][len(self.pos_matrix[0]) - 1][0] + self.mino_width, 
                    self.pos_matrix[-1][len(self.pos_matrix[0]) - 1][1] + self.mino_height)
        pygame.draw.line(self.screen_surface, (62, 62, 62), temp_beg, temp_end, 2)
        
    def render_gui(self):
        point_surface = self.default_font.render( str(self.points), True, (255,255,255), (0,0,0))
        self.screen_surface.blit( point_surface, (SCREEN_SIZE[0] - 50, 50) )
    
    def render_non_moving_blocks(self):
        
        non_moving_block_color = (255, 218, 51)
        
        for x in range(len(self.world_matrix)):
            for y in range(len(self.world_matrix[x])):
                if self.world_matrix[x][y] == 3:
                    pygame.draw.rect(self.screen_surface, 
                         non_moving_block_color, 
                         (self.pos_matrix[x][y][0], 
                          self.pos_matrix[x][y][1], 
                          self.mino_width, 
                          self.mino_height), 
                         1)
    
    def render_shadow_block(self):
        
        shadow_tetra = Tetramine(self.current_tetra.scheme, 
                                 self.current_tetra.current_orientation, 
                                 self.current_tetra.rotations, 
                                 self.current_tetra.renders)
        
        shadow_tetra.place(self.current_tetra.x, self.current_tetra.y)
        
        while ( (shadow_tetra.checkBoundaries(self) == True) and (shadow_tetra.checkCollisions(self) == True) ):
            shadow_tetra.place( shadow_tetra.x, shadow_tetra.y + 1 )
    
        shadow_tetra.place( shadow_tetra.x, shadow_tetra.y - 1 )
    
        shadow_tetra.render(self, center_color = (30, 140, 50), mino_color = (30, 140, 50) )
    
    def checkLines(self):
        lines = []
        
        for line in range(len(self.world_matrix[0])):
            blocks = 0
            for x in range(len(self.world_matrix)):
                if self.world_matrix[x][line] == 3:
                    blocks += 1
            if blocks == len(self.world_matrix):
                lines.append(line)
        
        return lines
    
    def removeLines(self):
        if (len(self.checkLines()) > 0):
            for line in self.checkLines():
                print "Removing line no" + str(line)
                self.removeSingleLine(line)
                
    def removeSingleLine(self, lineNo):
        for line in range(lineNo, 1, -1 ):
            zeros = 0
            for x in range( len(self.world_matrix) ):
                self.world_matrix[x][line] = self.world_matrix[x][line - 1]
                if self.world_matrix[x][line - 1] == 0:
                    zeros += 1
            if zeros == len(self.world_matrix[0]):
                break
                  
    
#===============================================================================
# 
#    0 = empty block
#    1 = center of moving block
#    2 = non-center of moving block
#    3 = filled block, non-moving
# 
#===============================================================================

        
pygame.init()
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

tetris = GameWorld(screen, SCREEN_SIZE, 10, 18, 50)
tetra_list = default_tetra.Classic_Tetra()

#Clock for framerate
main_clock = pygame.time.Clock()

#Set timer for tetra's drop 
pygame.time.set_timer(pygame.USEREVENT + 1, 600)

#Set timer for tetra's transition to non-moving blocks
transitionTimer = False
pygame.time.set_timer(pygame.USEREVENT + 2, 0)

#Choose a random tetra
x = randint(0,6)
random_tetra, random_rotations, random_renders = tetra_list.get_tetra(x)
current_tetra = Tetramine(random_tetra, 0, random_rotations, random_renders)
current_tetra.place(5,1)
tetris.add_tetramino(current_tetra)

while True:
    
    screen.fill((0, 0, 0))  
      
    tetris.removeLines()
      
    tetris.render()
    
    pygame.display.update()

    if (tetris.current_tetra == None):
        x = randint(0,6)
        random_tetra, random_rotations, random_renders = tetra_list.get_tetra(x)
        current_tetra = Tetramine(random_tetra, 0, random_rotations, random_renders)
        current_tetra.place(5,1)
        tetris.add_tetramino(current_tetra)
    
    for event in pygame.event.get():
        
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
            
        elif event.type == pygame.USEREVENT + 1:
            if (tetris.current_tetra is not None) and (transitionTimer is not True):
                tetris.current_tetra.y += 1 
                if tetris.current_tetra.checkBoundaries(tetris) == False:
                    tetris.current_tetra.y -= 1
                
                if (tetris.game_over is not True):
                    tetris.points += 1
                
        elif event.type == pygame.USEREVENT + 2:
            print "Transition."
            if tetris.current_tetra.isAtBottom(tetris) == True:
                x_pos, y_pos = tetris.current_tetra.calculate_mino_position((0, 0))
                tetris.world_matrix[x_pos][y_pos] = 3
             
                for (x, y) in tetris.current_tetra.renders[tetris.current_tetra.current_orientation]:
                    x_pos, y_pos = tetris.current_tetra.calculate_mino_position((x, y))
                    tetris.world_matrix[x_pos][y_pos] = 3
                    
                tetris.current_tetra = None
                transitionTimer = False
                pygame.time.set_timer(pygame.USEREVENT + 2, 0)
            else:
                print "Derp."
                transitionTimer = False
                pygame.time.set_timer(pygame.USEREVENT + 2, 0)
            
                
        elif event.type == pygame.KEYDOWN:
            if tetris.current_tetra is not None:
                if event.key == pygame.K_LEFT:
                    tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation - 1) % 4
                    if tetris.current_tetra.checkBoundaries(tetris) == False or\
                        tetris.current_tetra.checkCollisions(tetris) == False:
                        tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation + 1) % 4
                
                elif event.key == pygame.K_RIGHT:
                    tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation + 1) % 4
                    if tetris.current_tetra.checkBoundaries(tetris) == False or\
                        tetris.current_tetra.checkCollisions(tetris) == False:
                        tetris.current_tetra.current_orientation = (tetris.current_tetra.current_orientation - 1) % 4
                
                elif event.key == pygame.K_a:
                    tetris.current_tetra.x -= 1
                    if tetris.current_tetra.checkBoundaries(tetris) == False or\
                        tetris.current_tetra.checkCollisions(tetris) == False:
                        tetris.current_tetra.x += 1

                elif event.key == pygame.K_d:
                    tetris.current_tetra.x += 1 
                    if tetris.current_tetra.checkBoundaries(tetris) == False or\
                        tetris.current_tetra.checkCollisions(tetris) == False:
                        tetris.current_tetra.x -= 1

                elif event.key == pygame.K_w:
                    tetris.current_tetra.y -= 1
                    if tetris.current_tetra.checkBoundaries(tetris) == False:
                        tetris.current_tetra.y += 1
                    else:
                        transitionTimer = False
                        pygame.time.set_timer(pygame.USEREVENT + 2, 0)
                        
                elif event.key == pygame.K_s and (transitionTimer is not True):
                    tetris.current_tetra.y += 1 
                    if tetris.current_tetra.checkBoundaries(tetris) == False:
                        tetris.current_tetra.y -= 1
                    else:
                        transitionTimer = False
                        pygame.time.set_timer(pygame.USEREVENT + 2, 0)
                    
                    if (tetris.game_over is not True):
                        tetris.points += 1

    if (tetris.current_tetra is not None) and (tetris.current_tetra.isAtBottom(tetris) == True):
        print "Bottom!!!"
        
        if transitionTimer is not True:            
            pygame.time.set_timer(pygame.USEREVENT + 2, 500)
            transitionTimer = True
    
    
    milliseconds_passed = main_clock.tick(60)
        

            