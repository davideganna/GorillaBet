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

def create_stats_matrix(squadra_home, squadra_away):
    """Returns a matrix M:\n
    M[0] = Squadra\n
    M[1] = Giornate\n
    M[2] = GFc\n
    M[3] = GFt\n
    M[4] = GSc\n
    M[5] = GSt\n
    M[6] = Attack Strength Home\n
    M[7] = Attack Strength Away\n
    M[8] = Defence Strength Home\n
    M[9] = Defence Strength Away\n
    M[10] = Expected Goals when Home\n
    M[11] = Expected Goals when Away\n
    """
    M = np.ndarray((20,6), dtype = object)
    for n, squadra in enumerate(SquadraList):
        giornate = 0 # Partite giocate
        GFc = 0 # GFc = Goals fatti in casa
        GSc = 0 # GSc = Goals subiti in casa
        GFt = 0 # GFt = Goals fatti in trasferta
        GSt = 0 # GSt = Goals subiti in trasferta
        for r in rows:
            if r.homeTeam == squadra and r.HTHG is not "":
                GFc = GFc + int(r.FTHG)
                GSc = GSc + int(r.FTAG)
                giornate = giornate + 1
            elif r.awayTeam == squadra and r.HTHG is not "":
                GFt = GFt + int(r.FTAG)
                GSt = GSt + int(r.FTHG)
                giornate = giornate + 1

        M[n, 0] = squadra
        M[n, 1] = giornate
        M[n, 2] = GFc
        M[n, 3] = GFt
        M[n, 4] = GSc
        M[n, 5] = GSt
    
    giornate_tot = M[:,1].sum()
    GTFc = M[:,2].sum() # Goal totali fatti in casa
    GTFt = M[:,3].sum() # Goal totali fatti in trasferta
    GTSc = M[:,4].sum() # Goal totali subiti in casa
    GTSt = M[:,5].sum() # Goal totali subiti in trasferta

    y = PrettyTable(["Squadra", "Giornate", "GFc", "GFt", "GSc", "GSt"])
    for row in M:
        y.add_row(row)

    S = np.ndarray((20,4), dtype = object) # Strength Matrix
    for n, squadra in enumerate(SquadraList):
        try:
            attack_strength_H  = round((M[n,2]/M[n,1])/(GTFc/(20*M[n,1])), 3)
        except ZeroDivisionError:
            attack_strength_H = None

        try:
            attack_strength_A  = round((M[n,3]/M[n,1])/(GTFt/(20*M[n,1])), 3)
        except ZeroDivisionError:
            attack_strength_A = None

        try:
            defence_strength_H = round((M[n,4]/M[n,1])/(GTSc/(20*M[n,1])), 3)
        except ZeroDivisionError:
            defence_strength_H = None
        
        try:
            defence_strength_A = round((M[n,5]/M[n,1])/(GTSt/(20*M[n,1])), 3)
        except ZeroDivisionError:
            defence_strength_A = None
        
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
            exp_goals_H  = round(M[SquadraDict[squadra_home],6]*M[SquadraDict[squadra_away],9]*GTFc/giornate_tot, 3) 
        except ZeroDivisionError:
            exp_goals_H = None

        try:
            exp_goals_A  = round(M[SquadraDict[squadra_away],7]*M[SquadraDict[squadra_home],8]*GTFt/giornate_tot, 3)
        except ZeroDivisionError:
            exp_goals_A = None
        
        if squadra == squadra_home:
            E[SquadraDict[squadra_home],0] = exp_goals_H
            E[SquadraDict[squadra_home],1] = ""
        elif squadra == squadra_away:
            E[SquadraDict[squadra_away],1] = exp_goals_A
            E[SquadraDict[squadra_away],0] = ""
        else:
            E[n,0] = ""
            E[n,1] = ""
    
    M = np.concatenate((M,E),axis=1)

    y.add_column(f"Exp goals vs {squadra_away}", E[:,0])
    y.add_column(f"Exp goals vs {squadra_home}", E[:,1])
    print(y)
    return M

def calc_poisson_goals(squadra_home, squadra_away):
    M = create_stats_matrix(squadra_home, squadra_away)
    exp_goals_H = M[SquadraDict[squadra_home], 10]
    exp_goals_A = M[SquadraDict[squadra_away], 11]
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