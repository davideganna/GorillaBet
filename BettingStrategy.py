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
for squadra in Squadre:
    giornate.append(
        df["HomeTeam"].value_counts()[squadra] + df["AwayTeam"].value_counts()[squadra]
    )

d = {
    "Teams": Squadre,
    "Giornate": giornate
}
df = pd.DataFrame(data=d)
 
print(df) 



