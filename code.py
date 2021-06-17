import numpy as np 

import csv

import pandas as pd 

import plotly.express as px


with open("correlation/Student Marks vs Days Present.csv.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df, x="Marks In Percentage", y="Days Present")



    fig.show()



def getDataSource(data_path):
    coffeeInMl = []
    sleepInHours = []
    with open(data_path) as csvFile:
        csvReader = csv.DictReader(csvFile)
        for row in csvReader:
            coffeeInMl.append(float(row["Marks In Percentage"]))
            sleepInHours.append(float(row["Days Present"]))
    return {"x":coffeeInMl, "y":sleepInHours}



def findCorrelation(dataSource):
    correlation = np.corrcoef(dataSource["x"], dataSource["y"])
    print("Change Between Marks In Percentage vs Days Present:- \n---", correlation[0,1])




def setUp():
    data_path = "Student Marks vs Days Present.csv"
    dataSource = getDataSource(data_path)
    findCorrelation(dataSource)



setUp()