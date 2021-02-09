from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
import numpy as np 
from prettytable import PrettyTable
import math

# A betting strategy to be discussed with the team

# Attack strength  = goals totali / (goals totali + goals subiti)
attack_strength  = 0
# Defense strength = goals subiti / (goals totali + goals subiti)
defense_strength = 0
# Home factor = moltiplicatore per la squadra di casa (da sottrarre alla squadra away)
home_factor = 1.05

###################### Test - Jay ###################### 

rows:list[Row] = FileHelper.GetRowsFromFiles()

def poisson_pmf(mu, k):
    pmf = math.exp(-mu)*(mu**k)/math.factorial(k)
    return pmf

def create_matrix():
    M = np.ndarray((20,5), dtype = object)
    for n, squadra in enumerate(SquadraList):
        GFc = 0 # GFc = Goals fatti in casa
        GSc = 0 # GSc = Goals subiti in casa
        GFt = 0 # GFt = Goals fatti in trasferta
        GSt = 0 # GSt = Goals subiti in trasferta
        for r in rows:
            if r.homeTeam == squadra:
                GFc = GFc + int(r.FTHG)
                GSc = GSc + int(r.FTAG)
            elif r.awayTeam == squadra:
                GFt = GFt + int(r.FTAG)
                GSt = GSt + int(r.FTHG)

        M[n, 0] = squadra
        M[n, 1] = GFc
        M[n, 2] = GFt
        M[n, 3] = GSc
        M[n, 4] = GSt
    
    GTFc = M[:,1].sum() # Goal totali fatti in casa
    GTFt = M[:,2].sum() # Goal totali fatti in trasferta
    GTSc = M[:,3].sum() # Goal totali subiti in casa
    GTSt = M[:,4].sum() # Goal totali subiti in trasferta

    x = PrettyTable(["Squadra", "GFc", "GFt", "GSc", "GSt"])
    for row in M:
        x.add_row(row)
    print(x)

    matches = 20 # to fix
    S = np.ndarray((20,5), dtype = object) # Strength Matrix
    for n, squadra in enumerate(SquadraList):
        try:
            attack_strength_H  = round((M[n,1]/matches)/(GTFc/(20*matches)), 3)
        except ZeroDivisionError:
            attack_strength_H = None

        try:
            attack_strength_A  = round((M[n,2]/matches)/(GTFt/(20*matches)), 3)
        except ZeroDivisionError:
            attack_strength_A = None

        try:
            defence_strength_H = round((M[n,3]/matches)/(GTSc/(20*matches)), 3)
        except ZeroDivisionError:
            defence_strength_H = None
        
        try:
            defence_strength_A = round((M[n,4]/matches)/(GTSt/(20*matches)), 3)
        except ZeroDivisionError:
            defence_strength_A = None
        
        S[n,0] = squadra
        S[n,1] = attack_strength_H
        S[n,2] = attack_strength_A
        S[n,3] = defence_strength_H
        S[n,4] = defence_strength_A

    x = PrettyTable(["Squadra", "AttSt_Home", "AttSt_Away", "DefSt_Home", "DefSt_Away"])
    for row in S:
        x.add_row(row)
    print(x)


