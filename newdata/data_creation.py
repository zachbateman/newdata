'''
Python module for creating synthetic data sets.
'''
import math
import random
from typing import List, Dict


param_funcs = [
    lambda x: math.factorial(x),
    lambda x: math.frexp(x)[0],
    lambda x: math.exp(x),
    lambda x: math.log(x),
    lambda x: math.log(x, 5),
    lambda x: math.log(x, 10),
    lambda x: math.pow(x, 0.1),
    lambda x: math.pow(x, 0.4),
    lambda x: math.pow(x, 0.75),
    lambda x: math.pow(x, 1.5),
    lambda x: math.pow(x, 2.0),
    lambda x: math.pow(x, 3.0),
    lambda x: math.sqrt(x),
    lambda x: math.acos(x),
    lambda x: math.asin(x),
    lambda x: math.atan(x),
    lambda x: math.cos(x),
    lambda x: math.sin(x),
    lambda x: math.tan(x),
    lambda x: math.acosh(x),
    lambda x: math.asinh(x),
    lambda x: math.atanh(x),
    lambda x: math.cosh(x),
    lambda x: math.sinh(x),
    lambda x: math.tanh(x),
    lambda x: math.erf(x),
    lambda x: math.erfc(x),
    lambda x: math.gamma(x),
    lambda x: math.lgamma(x),
    lambda x: x + (random.random() - 0.5) * x,
    lambda x: 1 / x,
    lambda x: random() * 5 * x,
    lambda x: 0.25 * x,
    lambda x: 0.5 * x,
    lambda x: 0.75 * x,
    lambda x: random.random(),
    ]



class DataCreator():

    def __init__(self,) -> None:
        self.data = [{}, {}, ...]


    def create_data(self, num_params: int=10, num_samples: int=100) -> List[Dict[str, float]]:
        '''Creates a new data set.'''
        # create target parameter

        # create associated parameters

        pass
