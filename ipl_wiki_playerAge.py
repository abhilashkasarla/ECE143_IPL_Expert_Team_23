import csv
'''
Use the players_wiki.csv file generated by ipl_wiki_players_info.py
Calculate the average age for each team in each years
The result will be written into players_age_wiki.py
'''
def main():
    # prepare a dictionary to store data according to years
    resultDict = {}
    # get all past/current team names in the league
    teamNames = set()
    for year in range(2008,2020):
        #for each year, resultDict[year] will also be a dictionary
        resultDict[year] = {}
    #open players_wiki.csv to read for data
    with open('players_wiki.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        id = 0
        #proecess with each row (each player)
        #ignore the first row since it only contains column names
        for row in csvReader:
            if id==0:
                id = 1
                continue
            #row[2] is for this player's birthday
            #if this information is missing, simply skip over this player
            if row[2]=="NaN":
                continue
            #get the birth year
            birthYear = int(row[2].split("/")[0])
            #get the team name that this player played for in specific year
            #stored into the dictionary
            for year in range(2008,2020):
                index = 4+year-2008
                #if this teamname has not been registered in
                #teamNames yet
                if row[index]!="NaN":
                    teamNames.add(row[index])
                #if this team has been registered in the
                #dictionary for average age in that year
                #the information is stored in the format (age sum)+(player count)
                if row[index] in resultDict[year]:
                    value = resultDict[year][row[index]]
                    temp = value.split("+")
                    sum = int(temp[0])
                    count = int(temp[1])
                    sum = sum + year - birthYear
                    count = count + 1
                    resultDict[year][row[index]] = str(sum)+"+"+str(count)
                # if this team has not been registered in the
                # dictionary for average age in that year
                else:
                    sum = year - birthYear
                    count = 1
                    resultDict[year][row[index]] = str(sum) + "+" + str(count)
    #after collecting all information, open the file in which we will write the data
    file = open("players_age_wiki.csv", "a")
    id = 1
    #prepare column names
    temp = "id,team_name"
    for year in range(2008,2020):
        temp = temp+","+str(year)
    file.write(temp+"\n")

    #start writing in the actual data
    for team in teamNames:
        temp = str(id)+","+team
        for year in range(2008, 2020):
            if team in resultDict[year]:
                #get the data for that team in that year
                dataStr = resultDict[year][team]
                #doing the string processing
                tempList = dataStr.split("+")
                #tempList[0] will be sum of age
                #tempList[1] will be number of players
                #calculate the average age
                temp = temp+"," + str(int(tempList[0])/int(tempList[1]))
            #only if this team did not play in that year
            else:
                temp = temp + ","+"NaN"
        file.write(temp+"\n")
        id = id + 1
    #finish writing the data
    file.close()

if __name__ == '__main__':
    main()
