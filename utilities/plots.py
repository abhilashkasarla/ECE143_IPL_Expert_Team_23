#!/usr/bin/env python
# coding: utf-8

# In[4]:


import pandas as pd
import numpy as np
import os
'''
This file provides functions to calculate various metrics
related to the game of cricket.

It is divided in the following sections:
Sections:

Section 1 : The abbreviation of each team
Section 2 : The table of head to head winning rate table
Section 3 : Represent the rank of each team from 2008 to 2019
Section 4 : Represent the age of each team in 2018
'''
def sort_name(team_name):
    '''
    shorten the name of teams
    :param team_name: The name of each team
    :return: The abbreviation of each team
    '''
    assert type(team_name) == list
    team_name_sort = []
    for i in range(len(team_name)):
        l1 = team_name[i].split()
        lala = l1[0] + ' '
        for j in range(1,len(l1)):
            lulu = l1[j][0]
            lala = lala + lulu+'.'
        a = ''.join(lala)
        team_name_sort.append(a)
    return team_name_sort


# In[5]:


def win_heatmap(grp,team_name):
    '''
    get the table of heatmap
    :param team_name: The name of each team
                 grp: the table group by 'team1'
    :return: The table of head to head winning rate table
    '''
    result = [[0]*8 for x in range(8)]
    total_win = []

    for (i,m) in enumerate(team_name):
        grp1 = grp.get_group(m)
        grp2 = grp1.groupby('team2')
        p = 0
        q = 0
        for (j,n) in enumerate(team_name):
            grp4 = grp.get_group(n)
            grp5 = grp4.groupby('team2')
            num_1 = list(grp1['team2']).count(n)
            num_2 = list(grp4['team2']).count(m)
            if m == n or num_1 == 0 or num_2 == 0:
                result[i][j] = '-'
            else:
                grp3 = grp2.get_group(n)
                grp6 = grp5.get_group(m)
                result[i][j] = (list(grp3['winner']).count(m)+list(grp6['winner']).count(m))/                                         (len(list(grp3['winner']))+len(list(grp6['winner'])))
                p = p + list(grp3['winner']).count(m)+list(grp6['winner']).count(m)
                q = q + len(list(grp3['winner']))+len(list(grp6['winner']))
        total_win.append(p/q)
    return result,total_win


# In[6]:


def rank(file):
    '''
    represent the rank of each team from 2008 to 2019
    '''
    team_name = ['Royal Challengers Bangalore','Kings XI Punjab','Mumbai Indians','Kolkata Knight Riders',                 'Chennai Super Kings','Delhi Capitals','Rajasthan Royals','Sunrisers Hyderabad']
    year = sorted(list(set(file['year'])))
    grp = file.loc[:,['year','Team']]
    grp1 = grp.groupby('year')
    result = [[0]*len(year) for x in range(len(team_name))]

    for i in range(len(year)):
        grp2 = grp1.get_group(year[i])
        for j in range(len(team_name)):
            if team_name[j] in list(grp2['Team']):
                result[j][i] = list(grp2['Team']).index(team_name[j]) + 1
            else:
                result[j][i] = '-'
    return result


# In[7]:


def age(grp,team):
    '''
    represent the age of each team in 2018
    '''
    result = [[],[]]
    for i in team:
        grp2 = grp.get_group(i)
        result[0].append(min(list(grp2['age_2018'])))
        result[1].append(max(list(grp2['age_2018'])))
    return result

