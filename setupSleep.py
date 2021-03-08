import csv
import numpy as np

def getDataSource(dataPath):
    sleepTime = []
    amountOfCoffee = []
    
    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            sleepTime.append(float(row["sleep in hours"]))
            amountOfCoffee.append(float(row["Coffee (ml)"]))
        
    return {"x":amountOfCoffee,"y":sleepTime}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def main():
    dataPath = "Sleep.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

main()