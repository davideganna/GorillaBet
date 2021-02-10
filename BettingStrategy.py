from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
import numpy as np 
from prettytable import PrettyTable
import math

###################### Test - Jay ###################### 

rows:list[Row] = FileHelper.GetRowsFromFiles()

def poisson_pmf(mu, k):
    """Returns the Poisson PMF f(k)\n
    mu = Expected rate of goals\n
    k  = Number of goals to evaluate\n
    """
    pmf = math.exp(-mu)*(mu**k)/math.factorial(k)
    return pmf

def create_matrix():
    """Returns a matrix M:\n
    M[0] = Squadra\n
    M[1] = GFc\n
    M[2] = GFt\n
    M[3] = GSc\n
    M[4] = GSt\n
    M[5] = Attack Strength Home\n
    M[6] = Attack Strength Away\n
    M[7] = Defence Strength Home\n
    M[8] = Defence Strength Away\n
    M[9] = Expected Goals when Home\n
    M[10] = Expected Goals when Away\n
    """
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

    y = PrettyTable(["Squadra", "GFc", "GFt", "GSc", "GSt"])
    for row in M:
        y.add_row(row)

    matches = 20 # to fix
    S = np.ndarray((20,4), dtype = object) # Strength Matrix
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
        
        #S[n,0] = squadra
        S[n,0] = attack_strength_H
        S[n,1] = attack_strength_A
        S[n,2] = defence_strength_H
        S[n,3] = defence_strength_A

    y.add_column("AttSt_Home", S[:,0])
    y.add_column("AttSt_Away", S[:,1])
    y.add_column("DefSt_Home", S[:,2])
    y.add_column("DefSt_Away", S[:,3])

    M = np.concatenate((M,S),axis=1)

    E = np.ndarray((20,2), dtype = object) # Expected Goals Matrix
    for n, squadra in enumerate(SquadraList):
        try:
            exp_goals_H  = round(S[n,1]*M[13,8]*GTFc/(20*matches), 3) # S[13,4] -> DefStrength Roma when Away
        except ZeroDivisionError:
            exp_goals_H = None

        try:
            exp_goals_A  = round(S[n,2]*S[8,3]*GTFt/(20*matches), 3) # Contro la Roma
        except ZeroDivisionError:
            exp_goals_A = None
        
        #E[n,0] = squadra
        E[n,0] = exp_goals_H
        E[n,1] = exp_goals_A
    
    M = np.concatenate((M,E),axis=1)

    y.add_column("Exp_goals_vs_Roma", E[:,0])
    y.add_column("Exp_goals_vs_Juve", E[:,1])
    print(y)
    return M

def calc_poisson_goals(squadra_home, squadra_away):
    M = create_matrix()
    exp_goals_H = M[SquadraDict[squadra_home], 9]
    exp_goals_A = M[SquadraDict[squadra_away], 10]
    GPh = np.zeros(5) # Goal probabilities at home
    GPa = np.zeros(5) # Goal probabilities away
    for n in range(0, 5):
        GPh[n] = poisson_pmf(exp_goals_H, n)
        GPa[n] = poisson_pmf(exp_goals_A, n)
    
    return [GPh, GPa]

def calc_odds(GPh, GPa):
    """Based on goal probability vectors, calculates the odds matrix O.\n
    GPh = Goal probabilities at home\n
    GPa = Goal probabilities away\n
    Returns:\n
    O = Odds matrix\n
    """
    [PHW, PD, PAW] = np.zeros(3) # Probability Home Wins / Draw / Away Wins
    P = np.zeros((len(GPh),len(GPa)))
    for m in range(0, len(GPh)):
        for n in range(0, len(GPa)):
            P[m,n] = GPh[m]*GPa[n]
            if m > n:
                PHW = PHW + P[m,n]
            elif m == n:
                PD = PD + P[m,n]
            else:
                PAW = PAW + P[m,n]
    
    return [1/PHW, 1/PD, 1/PAW]
    

        


    
