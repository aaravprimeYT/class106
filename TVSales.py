import plotly.express as px
import csv

with open("TVSales.csv") as f:
    df = csv.DictReader(f)
    fig = px.scatter(df,x = "Size of TV", y = "TV Time (hours)")
    fig.show()