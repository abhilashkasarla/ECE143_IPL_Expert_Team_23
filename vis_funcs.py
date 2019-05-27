"""
Visualization Functions.

This file provides the visualization functions for the provided metrics.
"""

import os
import pandas as pd
from metrics import *


def load_data_as_df(fname):
    """
    Loads the specified file as a PD Data frame
    :param fname: Filename to load
    :return: Pandas Data Frame of the file
    """

    assert isinstance(fname, str), "Invalid file name"
    assert os.path.isfile(fname), "File does not exist"

    return pd.read_csv(fname)


def create_player_team_map(fname):
    pass


def vis_intro_params(fname):
    """
    Creates Visualization for Intro Section
    :param fname: File name to visualize from
    """

    ball_data = load_data_as_df(fname)
    hh = hard_hit(ball_data.copy())
    fs = fast_scoring(ball_data.copy())
    eco = economy(ball_data.copy())
    wick = wicket_taking(ball_data.copy())


if __name__ == '__main__':
    vis_intro_params('./data_csv_kaggle/deliveries.csv')

    a=1
