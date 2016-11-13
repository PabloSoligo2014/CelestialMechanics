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
        
        cls.GM = 398600.448
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
        plt.plot(x, z)
        plt.show()
        
        
    def __deriv(self, stateVector):
        
        mod = np.linalg.norm(stateVector); 
        
        
        coeff = -(self.GM)/mod**3
        stateVector[0] = stateVector[3]
        stateVector[1] = stateVector[4]
        stateVector[2] = stateVector[5]
        stateVector[3] = stateVector[0]*coeff
        stateVector[4] = stateVector[1]*coeff
        stateVector[5] = stateVector[2]*coeff
        
        return stateVector;
        
    def RK4(self, time):
        """
        RK4 hardcodeando las 4 derivaciones, sin uso de bucle
        """
        
        yant = self.stateVector;
        for t in range(0, time, self.h):
            
            y0 = yant
            k0 = self.__deriv(y0)
            
            y1 = y0 + (0.5*self.h)*k0
            k1 = self.__deriv(y1)
            
            y2 = y0 + (0.5*self.h)*k1
            k2 = self.__deriv(y2)
            
            y3 = y0 + (0.5*self.h)*k2
            k3 = self.__deriv(y3)
            
            yfinal =  y0 + (self.h/6.0)*(k0+ k1*2 + k2*2 + k3);

            self.stateVectors.append(yfinal)
            yant = yfinal;
            
        
                   
        
        
                
        
        """       
        _matrix _propagators::f_rk (double t, _matrix y) {

    _matrix m (N_ELEM_VECTOR, 1);
    double d;
    const double GM = 398600.448;
    double d3;
    _vector3d a_man;

    m [0][0] = y [3][0];
    m [1][0] = y [4][0];
    m [2][0] = y [5][0];
    d = sqrt (y [0][0] * y [0][0] + y [1][0] * y [1][0] + y [2][0] * y [2][0]);
    d3 = d * d * d;
    m [3][0] = - GM * y [0][0] / d3;
    m [4][0] = - GM * y [1][0] / d3;
    m [5][0] = - GM * y [2][0] / d3;
    m [6][0] = 0;



    if (mans.current != NULL){
        if ((t >= mans.current->mjd) && (t < (mans.current->mjd + mans.current->duration / 86400.0))){
            a_man = mans.current->dv * mans.current->thrust / y [6][0];
            m [6][0] = mans.current->flow_rate;
            m [3][0] = m [3][0] + a_man.x;
            m [4][0] = m [4][0] + a_man.y;
            m [5][0] = m [5][0] + a_man.z;
            }
        }
    return (m);
    }
    
    void _propagators::rk4 (_geoscx_time _t0, _cartesian c0, double h, _geoscx_time _tf)
    {
    double t;
    const int order = 4;
    _matrix yprima (6, 1);
    _matrix y (N_ELEM_VECTOR, 1), ymasuno (N_ELEM_VECTOR, 1);
    _matrix k (N_ELEM_VECTOR, order);
    _matrix yn (N_ELEM_VECTOR, order);
    _matrix tn (order, 1), f (N_ELEM_VECTOR, 1);
    _svec *p;
    int i, j, tt;

    y0.mjd = _t0.mjd ();
    y0.c = c0;
    y0.mass = mass;
    tf = _tf;
    reset ();

    y = y0.matrix ();
    p = new _svec (y);
    p->mjd = y0.mjd;
    add (p);

    for (t = y0.mjd; (t < tf.mjd ()); t += h / 86400.0)
        {
        // compute tn,i
        for (i = 0; (i < order); i ++)
            tn [i][0] = t + h / 86400.0 * tableau_rk4 [i][0];


        yn.clear ();
        // compute yn,i
        for (i = 0; (i < order); i ++) {
            for (tt = 0; (tt < N_ELEM_VECTOR); tt ++)
                yn [tt][i] = y [tt][0];

            for (j = 0; (j < order); j ++){

                if (tableau_rk4 [i][j + 1] != 0){
                    f = f_rk (tn [j][0], yn.column (j)) * h * tableau_rk4 [i][j + 1];
                    for (tt = 0; (tt < N_ELEM_VECTOR); tt ++)
                        yn [tt][i] = yn [tt][i] + f [tt][0];
                }
            }

        }
    // compute ymasuno

        ymasuno = y;
        for (i = 0; (i < order); i ++){
            ymasuno = ymasuno + f_euler (tn [i][0], yn.column (i)) * h * tableau_rk4 [order][i];
        }

        p = new _svec (ymasuno);
        p->mjd = t + h / 86400.0;
        add (p);
        y = ymasuno;
    }
    pack ();
}
"""