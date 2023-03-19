import pandas as pd

data = pd.read_csv("data.csv")

studentid = data.loc[:,"studentid"]
name = data.loc[:,"studentname"]
date = data.loc[:,"date"]
attendance = data.loc[:,"attendance"]

