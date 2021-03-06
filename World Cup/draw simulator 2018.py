# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 12:47:03 2017

@author: cdonovan
"""

# Python 2.7

import pandas as pd
import numpy as np
import random

def check_allocations(df):
    df2 = df[df['team']>=2]
    if len(df2)==0:
        return True
    elif len(df2)>1:
        return False
    elif len(df2)==1:
        if df2['conf'].values[0]=='UEFA':
            if df2['team']==2:
                return True
            else:
                return False
        else:
            return False

pot1 = [('Russia','UEFA'), ('Germany','UEFA'), ('Brazil','CONMEBOL'), ('Portugal','UEFA'), ('Argentina','CONMEBOL'), ('Belgium','UEFA'), ('Poland','UEFA'), ('France','UEFA')]
pot2 = [('Spain','UEFA'), ('Peru','CONMEBOL'), ('Switzerland','UEFA'), ('England','UEFA'), ('Colombia','CONMEBOL'), ('Uruguay','CONMEBOL'), ('Mexico','CONCACAF'), ('Croatia','UEFA')]
pot3 = [('Denmark','UEFA'), ('Iceland','UEFA'), ('Costa Rica','CONCACAF'), ('Sweden','UEFA'), ('Tunisia','CAF'), ('Egypt','CAF'), ('Senegal','CAF'), ('Iran','AFC')]
pot4 = [('Serbia','UEFA'), ('Nigeria','CAF'), ('Australia','AFC'), ('Japan','AFC'), ('Morocco','CAF'), ('Panama','CONCACAF'), ('South Korea','AFC'), ('Saudi Arabia','AFC')]

df = pd.DataFrame()
num = 1
for item in [pot1,pot2,pot3,pot4]:
    p1 = pd.DataFrame(item, columns=['team','conf'])
    p1['seed'] = [num for num2 in range(len(item))]
    df = df.append(p1)
    num+=1
df = df.reset_index(drop=True)
del item, num, num2, p1, pot1, pot2, pot3, pot4

group_names = ['A','B','C','D','E','F','G','H']
groups = dict([(item,{'group':pd.DataFrame(columns=['team','conf']),'count_conf':pd.DataFrame(),'used_pos':[]}) for item in group_names])

# 1st seeds
s1 = df[df['seed']==1][['team','conf']]
s1_teams = list(s1['team'])
for item in group_names:
    if item=='A':
        s1_teams = filter(lambda x:x!='Russia',s1_teams)
        g_0 = s1[s1['team']=='Russia']
        g_0.loc[:,'pos'] = pd.Series([1],index=g_0.index)
        g = groups[item]['group'].append(g_0)
        groups[item]['group'] = g
        c = g.groupby('conf')['team'].count().reset_index()
        groups[item]['count_conf'] = c
        groups[item]['used_pos'].append(1)
    else:
        t1 = random.choice(s1_teams)
        s1_teams = filter(lambda x:x!=t1,s1_teams)
        g_0 = s1[s1['team']==t1]
        g_0.loc[:,'pos'] = pd.Series([1],index=g_0.index)
        g = groups[item]['group'].append(g_0)
        groups[item]['group'] = g
        c = g.groupby('conf')['team'].count().reset_index()
        groups[item]['count_conf'] = c
        groups[item]['used_pos'].append(1)

# 2nd seeds








##########
# 1st seeds
s1 = df[df['seed']==1][['team','conf']]
t_list = list(s1['team'])
for num in range(len(s1)):
    if num==0:
        g = groups[num][0].append(s1[s1['team']=='Russia'])
        g['pos'] = [1]
        c1 = g.groupby('conf')['team'].count().reset_index()
        groups[num] = g, c1
        t_list = filter(lambda x:x!='Russia',t_list)
    else:
        t1 = random.choice(t_list)
        g = groups[num][0].append(s1[s1['team']==t1])
        g['pos'] = [1]
        c1 = g.groupby('conf')['team'].count().reset_index()
        groups[num] = g, c1
        t_list = filter(lambda x:x!=t1,t_list)
        
# 2nd-4th seeds
for num3 in range(2,5,1):
    s2 = df[df['seed']==num3][['team','conf']]
    t_list = list(s2['team'])
    for num in range(len(s2)):
        t1 = random.choice(t_list)
        g = groups[num][0].append(s2[s2['team']==t1])
        g['pos'] = g['pos'].fillna(random.choice([2,3,4]))
        c1 = g.groupby('conf')['team'].count().reset_index()
        groups[num] = g, c1
        t_list = filter(lambda x:x!=t1,t_list)









######################
groups = [pd.DataFrame(columns=['team','conf']) for num in range(8)]
a = df[df['team']=='Russia'][['team','conf']]
groups[0] = groups[0].append(a)

# 1st seeds
s1 = df[(df['team']!='Russia') & (df['seed']==1)][['team','conf']]
s1_1 = s1.iloc[np.random.permutation(len(s1))].reset_index(drop=True)
for num in range(len(s1_1)):
    groups[num+1] = groups[num+1].append(s1_1.iloc[num])

# 2nd seeds
s2 = df[df['seed']==2][['team','conf']]