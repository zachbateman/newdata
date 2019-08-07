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
    lambda x: math.pow(x, 1),
    lambda x: math.pow(x, 2),
    lambda x: math.pow(x, 3),
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
negative_param_funcs = [lambda x: -f(x) for f in param_funcs]
param_funcs = param_funcs + negative_param_funcs

def rand_func():
    if random.random() < 0.5:
        return random.choice(param_funcs)
    else:  # combine two functions to create a new function
        f1 = random.choice(param_funcs)
        f2 = random.choice(param_funcs)
        return lambda x: f2(f1(x))


def fuzzify(x, factor: float=0.5) -> float:
    '''
    Randomly change given number a bit to add noize/fuzz to data.
    factor is float [0 < factor < 1] that adjusts how much fuzz.
    '''
    return x * (random.random() + 0.5) ** (factor + 0.1)


class DataCreator():

    def __init__(self, num_params: int=10, num_samples: int=100) -> None:
        self.data = self.create_data(num_params, num_samples)  # [{}, {}, ...]


    def create_data(self, num_params: int=10, num_samples: int=100) -> List[Dict[str, float]]:
        '''Creates a new data set.'''
        # create initial data set structure with target values
        target_func = rand_func()
        min_initial_target = -random.random() * 10
        max_initial_target = random.random() * 10
        initial_values = [random.uniform(min_initial_target, max_initial_target) for _ in range(num_samples)]
        target_values = [fuzzify(target_func(x)) for x in initial_values]
        self.data = [{'Target': x} for x in target_values]

        # create associated parameters
        for i in range(1, num_params + 1):
            param = f'Param_{i}'
            fuzz_factor = random.random()
            param_func = rand_func()
            for index, d in enumerate(self.data):
                d[param] = fuzzify(param_func(d['target']), fuzz_factor)
