import pandas as pd
"""
Calculate different Metrics

This file provides functions to calculate various metrics
related to the game of cricket.

It is divided in the following sections:

Sections:

1. Batsmen Metrics
    - Hard Hitting Ability
2. Bowler Metrics
3. Match Metrics
"""

"""
Section I: Batting Metrics
"""


def hard_hit(data, batter='batsman', runs='batsman_runs', asc=False):
    """
    Calculates the hard hitting ability from given data.

    This is defined as follows:
        >> Hard Hitting Ability = (Fours + Sixes) / Balls Played by batsman

    :param data: Data to calculate from
    :param batter: Column with batsman info
    :param runs: Column with runs scored info
    :param asc: ascending order sorted
    :return: Hard Hitting Ability Data Frame
    """

    assert isinstance(data, pd.DataFrame), "Data format is invalid"
    data.drop(data.columns.difference([batter, runs]), 1, inplace=True)

    # Calculate required info for stat
    balls = data.groupby(batter).count().reset_index()
    balls = balls.rename(columns={runs: 'plays'})

    fours = data[data[runs] == 4].groupby(batter).count().reset_index()
    fours = fours.rename(columns={runs: 'fours'})

    sixes = data[data[runs] == 6].groupby(batter).count().reset_index()
    sixes = sixes.rename(columns={runs: 'sixes'})

    # Merge Data into single Frame
    balls = pd.merge(balls, fours, on=batter, how='outer')
    balls = pd.merge(balls, sixes, on=batter, how='outer')
    balls.fillna(0, inplace=True)

    # Calculate Hard Hit
    balls.eval('hh = (fours + sixes) / plays', inplace=True)

    # Beautify
    balls.sort_values('hh', ascending=asc, inplace=True)
    balls = balls.rename(columns={'hh': 'Hard Hit', 'plays': 'Number of Balls Faced'})

    return balls


def fast_scoring(data, batter='batsman', runs='batsman_runs', asc=False):
    """
    Calculates fast scoring ability from the given data
    This is defined as follows:
        >> Total Runs / Balls Played by Batsman
    :param data: Data to calculate from
    :param batter: Column with batsman info
    :param runs: Column with runs scored info
    :param asc: ascending order sorted
    :return: Hard Hitting Ability Data Frame
    """

    assert isinstance(data, pd.DataFrame), "Data format is invalid"
    data.drop(data.columns.difference([batter, runs]), 1, inplace=True)

    # Calculate required info for stat
    balls = data.groupby(batter).count().reset_index()
    balls = balls.rename(columns={runs: 'plays'})

    run_score = data.groupby(batter).sum().reset_index()
    run_score = run_score.rename(columns={runs: 'runs'})

    # Merge Data into single Frame
    balls = pd.merge(balls, run_score, on=batter, how='outer')
    balls.fillna(0, inplace=True)

    # Calculate Fast Scoring
    balls.eval('fs =  runs / plays', inplace=True)

    # Beautify
    balls.sort_values('fs', ascending=asc, inplace=True)
    balls = balls.rename(columns={'fs': 'Fast Scoring', 'plays': 'Number of Balls Faced'})

    return balls


"""
Section II: Bowling Metrics
"""


def economy(data, bowler='bowler', runs='batsman_runs', asc=True):
    """
    Calculates economy of bowler from the given data
    This is defined as follows:
        >> Economy = Runs Conceded / Number of Overs
    :param data: Data to calculate from
    :param bowler: Column with bowler info
    :param runs: Column with runs scored info
    :param asc: ascending order sorted
    :return: Hard Hitting Ability Data Frame
    """

    assert isinstance(data, pd.DataFrame), "Data format is invalid"
    data.drop(data.columns.difference([bowler, runs]), 1, inplace=True)

    # Calculate required info for stat
    balls = data.groupby(bowler).count().reset_index()
    balls = balls.rename(columns={runs: 'plays'})
    balls['overs'] = balls['plays']/6

    run_score = data.groupby(bowler).sum().reset_index()
    run_score = run_score.rename(columns={runs: 'runs'})

    # Merge Data into single Frame
    balls = pd.merge(balls, run_score, on=bowler, how='outer')
    balls.fillna(0, inplace=True)

    # Calculate Economy
    balls.eval('eco =  runs / overs', inplace=True)

    # Beautify
    balls.sort_values('eco', ascending=asc, inplace=True)
    balls = balls.rename(columns={'eco': 'Economy', 'plays': 'Number of Balls Thrown'})

    return balls


def wicket_taking(data, bowler='bowler', wicket='dismissal_kind', out_kind=None, asc=True):
    """
    Measure of wicket taking ability
    This is defined as follows:
        >> Wicket Taking Ability = Number of balls bowled / Wickets Taken
    :param data: Data to calculate from
    :param bowler: Column with bowler info
    :param wicket: Column with wicket info
    :param out_kind: Values to consider for out
    :param asc: Ascending Sort
    :return: Wicket Taking ability Data Frame
    """
    assert isinstance(data, pd.DataFrame), "Data format is invalid"
    data.drop(data.columns.difference([bowler, wicket]), 1, inplace=True)

    if out_kind is None:
        out_kind = ['caught', 'bowled', 'run out', 'lbw', 'caught and bowled', 'stumped']

    # Calculate required info for stat
    balls = data[bowler].value_counts().reset_index()
    balls = balls.rename(columns={bowler: 'balls', 'index': bowler})

    wickets = data[data[wicket].isin(out_kind)]['bowler'].value_counts().reset_index()
    wickets = wickets.rename(columns={bowler: 'wickets', 'index': bowler})

    # Merge Data into single Frame
    wickets = pd.merge(balls, wickets, on=bowler, how='inner')

    # Calculate Wickets Taken
    wickets = wickets.eval('wtaken = balls / wickets')

    # Beautify
    wickets.sort_values('wtaken', ascending=asc, inplace=True)
    wickets.rename(columns={'balls': 'Number of Balls Thrown', 'wickets': 'Number of Wickets taken',
                            'wtaken': 'Wicket Taking Ability'})

    return wickets
