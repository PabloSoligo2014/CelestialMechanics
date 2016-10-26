'''
Created on 24 de oct. de 2016

@author: pabli
'''

import math
import numpy as np

mu = 398600
earthRadius = 6378


class Satellite(object):
    '''
    classdocs
    '''

    earthCenterDistance = 0
    velocity = 0
    energy = 0
    semiMajorAxis = 0
    apogeeDistance = 0
    perigeeDistance = 0
    vh = 0
    vk = np.array([0, 0, 1])
    
    def __init__(self, pd, ad):
        '''
        Constructor
        '''
        self.apogeeDistance = ad
        self.perigeeDistance = pd
        
        
        self.versor_i = np.array([1,0,0]) 
        self.versor_j = np.array([0,1,0])
        self.versor_k = np.array([0,0,1])
        
    def getPeriod(self):
        return 2*math.pi*math.sqrt( ((self.a)**3) / mu )
        
    def getPerigeoPosition(self):
        #la posicion con angulo tita = 0
        pass
        #tita-E-Me-t
            
        
        
    def setPosition(self, ri, rj, rk, vi, vj, vk):
        #self.earthCenterDistance = math.sqrt(i**2 + j**2 + k**2 )
        
        #Fuente 
        #http://space.stackexchange.com/questions/1904/how-to-programmatically-calculate-orbital-elements-using-position-velocity-vecto
        
        self.vr = np.array([ri, rj, rk])#Vector posicion
        self.vv = np.array([vi, vj, vk])#Vector velocidad
        self.vh = self.vr*self.vv
        self.vn = self.vk*self.vh
        self.n = np.linalg.norm(self.vn)
        
        #self.ve = ((self.vv*self.vh)/mu)-(self.vr/self.getRModule())
        
        self.v = np.linalg.norm(self.vv)
        self.r = np.linalg.norm(self.vr)
        
        self.ve =  ( np.dot( (self.v**2-(mu/self.r)), self.vr ) - np.dot( np.dot( self.vr, self.vv ), self.vv) ) / mu
        
        self.e  = np.linalg.norm(self.ve) 
        
        self.h = np.linalg.norm(self.vh) 
        self.p  = (self.h**2)/mu
    
        self.energy = (self.v**2/2) - (mu/self.r)
        
        #solo para self.e != 1
        self.a = -mu/2*self.energy
        
        self.i = np.arccos(np.dot(self.vh,self.versor_k)/self.h)
        self.raan = np.arccos(np.dot(self.vn,self.versor_i)/self.n)
        self.omega =  np.arccos(np.dot(self.vn,self.ve)/self.n*self.e)
        self.tita =  np.arccos(np.dot(self.ve,self.vr)/self.e*self.r)
        
        
        #Calcular self.a
         
        
    def __getVectorModule(self, v):
        
        result = 0
        for e in v:
            result = result+e**2
    
        return math.sqrt(result)
    
    
    def getRModule(self):
        return self.__getVectorModule(self.vr)
        
    
        
    def setVelocity(self, i, j, k):
        self.velocity = math.sqrt(i**2 + j**2 + k**2 )
        
    def getAltitude(self):
        return self.earthCenterDistance-earthRadius
    
    def getEnergy(self):
        return -mu/2*self.semiMajorAxis
    
    def getAngMomentum(self):
        pass
    
    