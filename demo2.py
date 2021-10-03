import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("C-108\data.csv")
figure = ff.create_distplot([df["Avg Rating"].tolist()], ["Rating"], show_hist = False)
figure.show()