import random
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

def get_information(url):
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
    ex = soup.find('table', attrs={'class': "wikitable sortable"});
    playerResults = ex.findAll('tr')
    columnInformation = playerResults.pop(0).findAll("th")
    for information in columnInformation:
        if information.text != "":
            columnNames.append(information.text.replace("\n",""))
    columnNames.insert(1,"birthday")
    #use actualValues to store values for each team
    for teamResult in playerResults:
        tempValues = []
        values = teamResult.findAll('td')
        player = values.pop(0)
        print(player.text.strip())
        #append the player name here
        tempValues.append(player.text.strip())
        #get the wiki link for that player
        if player.find('a', href=True)!=None:
            playerURL = "https://en.wikipedia.org/"+player.find('a', href=True)['href']
            r2 = requests.get(playerURL, headers=headers)
            if r2!=None and r2.status_code!=404:
                r2.raise_for_status()
                html2 = r2.text.encode("utf8")
                soup2 = BeautifulSoup(html2, "lxml")
                birthday = soup2.find('span', attrs={'class': "bday"})
                if birthday!=None:
                    tempValues.append(birthday.text)
                else:
                    tempValues.append("NaN")
            else:
                tempValues.append("NaN")
        else:
            tempValues.append("NaN")


        for value in values:
            temp = value.text.replace("\xa0","").replace("\n","")
            if temp!="":
                tempValues.append(temp)
            else:
                tempValues.append("NaN")
        while len(tempValues)!=len(columnNames):
            tempValues.append("NaN");
        actualValues.append(tempValues)
    return actualValues

valueDict = []
columnNames = []
def main():
    file = open("players_wiki.csv", "a")
    id = 1

    #get the website url
    url = "https://en.wikipedia.org/wiki/List_of_Indian_Premier_League_players"
    valueDict = get_information(url)
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
if __name__ == '__main__':
    main()



