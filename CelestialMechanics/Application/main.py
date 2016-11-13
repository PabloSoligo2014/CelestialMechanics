'''
Created on 24 de oct. de 2016

@author: pabli
'''

from Models.Propagator import Propagator
import numpy as np

from math import *

#3.986004418(9)×10**14

mu = 398600.0
earthRadius = 6378.0

def ej1():
    rapogeo = 42164.0
    alturaperigeo = 250.0
    rperigeo = earthRadius+alturaperigeo
    
    
    
    argumentoperigeo = 0
    inclinacion = 7.0
    
    
        
    semieje = (rapogeo+rperigeo)/2.0    
    
    
     
    #Terminar...    
    vapogeo = sqrt(mu*(2/rapogeo - 1/semieje));
    vperigeo = sqrt(mu*(2/rperigeo - 1/semieje));
    
    #Para calcular el deltav debo usar formula con semieje...
    
    
    print("Velocidades: ", vapogeo, vperigeo)
    
    vfinal = sqrt(mu*(2/rapogeo - 1/rapogeo));
    
    print("vfinal: ", vfinal) #Da bien...
    


def ej2():
    alturaperigeo = 250.0
    rperigeo = earthRadius+alturaperigeo
    rapogeo = 82000.0
    
    
    
    
    argumentoperigeo = 0
    inclinacion = 7.0
    
    
        
    semieje = (rapogeo+rperigeo)/2.0    
    
    
     
    #Terminar...    
    vapogeo = sqrt(mu*(2/rapogeo - 1/semieje));
    vperigeo = sqrt(mu*(2/rperigeo - 1/semieje));
    
    #Para calcular el deltav debo usar formula con semieje...
    
    
    print("Velocidades: ", vapogeo, vperigeo)
    
    vfinal = sqrt(mu*(2/rapogeo - 1/rapogeo));
    
    print("vfinal: ", vfinal) #Da bien...
    
    #Cambio de inclinacion en el apageo
    
    
    
    



if __name__ == '__main__':
    
    sv = np.array([42164.0, 0.0, 0.0, 0.0, 1.5, 0.0])
    
    p = Propagator.create(sv, 100)
    
    p.RK4(94000)
    
    
    p.plot()
    #pass
    
    """
    ej1()
    print("---------------------------------------------")
    print("Ejercicio 2")
    print("---------------------------------------------")
    ej2()
    
    """
   
    
    
    
    
    
    
    
    
    
    
    
    
    