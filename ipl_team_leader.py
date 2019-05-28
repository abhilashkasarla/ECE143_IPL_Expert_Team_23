import random
import requests
from bs4 import BeautifulSoup
'''
In this file, we scrape all past/current team leader information from wikipedia
https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_captains
which contains a table for their information
There will be two output files.
leader_wiki1.csv will be the same to the table on the website 
each player will have a row and all his/her leaded team either in the present
or in the past connected with "+" sign

leader_wiki2.csv, however, will only contains information about the player and
his/her leaded teams, and for each one of the team he leaded will take a row:
for example:
player1 team1
player1 team2
player2 team3
...
'''
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
def get_information(url):
    '''
    :param url: url for the overall information for certain year
    :return: return the list of player informations (also represented as list)
    '''
    actualValues = []
    headers = {'User-Agent': user_agents[random.randint(0, 8)]}
    #send out URL request and get the data
    r = requests.get(url, headers=headers)
    r.raise_for_status()
    html = r.text.encode("utf8")
    soup = BeautifulSoup(html, "lxml")
    #process the webpage data, get the target section
    ex = soup.find('table', attrs={'class': "wikitable plainrowheaders sortable"});
    playerResults = ex.findAll('tr')
    columnInformation = playerResults.pop(0).findAll("th")
    for information in columnInformation:
        if information.text != "":
            columnNames.append(information.text.replace("\n",""))
    #use actualValues to store values for each team
    for teamResult in playerResults:
        tempValues = []

        values = teamResult.findAll('td')
        player = teamResult.findAll('th').pop(0)
        print(player.text.strip())
        #append the player name here
        tempValues.append(player.text.strip())
        playerList.append(player.text.strip())
        #write the remaining data into the information list
        for value in values:
            if value.find('a', href=True)!=None:
                teamList = value.findAll("a")
                #save tje team lists into dictionary for leader_wiki2.csv
                teamDict[player.text.strip()] = teamList
                temp = ""
                for team in teamList:
                    if temp!="":
                        temp = temp+"+"+team.text
                    else:
                        temp = team.text
                tempValues.append(temp)
            else:
                temp = value.text.replace("\xa0","").replace("\n","")
                temp = temp.replace(",","+")
                if temp!="":
                    tempValues.append(temp)
                else:
                    tempValues.append("NaN")
        #for some player they didn't attend recent years' competition
        #fill those block with "NaN"
        while len(tempValues)!=len(columnNames):
            tempValues.append("NaN");
        actualValues.append(tempValues)
    return actualValues

valueDict = []
columnNames = []
playerList = []
teamDict = {}
def main():
    file = open("leader_wiki1.csv", "a")
    file2 = open("leader_wiki2.csv", "a")
    id = 1
    #get the website url
    url = "https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_captains"
    valueDict = get_information(url)
    #write for leader_wiki1.csv
    temp = "id"
    for name in columnNames:
        temp = temp+","+name
    file.write(temp+"\n")

    for values in valueDict:
        temp = str(id)
        for value in values:
            temp = temp+","+value
        file.write(temp+"\n")
        id = id + 1
    file.close()
    #write for leader_wiki2.csv
    id = 1
    file2.write("id,name,team\n")
    for player in playerList:
        teamList = teamDict[player]
        for team in teamList:
            file2.write(str(id)+","+player+","+str(team.text)+"\n")
            id = id + 1
    file2.close()
if __name__ == '__main__':
    main()



