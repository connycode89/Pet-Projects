# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:40:29 2018

@author: jdonovc
"""

# Python 2.7
# code to do a random draw to put teams into n number of groups
import pandas as pd
from math import floor
import numpy as np

def read_data(path):
    teams = pd.read_csv(path)
    return list(teams['Team Name'])

def determine_format(num_groups, num_teams):
    base_amt_per_grp = int(floor(num_teams/num_groups))
    remainder = num_teams%num_groups
    if remainder==0:
        return [base_amt_per_grp for num in range(num_groups)]
    elif remainder>0:
        first_groups = [base_amt_per_grp+1 for num in range(1, remainder+1)]
        second_groups = [base_amt_per_grp for num in range(1, num_groups-remainder+1)]
        return first_groups+second_groups
    
def randomize(team_col):
    list1 = list(team_col)
    np.random.shuffle(list1)
    return list1
    
def draw(path1, n_groups):
    col1 = read_data(path1)
    format1 = determine_format(n_groups, len(col1))
    rearrange = randomize(col1)
    draw_list = []
    for item in format1:
        first = rearrange[:item]
        draw_list.append(first)
        rearrange = [item for item in rearrange if item not in first]
    return draw_list
    

path = 'C:\\Users\\cdonovan\\Downloads\\Table Tennis Registration.csv.zip'
#path = 'C:\\Users\\Conor\\Downloads\\Table Tennis Registration.csv.zip'
results = draw(path, 3)