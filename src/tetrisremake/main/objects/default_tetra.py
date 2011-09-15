'''
Created on 15/set/2011

@author: Christian
'''

class Classic_Tetra:
    
    def __init__(self):
        
        #Structure (sign for x, x or y, sign for y, x or y)
        # 0 = +    1 = -
        # 0 = x    1 = y
        rotation_modes = [
                          [(0, 0, 0, 1), (0, 0, 0, 1)],
                          [(1, 1, 1, 0), (1, 1, 0, 0)],
                          [(1, 0, 1, 1), (1, 0, 1, 1)],
                          [(0, 1, 0, 0), (0, 1, 1, 0)]
                          ]
        
        t_offsets = [ (1, 0), (-1, 0), (0, -1) ]
        i_offsets = [ (0, -1), (0, 1), (0, 2) ]
        l_offsets = [ (0, -1), (0, 1), (1, 1) ]
        j_offsets = [ (0, -1), (0, 1), (-1, 1) ]
        s_offsets = [ (1, 0), (0, 1), (-1, 1) ]
        z_offsets = [ (-1, 0), (0, 1), (1, 1) ]
        o_offsets = [ (1, 0), (0, 1), (1, 1) ]
        
        t_rotations = ( rotation_modes[0], rotation_modes[1], rotation_modes[2], rotation_modes[3] )
        i_rotations = ( rotation_modes[0], rotation_modes[1], rotation_modes[0], rotation_modes[1] )
        l_rotations = ( rotation_modes[0], rotation_modes[1], rotation_modes[2], rotation_modes[3] )
        j_rotations = ( rotation_modes[0], rotation_modes[1], rotation_modes[2], rotation_modes[3] )
        s_rotations = ( rotation_modes[0], rotation_modes[1], rotation_modes[0], rotation_modes[1] )
        z_rotations = ( rotation_modes[0], rotation_modes[1], rotation_modes[0], rotation_modes[1] )
        o_rotations = ( rotation_modes[0], rotation_modes[0], rotation_modes[0], rotation_modes[0] )
        
        self.offsets = []       
        self.offsets.append(t_offsets)
        self.offsets.append(i_offsets)
        self.offsets.append(l_offsets)
        self.offsets.append(j_offsets)
        self.offsets.append(s_offsets)
        self.offsets.append(z_offsets)
        self.offsets.append(o_offsets)
        
        self.rotations = []
        self.rotations.append(t_rotations)
        self.rotations.append(i_rotations)
        self.rotations.append(l_rotations)
        self.rotations.append(j_rotations)
        self.rotations.append(s_rotations)
        self.rotations.append(z_rotations)
        self.rotations.append(o_rotations)
        
    def get_tetra(self, x):
        
        return self.offsets[x], self.rotations[x]