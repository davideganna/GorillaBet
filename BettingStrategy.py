from Squadra import *
from Enumerators import *

# A betting strategy to be discussed with the team

# Attack strength  = goals totali / (goals totali + goals subiti)
attack_strength  = 0
# Defense strength = goals subiti / (goals totali + goals subiti)
defense_strength = 0
# Home factor = moltiplicatore per la squadra di casa (da sottrarre alla squadra away)
home_factor = 1.05

def print_squadre(squadre:list[Squadra]):
    s:Squadra
    for s in squadre:
        print(s.Nome)

###################### Test - Jay ###################### Usa un file e una classe apposita, non sporchiamo qui!

#GFc = 0 # GFc = Goals fatti in casa
#GSc = 0 # GSc = Goals subiti in casa
#GFt = 0 # GFt = Goals fatti in trasferta
#GSt = 0 # GSt = Goals subiti in trasferta

#for squadra in SquadraList:
    #print(f"\n --- Storico Goals {squadra} --- \n")
    #for r in rows:
    #    if r.homeTeam == squadra:
    #        print(f"Goals in casa contro il {r.awayTeam}: {r.FTHG}")
    #        GFc = GFc + int(r.FTHG)
    #        GSc = GSc + int(r.FTAG)
    #    elif r.awayTeam == squadra:
    #        print(f"Goals in trasferta contro il {r.homeTeam}: {r.FTAG}")
    #        GFt = GFt + int(r.FTAG)
    #        GSt = GSt + int(r.FTHG)

    #print("\n --- Totale Goals --- \n")
    #print(f"Totale Goals fatti in casa: {GFc}")
    #print(f"Totale Goals subiti in casa: {GSc}")
    #print(f"Totale Goals fatti in trasferta: {GFt}")
    #print(f"Totale Goals subiti in trasferta: {GSt}")

    #print("\n --- Total Strength / Weakness --- \n")
    #try:
    #    attack_strength  = (GFc + GFt)/(GFc + GFt + GSc + GSt)
    #except ZeroDivisionError:
    #    attack_strength = None

    #try:
    #    defence_weakness = (GSc + GSt)/(GFc + GFt + GSc + GSt)
    #except ZeroDivisionError:
    #    defence_weakness = None

    #print(f"{squadra} Attack Strength:  {attack_strength:.5f}")
    #print(f"{squadra} Defence Weakness: {defence_weakness:.5f}")