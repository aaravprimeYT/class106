import csv
import numpy as np

def getDataSource(dataPath):
    tvTime = []
    size = []

    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            tvTime.append(float(row["TV Time (hours)"]))
            size.append(float(row["Size of TV"]))
        
    return {"x":tvTime,"y":size}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def main():
    dataPath = "TVSales.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

main()