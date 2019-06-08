# ECE143_IPL_Expert_Team_23
To Analyze IPL data from 2008 to 2019 and to provide interesting insights into players attributes and Teams performance
# Scraping data (By Zicong Zhang):
1) Most of the matches data and seasonal overviews comes from https://www.iplt20.com/ either under “Archive” or “Stats”
We are getting more data from Wikipedia for players’ detailed information
https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_players 
2) Imported libraries:
import requests
import json
from bs4 import BeautifulSoup
import random
import csv
3) To scrape all the data, use Chrome browser’s developer tools (F12) to look for the data section we want and useful url request as well as its parameter for requesting data.
4) For JSON type responses, use Postman for better visualization.
5) Simulate the url request in Python by using BeautifulSoup and requests library.
6) For table elements, treat them as list with index.
7) For JSON elements, transform to dictionary and use key string to get value.
8) All data value will be processed (e.g remove extra space, deal with comma, handle for empty value or invalid response data), and then saved into .csv files for later evaluation.

Brief Introduction to all files (check comments inside each files for more detailed introduction)

-ipl_match_result.py
collect each match result from 2012 to 2018(2013 excluded) into
match_result.csv

-ipl_player_performance.py
collect all batting players and bowling players information now or in the past into 
player_batting_performance.csv
player_bowling_performance.csv

-ipl_team_leader.py
collect all current/past captains information for all teams inside the league into
leader_wiki1.csv
leader_wiki2.csv

-ipl_team_performance.py
collect seasonal performance conclusion for all teams played in the league into
team_performance.csv

-ipl_wiki_players_info.py
collect the current team or past team for each player and the player's current age into 
players_wiki.csv

-ipl_wiki_playerAge.py
use the players_wiki.csv to calculate the average for each team in each season into
players_age_wiki.csv

