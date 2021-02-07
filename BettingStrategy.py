from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
import numpy as np 
from prettytable import PrettyTable

# A betting strategy to be discussed with the team

# Attack strength  = goals totali / (goals totali + goals subiti)
attack_strength  = 0
# Defense strength = goals subiti / (goals totali + goals subiti)
defense_strength = 0
# Home factor = moltiplicatore per la squadra di casa (da sottrarre alla squadra away)
home_factor = 1.05

###################### Test - Jay ###################### 

rows:list[Row] = FileHelper.GetRowsFromFiles()

def create_matrix():
    GFc = 0 # GFc = Goals fatti in casa
    GSc = 0 # GSc = Goals subiti in casa
    GFt = 0 # GFt = Goals fatti in trasferta
    GSt = 0 # GSt = Goals subiti in trasferta

    M = np.ndarray((20,7), dtype = object)
    for n, squadra in enumerate(SquadraList):
        for r in rows:
            if r.homeTeam == squadra:
                #print(f"Goals in casa contro il {r.awayTeam}: {r.FTHG}")
                GFc = GFc + int(r.FTHG)
                GSc = GSc + int(r.FTAG)
            elif r.awayTeam == squadra:
                #print(f"Goals in trasferta contro il {r.homeTeam}: {r.FTAG}")
                GFt = GFt + int(r.FTAG)
                GSt = GSt + int(r.FTHG)
        

        #print("\n --- Totale Goals --- \n")
        #print(f"Totale Goals fatti in casa: {GFc}")
        #print(f"Totale Goals subiti in casa: {GSc}")
        #print(f"Totale Goals fatti in trasferta: {GFt}")
        #print(f"Totale Goals subiti in trasferta: {GSt}")

        #print("\n --- Total Strength / Weakness --- \n")
        try:
            attack_strength  = (GFc + GFt)/(GFc + GFt + GSc + GSt)
        except ZeroDivisionError:
            attack_strength = None

        try:
            defence_weakness = (GSc + GSt)/(GFc + GFt + GSc + GSt)
        except ZeroDivisionError:
            defence_weakness = None

        #print(f"{squadra} Attack Strength:  {attack_strength:.5f}")
        #print(f"{squadra} Defence Weakness: {defence_weakness:.5f}")
        M[n, 0] = squadra
        M[n, 1] = GFc
        M[n, 2] = GFt
        M[n, 3] = GSc
        M[n, 4] = GSt
        M[n, 5] = attack_strength
        M[n, 6] = defence_weakness

        M[1,:].round(3)

        GFc = 0 # GFc = Goals fatti in casa
        GSc = 0 # GSc = Goals subiti in casa
        GFt = 0 # GFt = Goals fatti in trasferta
        GSt = 0 # GSt = Goals subiti in trasferta

    x = PrettyTable(["Squadra", "GFc", "GFt", "GSc", "GSt", "AttF", "DefW"])
    for row in M:
        x.add_row(row)
    print(x)