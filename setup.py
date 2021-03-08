import csv
import numpy as np

def getDataSource(dataPath):
    iceCreamSales = []
    temp = []

    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            iceCreamSales.append(float(row["Ice-cream Sales"]))
            temp.append(float(row["Temperature"]))

    return {"x":iceCreamSales,"y":temp}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def main():
    dataPath = "ice-Cream.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

main()