from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 

#Fase 1 Aprire i file sorgente e ottenerne la struttura dati per ogni riga
rows:list[Row] = FileHelper.GetRowsFromFiles()
#conversione in una più cristiana variabile partita
partite:list[Partita] = []
r:Row
for r in rows:
    partite.append(r.GetPartita())
######################################


###################### Test - Jay ###################### Usa un file e una classe apposita, non sporchiamo qui!

GFc = 0 # GFc = Goals fatti in casa
GSc = 0 # GSc = Goals subiti in casa
GFt = 0 # GFt = Goals fatti in trasferta
GSt = 0 # GSt = Goals subiti in trasferta


for squadra in SquadraList:
    print(f"\n --- Storico Goals {squadra} --- \n")
    for r in rows:
        if r.homeTeam == squadra:
            print(f"Goals in casa contro il {r.awayTeam}: {r.FTHG}")
            GFc = GFc + int(r.FTHG)
            GSc = GSc + int(r.FTAG)
        elif r.awayTeam == squadra:
            print(f"Goals in trasferta contro il {r.homeTeam}: {r.FTAG}")
            GFt = GFt + int(r.FTAG)
            GSt = GSt + int(r.FTHG)

    print("\n --- Totale Goals --- \n")
    print(f"Totale Goals fatti in casa: {GFc}")
    print(f"Totale Goals subiti in casa: {GSc}")
    print(f"Totale Goals fatti in trasferta: {GFt}")
    print(f"Totale Goals subiti in trasferta: {GSt}")

    print("\n --- Total Strength / Weakness --- \n")
    try:
        attack_strength  = (GFc + GFt)/(GFc + GFt + GSc + GSt)
    except ZeroDivisionError:
        attack_strength = None

    try:
        defence_weakness = (GSc + GSt)/(GFc + GFt + GSc + GSt)
    except ZeroDivisionError:
        defence_weakness = None

    print(f"{squadra} Attack Strength:  {attack_strength:.5f}")
    print(f"{squadra} Defence Weakness: {defence_weakness:.5f}")

    GFc = 0 # GFc = Goals fatti in casa
    GSc = 0 # GSc = Goals subiti in casa
    GFt = 0 # GFt = Goals fatti in trasferta
    GSt = 0 # GSt = Goals subiti in trasferta

