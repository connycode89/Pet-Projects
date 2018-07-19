# -*- coding: utf-8 -*-
"""
Created on Thu Jul 19 13:38:34 2018

@author: jdonovc
"""

# Python 3.5
# https://arxiv.org/pdf/1804.04888.pdf

import numpy as np
import pandas as pd
import tensorflow as tf

def create_data():
    np.random.seed(42)
    x = np.random.randint(5, size=2000).reshape((100, 20))
    indices = np.random.choice(range(len(x)), size=10)
    for num in indices:
        x[num] *= 3
    labs = np.array([-1 if item in indices else 1 for item in range(len(x))])
    return x, labs


