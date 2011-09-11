'''
Created on 11/set/2011

@author: Christian
'''

class Mino(object):
    '''
    classdocs
    '''


    def __init__(self, width, height, isCenter, orientation):
        '''
        Constructor
        '''
        self.width = width
        self.height = height
        self.isCenter = isCenter
        self.orientation = orientation