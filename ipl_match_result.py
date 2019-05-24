import requests
import json
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
valueDict = {}
def main():
    file = open("match_result.csv", "a")
    id = 1
    file.write("id,year,team1,team2,match_result,match_winner,toss_winner,action\n")
    dataDict = {}
    #year2018: match id 7894 to 7953
    list2018 = list(range(7894,7954))
    dataDict[2018] = list2018
    #year2017: match id 5839 to 5898
    list2017 = list(range(5839,5899))
    dataDict[2017] = list2017
    #year2016: match id 4042 to 4101
    list2016 = list(range(4042,4102))
    dataDict[2016] = list2016
    #year2015: match id 3226 to 3285
    list2015 = list(range(3226,3286))
    dataDict[2015] = list2015
    #year2014: match id 2424 to 2483
    list2014 = list(range(2424,2484))
    dataDict[2014] = list2014
    #year2012: match id 2 to 77
    list2012 = list(range(2,78))
    dataDict[2012] = list2012
    #for year 2011 or earlier all records had been cleared, data for year 2013 has bad JSON format
    for year in dataDict:
        print("Processing year:"+str(year))
        for matchId in dataDict[year]:
            url = "https://cricketapi.platform.iplt20.com//fixtures/" + str(matchId) + "/scoring"
            r = requests.get(url)
            # print(r.json())
            tempDict = json.loads(r.text)
            team1 = tempDict["matchInfo"]["teams"][0]["team"]["fullName"]
            team2 = tempDict["matchInfo"]["teams"][1]["team"]["fullName"]
            match_winner = "NaN"
            match_result = "NaN"
            if tempDict["matchInfo"]["matchStatus"]["outcome"] == 'A':
                match_winner = team1
                match_result = "Normal"
            elif tempDict["matchInfo"]["matchStatus"]["outcome"] == 'B':
                match_winner = team2
                match_result = "Normal"
            if "Tied" in tempDict["matchInfo"]["matchSummary"]:
                match_result = "Tied"
            if tempDict["matchInfo"]["matchStatus"]["outcome"] == 'N':
                match_result = "NaN"
            toss_winner = "NaN"
            action = "NaN"
            if "toss.winner" in tempDict["matchInfo"]["additionalInfo"]:
                toss_winner = tempDict["matchInfo"]["additionalInfo"]["toss.winner"]
                if " bat" in tempDict["matchInfo"]["additionalInfo"]["toss.elected"]:
                    action = "bat"
                else:
                    action = "field"
            tempStr = str(id) + "," + str(
                year) + "," + team1 + "," + team2 + "," +match_result+ "," + match_winner + "," + toss_winner + "," + action + "\n"
            file.write(tempStr)
            id = id + 1
    #for year 2011 or earlier all records had been cleared, data for year 2013 has bad JSON format
    file.close()


if __name__ == '__main__':
    main()