

import pandas as pd
import numpy as np
import os
'''
This file provides a few helper functions

It is divided in the following sections:
Sections:

Section 1: provides the info of the winners over the years
'''

def get_winners():
    '''
    provides the info of the winners over the years
    '''
    group_names=['CSK', 'MI', 'KKR', 'DCH', 'SRH', 'RR']
    group_size=[3,4,2,1,1,1]
    subgroup_names=['2010', '2011', '2018', '2013', '2015', '2017', '2019', '2012', '2014', '2009', '2016', '2008']
    subgroup_size=[1,1,1,1,1,1,1,1,1,1,1,1]
    return [group_names, group_size, subgroup_names, subgroup_size]
