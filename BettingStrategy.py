from FileHelper import FileHelper
from Enumerators import *
import numpy as np 
from prettytable import PrettyTable
import math
import pandas as pd

###################### Test - Jay ###################### 

df_csv = FileHelper.get_dataframe()
df_csv = df_csv[['HomeTeam','AwayTeam','FTHG','FTAG']]
df_csv = df_csv.rename(columns={'FTHG': 'HomeGoals', 'FTAG': 'AwayGoals'})

partite_juve = df_csv[
    (df_csv['HomeTeam'] == "Juventus") | 
    (df_csv['AwayTeam'] == "Juventus")
]

GTFc = partite_juve[partite_juve["HomeTeam"] == "Juventus"]["HomeGoals"].sum()
GTFt = partite_juve[partite_juve["AwayTeam"] == "Juventus"]["AwayGoals"].sum()

d = {"Teams": SquadraList}
df = pd.DataFrame(data=d)
print(df)