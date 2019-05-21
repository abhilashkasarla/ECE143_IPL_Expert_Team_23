import random
import os,subprocess
import requests
from bs4 import BeautifulSoup

user_agents = [
    'Mozilla/5.0 (Windows; U; Windows NT 5.1; it; rv:1.8.1.11) Gecko/20071127 Firefox/2.0.0.11',
    'Opera/9.25 (Windows NT 5.1; U; en)',
    'Mozilla/4.0 (compatible; MSIE 6.0; Windows NT 5.1; SV1; .NET CLR 1.1.4322; .NET CLR 2.0.50727)',
    'Mozilla/5.0 (compatible; Konqueror/3.5; Linux) KHTML/3.5.5 (like Gecko) (Kubuntu)',
    'Mozilla/5.0 (Windows NT 5.1) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.142 Safari/535.19',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.7; rv:11.0) Gecko/20100101 Firefox/11.0',
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.6; rv:8.0.1) Gecko/20100101 Firefox/8.0.1',
    'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/535.19 (KHTML, like Gecko) Chrome/18.0.1025.151 Safari/535.19',
 	'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:41.0) Gecko/20100101 Firefox/41.0'
]
# all column names stored in columnNames

def get_information1(url):
    '''
    :param url: url for the overall information for certain year
    :return: return the 8 team overall performance stored inside a list (actualValues)
    '''
    actualValues = []
    headers = {'User-Agent': user_agents[random.randint(0, 8)]}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    html = r.text.encode("utf8")
    soup = BeautifulSoup(html, "lxml")
    ex = soup.find('table', attrs={'class': "table table--scroll-on-tablet top-players"})
    playerResults = ex.findAll('tr')
    columnInformation = playerResults.pop(0).findAll("th")

    #remove the first column as unneeded information
    columnInformation.pop(0)
    #all column names stored in columnNames, only do it if the columnNames has not been filled yet
    if len(columnNamesBatting)==0:
        for information in columnInformation:
            if information.text!="":
                columnNamesBatting.append(information.text.replace(" ","").replace("\n",""))
    #use actualValues to store values for each player
    for playerResult in playerResults:
        tempValues = []
        values = playerResult.findAll('td')
        values.pop(0)
        name = values.pop(0).find('div',attrs={"class":"top-players__player-name"}).text
        while "  " in name:
            name=name.replace("  "," ")
        tempValues.append(name.replace("\n","").strip())
        for value in values:
            tempValues.append(value.text.replace("\n","").strip())
        actualValues.append(tempValues)
    return actualValues

def get_information2(url):
    '''
    :param url: url for the overall information for certain year
    :return: return the 8 team overall performance stored inside a list (actualValues)
    '''
    actualValues = []
    headers = {'User-Agent': user_agents[random.randint(0, 8)]}
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    html = r.text.encode("utf8")
    soup = BeautifulSoup(html, "lxml")
    ex = soup.find('table', attrs={'class': "table table--scroll-on-tablet top-players"})
    playerResults = ex.findAll('tr')
    columnInformation = playerResults.pop(0).findAll("th")

    #remove the first column as unneeded information
    columnInformation.pop(0)
    #all column names stored in columnNames, only do it if the columnNames has not been filled yet
    if len(columnNamesBowling)==0:
        for information in columnInformation:
            if information.text!="":
                columnNamesBowling.append(information.text.replace(" ","").replace("\n",""))
    #use actualValues to store values for each player
    for playerResult in playerResults:
        tempValues = []
        values = playerResult.findAll('td')
        values.pop(0)
        name = values.pop(0).find('div',attrs={"class":"top-players__player-name"}).text
        while "  " in name:
            name=name.replace("  "," ")
        tempValues.append(name.replace("\n","").strip())
        for value in values:
            tempValues.append(value.text.replace("\n","").strip())
        actualValues.append(tempValues)
    return actualValues


valueDictBatting = {}
valueDictBowling = {}
columnNamesBatting = []
columnNamesBowling = []
def main():
    #retrieve data from 2008 to 2018
    for year in range(2008,2018):
        #get the website url for each year
        urlBatting="https://www.iplt20.com/stats/"+str(year)+"/most-runs"
        urlBowling="https://www.iplt20.com/stats/"+str(year)+"/most-wickets"
        valueDictBatting[year] = get_information1(urlBatting)
        valueDictBowling[year] = get_information2(urlBowling)
    print("=========================Batting===========================")
    print("column names:")
    print(columnNamesBatting)
    for number in range(2008,2018):
        print("data for year "+str(number)+":")
        print(valueDictBatting[number])
    print("=========================Bowling===========================")
    print("column names:")
    print(columnNamesBowling)
    for number in range(2008,2018):
        print("data for year "+str(number)+":")
        print(valueDictBowling[number])
if __name__ == '__main__':
    main()