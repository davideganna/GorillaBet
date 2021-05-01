from FileHelper import FileHelper
from Enumerators import *
import numpy as np 
from prettytable import PrettyTable
import math
import pandas as pd

###################### Test - Jay ###################### 

df = FileHelper.get_dataframe()
df = df[["HomeTeam", "AwayTeam", "FTHG", "FTAG"]]
df = df.rename(columns={"FTHG": "HomeGoals", "FTAG": "AwayGoals"})

giornate = []
home_goals_made = []  # Totale Goal fatti in casa
away_goals_made = []  # Totale Goal fatti in trasferta
home_goals_taken = [] # Totale Goal subiti in casa
away_goals_taken = [] # Totale Goal subiti in trasferta

for squadra in Squadre:
    giornate.append(
        df["HomeTeam"].value_counts()[squadra] + df["AwayTeam"].value_counts()[squadra]
    )
    home_goals_made.append(
        df.loc[df["HomeTeam"] == squadra]["HomeGoals"].sum()
    )
    away_goals_made.append(
        df.loc[df["AwayTeam"] == squadra]["AwayGoals"].sum()
    )
    home_goals_taken.append(
        df.loc[df["HomeTeam"] == squadra]["AwayGoals"].sum()
    )
    away_goals_taken.append(
        df.loc[df["AwayTeam"] == squadra]["HomeGoals"].sum()
    )

d = {
    "Teams": Squadre,
    "Giornate": giornate,
    "GFc": home_goals_made,
    "GFt": away_goals_made,
    "GSc": home_goals_taken,
    "GSt": away_goals_taken,
}
df = pd.DataFrame(data=d)
 
print(df)



