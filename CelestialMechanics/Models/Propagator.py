 #!/usr/bin/python
 # -*- coding:UTF-8 -*-
'''
Created on 12 de nov. de 2016

@author: pabli
'''
import numpy as np
import matplotlib.pyplot as plt
from numpy import dtype
import math

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
        
        
        result.tableau_rk4 = np.array( [
                                    [0,   0,   0,   0,   0],
                                    [0.5, 0.5, 0,   0,   0],
                                    [0.5,  0,   0.5, 0,   0],
                                    [1,    0,   0,   1,   0],
                                    [1.0/6.0, 1.0/3.0, 1.0/3.0, 1.0/6.0, 0]
                                    ])
        
        result.tableau_rkf45 = np.array([
                    		[0,           0,         0,          0,          0,        0,      0,      0],
                    		[0.25,   0.25, 0,   0,   0, 0, 0, 0],
                    		[0.375,  0.09375,   0.28125, 0,   0, 0, 0, 0],
                    		[0.9230769230769231,  0.8793809740555303,   -3.277196176604461,   3.3208921256258535,   0, 0, 0, 0],
                    		[1.0, 2.0324074074074074, -8.0, 7.173489278752436, -0.20589668615984405, 0, 0, 0],
                    		[0.5, -0.2962962962962963, 2.0, -1.3816764132553607, 0.4529727095516569, -0.275, 0,0],
                    		[0.11851851851851852, 0, 0.5189863547758284, 0.5061314903420167, -0.18, 0.03636363636363636, 0, 0],
                    		[0.11574074074074074, 0, 0.5489278752436647, 0.5353313840155945, -0.2, 0, 0, 0]
                            ])
        
        
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
    
    
    
    def RKN(self, time, n):
        """
        RK4 hardcodeando las 4 derivaciones, sin uso de bucle
        """
        
       
        yant     = self.stateVector;
        for t in range(0, time, self.h):
            
            
            kimenosuno = self.__deriv(yant)
            
            yis = []
            kis = []
            
            for i in range(0, n):
                mult = self.tableau_rk4[i,i]
                yi = yant + (mult*self.h)*kimenosuno
                ki = self.__deriv(yi)
                
                #Se podria hacer todo en un paso pero por apredizaje
                #y debug se abre
                kis.append(ki)
                yis.append(yi)
                
                kimenosuno = ki
                
            ysum = [0,0,0,0,0,0]
            
            #ymasuno = ymasuno + f_euler (tn [i][0], yn.column (i)) * h * tableau_rk4 [order][i];
            for i in range(0, n):
                ysum =  ysum + self.tableau_rk4[n,i]*kis[i]

            yfinal =  yant + self.h*ysum
            
            self.stateVectors.append(yfinal)
            
            yant = yfinal;
        
        
    def RK45(self, time, n, epsilon):
        """RKF45
        
        Parameters
        ----------
        
        
        """
        
        yant = self.stateVector;
        
        self.h = 100.0
        t = 0.0
        #recorro desde desde un tiempo inicial a un tiempo final
        #for t in xrange(0, time,self.h):
        #for t in np.arange(0, time, self.h):
        while t < time:
            #kimenosuno = self.__deriv(yant)
            #Inicializo vectores a utilizar
            yis = np.array([])
            kis = np.array([])
            sum = np.array([])   
            f = np.array([])         
            #matriz para guardar los k intermedios
            kn = []
              
            #Recorro las filas de la tabla
            for i in range(0, n):
                kn.append(yant)
                #Recorro por columna
                for j in range(0, n):
                    if self.tableau_rkf45[i ,j + 1] != 0:
                        a = self.tableau_rkf45[i,j + 1]
                        f =  self.__deriv(kn[i]) * a * self.h
                        kn[i] = kn[i] + f
                
                        
            ysum = yant
            ysum_45 = yant
            #ymasuno = ymasuno + f_euler (tn [i][0], yn.column (i)) * h * tableau_rk4 [order][i];
            for i in range(0, n): 
                ysum =  ysum + self.__deriv(kn[i]) * self.tableau_rkf45[n+1,i] * self.h
              
                #calculate ysum for rkf45
                ysum_45 = ysum_45 + self.__deriv(kn[i]) * self.tableau_rkf45[n,i]* self.h

                
            #Calculate s            
            s = 0.0
            #Recta vectorial
            
        
            aux = ysum - ysum_45
            
            #modulo de aux
            aux1 = np.linalg.norm(aux)
           
            aux1 = epsilon / aux1
            
            
            s = 0.84 * (aux1 ** (0.25))
            
            if (math.fabs(s) > 5):
                s = (s/math.fabs(s)) * 5
                
            elif (math.fabs(s) < 0.2):
                s = (s/math.fabs(s)) * 0.2
            
            #end caclulate s
            
            #yfinal =  yant + self.h*ysum
            
            self.stateVectors.append(ysum)
            
            yant = ysum;
            self.h = self.h * s
            
            t = t + self.h
           
            
        
        
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
            
        
         