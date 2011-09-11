'''
Created on 11/set/2011

@author: Christian
'''

class Tetramine(object):
    '''
    classdocs
    '''


    def __init__(self, scheme):
        '''
        Constructor
        '''
        self.scheme = scheme
        self.x = 0
        self.y = 0
        
    def  render(self, world, surface):
        pass
    
    def place(self, x, y):
        self.x = x
        self.y = y