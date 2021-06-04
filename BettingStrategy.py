from FileHelper import FileHelper
from Enumerators import *
import numpy as np 
from prettytable import PrettyTable
import math
import pandas as pd

###################### Functions ###################### 

def poisson_pmf(mu, k):
    """Returns the Poisson PMF f(k)\n
    mu = Expected rate of goals\n
    k  = Number of goals to evaluate\n
    """
    pmf = math.exp(-mu)*(mu**k)/math.factorial(k)
    return pmf

###################### Test - Jay ###################### 

df = FileHelper.get_dataframe()
df = df[["HomeTeam", "AwayTeam", "FTHG", "FTAG"]]
df = df.rename(columns={"FTHG": "HomeGoals", "FTAG": "AwayGoals"})

giornate = []
home_goals_made = []        # Totale Goal fatti in casa
away_goals_made = []        # Totale Goal fatti in trasferta
home_goals_taken = []       # Totale Goal subiti in casa
away_goals_taken = []       # Totale Goal subiti in trasferta
attack_strength_home = []   # Fattore di attacco in casa
attack_strength_away = []   # Fattore di attacco in trasferta
defense_strength_home = []  # Fattore di difesa in casa
defense_strength_away = []  # Fattore di difesa in trasferta

# Calculate goals
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

# Fill the DataFrame
d = {
    "Squadra": Squadre,
    "Giornate": giornate,
    "GFc": home_goals_made,
    "GFt": away_goals_made,
    "GSc": home_goals_taken,
    "GSt": away_goals_taken
}
df = pd.DataFrame(data=d)

# Calculate strength
for squadra in Squadre:
    attack_strength_home.append(
        (df.loc[df["Squadra"] == squadra]["GFc"].sum() / df.loc[df["Squadra"] == squadra]["Giornate"].sum()) / (df["GFc"].sum()/df["Giornate"].sum())
    )
    attack_strength_away.append(
        (df.loc[df["Squadra"] == squadra]["GFt"].sum() / df.loc[df["Squadra"] == squadra]["Giornate"].sum()) / (df["GFt"].sum()/df["Giornate"].sum())
    )
    defense_strength_home.append(
        (df.loc[df["Squadra"] == squadra]["GSc"].sum() / df.loc[df["Squadra"] == squadra]["Giornate"].sum()) / (df["GSc"].sum()/df["Giornate"].sum())
    )
    defense_strength_away.append(
        (df.loc[df["Squadra"] == squadra]["GSt"].sum() / df.loc[df["Squadra"] == squadra]["Giornate"].sum()) / (df["GSt"].sum()/df["Giornate"].sum())
    )
    pass

# Fill the DataFrame
d = {
    "Squadra": Squadre,
    "Giornate": giornate,
    "GFc": home_goals_made,
    "GFt": away_goals_made,
    "GSc": home_goals_taken,
    "GSt": away_goals_taken,
    "ASh": attack_strength_home,
    "ASa": attack_strength_away,
    "DSh": defense_strength_home,
    "DSa": defense_strength_away,
}
df = pd.DataFrame(data=d)
print(df)

