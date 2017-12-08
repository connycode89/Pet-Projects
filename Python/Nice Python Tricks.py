# -*- coding: utf-8 -*-
"""
Created on Fri Dec 08 10:23:30 2017

@author: cdonovan
"""

def swap_values(val1, val2):
    """
    Swap the values of val1 and val2
    Args:
        val1, val2 (ints): 2 integer values
    Returns:
        val1, val2 (ints): val1 is the value that val2 originally was an vice versa
    """
    val1 = val1^val2
    val2 = val2^val1
    val1 = val1^val2
    return val1, val2

___________________________________________________________________________________________

# named tuples
import collections

a = collections.namedtuple('Point',['x','y'])
p = a(x=1.0, y=2.0)
p.y

___________________________________________________________________________________________

# default dictionary
from collections import defaultdict
rows_by_date = defaultdict(list)
rows_by_date['a']=2

___________________________________________________________________________________________

# Counter
f = [1,2,3,4]
collections.Counter(f)

___________________________________________________________________________________________

bool(2==1)

___________________________________________________________________________________________

# re matching
import re
re.match('^...','asad')

___________________________________________________________________________________________

# canonical string representation
repr('C:\\Users\\cdonovan\\Desktop\\Goto Meeting Details.txt')[1:-1]

___________________________________________________________________________________________

import time
import sys
for progress in range(100):
  time.sleep(0.1)
  sys.stdout.write("Download progress: %d%%   \r" % (progress) ) 
  sys.stdout.flush()
