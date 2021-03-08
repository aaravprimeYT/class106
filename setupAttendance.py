import csv
import numpy as np

def getDataSource(dataPath):
    rollNo = []
    dayPresent = []

    with open(dataPath) as f:
        csvReader = csv.DictReader(f)
        for row in csvReader:
            rollNo.append(float(row["Roll No"]))
            dayPresent.append(float(row["Days Present"]))
        
    return {"x":rollNo,"y":dayPresent}

def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"],dataSource["y"])
    print(correlation[0,1])

def main():
    dataPath = "Attendance.csv"
    dataSource = getDataSource(dataPath)
    findCorrelation(dataSource)

main()