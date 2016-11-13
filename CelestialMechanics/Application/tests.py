'''
Created on 24 de oct. de 2016

@author: pabli
'''
import unittest
from Models.Satellite import Satellite

class Test(unittest.TestCase):


    def testName(self):
        sat = Satellite()
        sat.setPosition(-8900, -1690, 5210, -6, -4.5, -1.5)
        sat.setVelocity(-6, -4.5, -1.5)
        
        print(sat.getAltitude())
        print(sat.velocity)
        print(sat.earthCenterDistance)
        
        print("El semi eje del satelite es : ",  sat.a)
        
        print("El periodo del satelite es : ",  sat.getPeriod()/60)
        
        print("El vector h es : ",  sat.vh)
        print("El vector e es : ",  sat.ve)
        print("La exentrincidad es :", sat.e)
        

        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()