import csv
def main():
    resultDict = {}
    teamNames = set()
    for year in range(2008,2020):
        resultDict[year] = {}
    with open('players_wiki.csv') as csvDataFile:
        csvReader = csv.reader(csvDataFile)
        id = 0
        for row in csvReader:
            if id==0:
                id = 1
                continue
            if row[2]=="NaN":
                continue
            birthYear = int(row[2].split("/")[0])
            for year in range(2008,2020):
                index = 4+year-2008
                if row[index]!="NaN":
                    teamNames.add(row[index])
                if row[index] in resultDict[year]:
                    value = resultDict[year][row[index]]
                    temp = value.split("+")
                    sum = int(temp[0])
                    count = int(temp[1])
                    sum = sum + year - birthYear
                    count = count + 1
                    resultDict[year][row[index]] = str(sum)+"+"+str(count)
                else:
                    sum = year - birthYear
                    count = 1
                    resultDict[year][row[index]] = str(sum) + "+" + str(count)
    file = open("players_age_wiki.csv", "a")
    id = 1
    temp = "id,team_name"
    for year in range(2008,2020):
        temp = temp+","+str(year)
    file.write(temp+"\n")

    for team in teamNames:
        temp = str(id)+","+team
        for year in range(2008, 2020):
            if team in resultDict[year]:
                dataStr = resultDict[year][team]
                tempList = dataStr.split("+")
                temp = temp+"," + str(int(tempList[0])/int(tempList[1]))
            else:
                temp = temp + ","+"NaN"
        file.write(temp+"\n")
        id = id + 1
    file.close()

if __name__ == '__main__':
    main()
