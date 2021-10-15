import csv
import pandas as pd
import plotly.figure_factory as ff

data = pd.read_csv("m.csv")
fig = ff.create_distplot([data["Avg Rating"].tolist()],["Avg Rating"],show_hist=True)
fig.show()