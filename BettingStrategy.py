from Squadra import *
from Enumerators import *

# A betting strategy to be discussed with the team

# Attack strength  = goals totali / (goals totali + goals subiti)
attack_strength  = 0
# Defense strength = goals subiti / (goals totali + goals subiti)
defense_strength = 0
# Home factor = moltiplicatore per la squadra di casa (da sottrarre alla squadra away)
home_factor = 1.05

def printNome(squadre:list[Squadra]):
    s:Squadra
    for s in squadre:
        print(s.Nome)