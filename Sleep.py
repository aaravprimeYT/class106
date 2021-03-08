import plotly.express as px
import csv

with open("Sleep.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Coffee (ml)", y = "sleep in hours")
    fig.show()