# -*- coding: utf-8 -*-
"""
Created on Fri Jun 15 13:40:29 2018

@author: jdonovc
"""

# Python 2.7
# code to do a random draw to put teams into n number of groups
import pandas as pd
from math import floor

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
    
determine_format(5,12)

path = 'C:\\Users\\cdonovan\\Downloads\\Table Tennis Registration.csv.zip'