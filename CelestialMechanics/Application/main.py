'''
Created on 24 de oct. de 2016

@author: pabli
'''

from Models.Propagator import Propagator
import numpy as np

if __name__ == '__main__':
    
    sv = np.array([42164.0, 0.0, 0.0, 0.0, 1.5, 0.0])
    
    p = Propagator.create(sv, 1)
    
    p.RK4(94000)
    
    
    p.plot()