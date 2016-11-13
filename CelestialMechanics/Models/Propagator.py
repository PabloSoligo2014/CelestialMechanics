'''
Created on 12 de nov. de 2016

@author: pabli
'''
import numpy as np
import matplotlib.pyplot as plt
from numpy import dtype

class Propagator(object):
    '''
    classdocs
    '''
    
    """
    def __init__(self):
        '''
        Constructor
        '''
        pass
    """    
    @classmethod
    def create(cls, stateVector, h):
        """
        Se utiliza metodo de clase en la construccion para poder luego utilizarlo con el 
        ORM de django
        """
        result = cls()
        
        cls.mu = 398600.448
        cls.stateVectors = []
        
        result.h = h
        result.stateVector = stateVector
        return result
    
    def plot(self):
        x = []
        y = []
        z = []
       
        """
        y_flt = [float(n) for n in s[0].split()]
        plt.plot(x, y_flt)
        """
        
        for e in self.stateVectors:
            x.append(e[0])
            y.append(e[1])
            z.append(e[2])

        plt.title("Orbita RK")
        plt.plot(x, y)
        plt.show()
        
        
    def __deriv(self, stateVector):
        
        mod = np.linalg.norm(stateVector); 
        
        #Paso derivo la posicion y me da velocidad
        #Derivo la velocidad y me da aceleracion
        coeff = -(self.mu)/(mod**3)
        result = np.array([ stateVector[3],
                            stateVector[4],
                            stateVector[5],
                            stateVector[0]*coeff,
                            stateVector[1]*coeff,
                            stateVector[2]*coeff,
                           ]) 
        

        
        return result;
    
    
        
    def RK4(self, time):
        """
        RK4 hardcodeando las 4 derivaciones, sin uso de bucle
        """
        
        yant     = self.stateVector;
        for t in range(0, time, self.h):
            
            y0 = yant
            k0 = self.__deriv(y0)
            
            y1 = y0 + (0.5*self.h)*k0
            k1 = self.__deriv(y1)
            
            y2 = y0 + (0.5*self.h)*k1
            k2 = self.__deriv(y2)
            
            y3 = y0 + (self.h)*k2
            k3 = self.__deriv(y3)
            
            yfinal =  y0 + (1/6.0)*(k0+ k1*2 + k2*2 + k3)*self.h;

            self.stateVectors.append(yfinal)
            yant = yfinal;
            
        
         