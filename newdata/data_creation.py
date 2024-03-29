'''
Python module for creating synthetic data sets.
'''
import os
import csv
import math
import random
from typing import List, Dict


param_funcs = [
    lambda x: math.factorial(abs(x) ** 0.1 // 1),
    lambda x: math.frexp(x)[0],
    lambda x: math.log(abs(x) + 0.1),
    lambda x: math.log(abs(x) + 0.1, 5),
    lambda x: math.log(abs(x) + 0.1, 10),
    lambda x: math.pow(x, 1),
    lambda x: math.pow(x, 2),
    lambda x: math.pow(x, 3),
    lambda x: math.sqrt(abs(x)),
    lambda x: math.atan(x),
    lambda x: math.cos(x),
    lambda x: math.sin(x),
    lambda x: math.tan(x),
    lambda x: math.erf(x),
    lambda x: math.erfc(x),
    lambda x: math.gamma((abs(x) + 0.1) ** 0.1),
    lambda x: math.lgamma((abs(x) + 0.1) ** 0.1),
    lambda x: x + (random.random() - 0.5) * x,
    lambda x: 1 / x if x != 0 else 1 / 0.00001,
    lambda x: random.random() * 5 * x,
    lambda x: x ** random.random(),
    lambda x: 0.25 * x,
    lambda x: 0.5 * x,
    lambda x: 0.75 * x,
    lambda x: random.random(),
    lambda x: x ** 2 - x
    ]
negative_param_funcs = [lambda x: -f(x) for f in param_funcs]
param_funcs = param_funcs + negative_param_funcs

def rand_func():
    if random.random() < 0.5:
        return random.choice(param_funcs)
    else:  # combine two functions to create a new function
        f1 = random.choice(param_funcs)
        f2 = random.choice(param_funcs)
        return lambda x: f2(f1(x)) if not isinstance(f1(x), complex) else f2(f1(x).real)


def fuzzify(x, factor: float=0.5) -> float:
    '''
    Randomly change given number a bit to add noise/fuzz to data.
    factor is float [0 < factor < 1] that adjusts how much fuzz.
    '''
    if isinstance(x, complex):
        x = x.real
    try:
        return x * (random.random() + 0.5) ** (factor + 0.1)
    except OverflowError:
        if x > 0:
            return 10 ** 10
        else:
            return -10 ** 10


class DataCreator():

    def __init__(self, num_params: int=10, num_samples: int=100) -> None:
        self.num_params = num_params
        self.num_samples = num_samples
        self.data = self.create_data(num_params, num_samples)  # [{}, {}, ...]


    def create_data(self, num_params: int=10, num_samples: int=100) -> List[Dict[str, float]]:
        '''Creates a new data set.'''
        # create initial data set structure with target values
        target_func = rand_func()
        min_initial_target = -random.random() * 10
        max_initial_target = random.random() * 10
        initial_values = [random.uniform(min_initial_target, max_initial_target) for _ in range(num_samples)]
        target_values = [fuzzify(target_func(x) if not isinstance(target_func(x), complex) else target_func(x).real)
                         for x in initial_values]
        data = [{'Target': x} for x in target_values]

        # create associated parameters
        for i in range(1, num_params + 1):
            param = f'Param_{i}'
            fuzz_factor = random.random()
            param_func = rand_func()
            for index, d in enumerate(data):
                value = fuzzify(param_func(d['Target']), fuzz_factor)
                if isinstance(value, complex):
                    value = value.real
                d[param] = value

        return data


    def save_data_as_pymodule(self, module_name='newdata_set.py') -> None:
        '''
        Create a string which creates a Python module with
        self's created data as an importable list.
        '''
        s = "'''\nPython module with a synthetic data set created by newdata.\n"
        s += f"Number of Parameters: {self.num_params}\n"
        s += f"Number of Samples: {self.num_samples}\n'''\n\n"

        s += f"data = [\n"
        for d in self.data:
            s += f"  {str(d)},\n"
        s += "  ]\n"

        with open(os.path.join('.', module_name), 'w') as f:
            f.write(s)
        print(f'New synthetic data saved to {module_name}!')


    def save_data_as_csv(self, csv_filename='newdata_set.csv') -> None:
        '''
        Output a CSV file with the synthetic data set.
        '''
        with open(csv_filename, 'w', newline='') as f:
            keys = self.data[0].keys()
            dict_writer = csv.DictWriter(f, keys, delimiter=',')
            dict_writer.writeheader()
            dict_writer.writerows(self.data)
