from FileHelper import FileHelper
from Row import Row
from Enumerators import *

#Fase 1 Aprire i file sorgente e ottenerne la struttura dati per ogni riga

#forse l'idea delle classi è diversa in python?
# Esempio per Juventus
rows:list[Row] = FileHelper.GetRowsFromFiles()

juveIn : list[Row] = []


###################### Test - Jay ######################

GFc = 0 # GFc = Goals fatti in casa
GSc = 0 # GSc = Goals subiti in casa
GFt = 0 # GFt = Goals fatti in trasferta
GSt = 0 # GSt = Goals subiti in trasferta

r: Row
print("\n --- Storico Goals Juventus --- \n")
for r in rows:
    if r.homeTeam == Squadra.Juventus:
        print(f"Goals in casa contro il {r.awayTeam}: {r.FTHG}")
        GFc = GFc + int(r.FTHG)
        GSc = GSc + int(r.FTAG)
    elif r.awayTeam == Squadra.Juventus:
        print(f"Goals in trasferta contro il {r.homeTeam}: {r.FTAG}")
        GFt = GFt + int(r.FTAG)
        GSt = GSt + int(r.FTHG)

print("\n --- Totale Goals --- \n")
print(f"Totale Goals fatti in casa: {GFc}")
print(f"Totale Goals subiti in casa: {GSc}")
print(f"Totale Goals fatti in trasferta: {GFt}")
print(f"Totale Goals subiti in trasferta: {GSt}")

print("\n --- Total Strength --- \n")
print(f"Juventus Attack Strength: {(GFc + GFt)/(GFc + GFt + GSc + GSt)}")
print(f"Juventus Defence Strength: {(GSc + GSt)/(GFc + GFt + GSc + GSt)}")

