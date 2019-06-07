# ECE143_IPL_Expert_Team_23
To Analyze IPL data from 2008 to 2019 and to provide interesting insights into players attributes and Teams performance
# Scraping data:
1) Most of the matches data and seasonal overviews comes from https://www.iplt20.com/ either under “Archive” or “Stats”
We are getting more data from Wikipedia for players’ detailed information
https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_players 
2) To scrape all the data, use Chrome browser’s developer tools (F12) to look for the data section we want and useful url request as well as its parameter for requesting data.
3) For JSON type responses, use Postman for better visualization.
4) Simulate the url request in Python by using BeautifulSoup and requests library:
5) For table elements, treat them as list with index
6) For JSON elements, transform to dictionary and use key string to get value
7) All data value will be processed (e.g remove extra space, deal with comma, handle for empty value or invalid response data), and then saved into .csv files for later evaluation.
