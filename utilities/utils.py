

import pandas as pd
import numpy as np
import os
'''
This file provides a few helper functions

It is divided in the following sections:
Sections:

Section 1: replace team names with their latest ones
Section 2: provides the info of the winners over the years
Section 3: computes the number of used players by teams across all years
'''

def preprocess_team_names(df):
    '''method for preprocessing team names
    Replacing team names with their latest ones
    as some teams changed their name in between
    '''
    df.replace('Rising Pune Supergiants', 'Rising Pune Supergiant', inplace=True)
    df.replace('Delhi Daredevils', 'Delhi Capitals', inplace=True)


def get_winners():
    '''
    provides the info of the winners over the years
    '''
    group_names=['CSK', 'MI', 'KKR', 'DCH', 'SRH', 'RR']
    group_size=[3,4,2,1,1,1]
    subgroup_names=['2010', '2011', '2018', '2013', '2015', '2017', '2019', '2012', '2014', '2009', '2016', '2008']
    subgroup_size=[1,1,1,1,1,1,1,1,1,1,1,1]
    return [group_names, group_size, subgroup_names, subgroup_size]

def get_used_players(ball_data):
    '''
    computes the number of used players by teams across all years
    '''
    short_names = {'Chennai Super Kings':'CSK', 'Delhi Capitals': 'DC', 'Kings XI Punjab' :'KXIP', 
               'Mumbai Indians':'MI', 'Rajasthan Royals':'RR', 'Royal Challengers Bangalore':'RCB', 
               'Sunrisers Hyderabad': 'SRH', 'Kolkata Knight Riders': 'KKR'}
    strikers = ball_data[['match_id', 'batting_team', 'batsman']].copy()
    non_strikers = ball_data[['match_id', 'batting_team', 'non_striker']].copy()
    non_strikers.rename(columns={'non_striker':'batsman'}, inplace=True)
    all_batsman = pd.concat([strikers, non_strikers], ignore_index=True)
    all_batsman.rename(columns={'batsman':'player', 'batting_team':'team'}, inplace=True)
    all_bowlers = ball_data[['match_id', 'bowling_team', 'bowler']].copy()
    all_bowlers.rename(columns={'bowler':'player', 'bowling_team':'team'}, inplace=True)
    all_players = pd.concat([all_batsman, all_bowlers], ignore_index=True)
    d = {'match_id':'Total matches', 'player':'Number of players used'}
    all_players = all_players.replace(short_names)
    used_players = all_players.groupby('team').agg({'match_id':pd.Series.nunique, 'player':pd.Series.nunique}).rename(columns=d)
    return used_players
