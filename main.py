from ApiInterface import DashApi as API
from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
from BettingStrategy import *
from ReadableBettingStrategy import ReadableBettingStrategy
from CacheHelper import CacheHelper as cache

############## Modify this to test different codes ##############
tester = "Jay" # "Eim", "Jay", "Varsa"
#################################################################
if tester == "Eim":
    API.GetAllSquadre()
elif tester == "Jay":
    squadra_home = "Napoli"
    squadra_away = "Juventus"
    squadra_home = squadra_home.lower()
    squadra_away = squadra_away.lower()
    game = squadra_home + squadra_away
    [GPh, GPa] = calc_poisson_goals(squadra_home, squadra_away)
    [OHW, OD, OAW] = calc_odds(GPh, GPa)
    print(f"[Bot] {squadra_home} wins: {OHW:.4}")
    print(f"[Bot] Draw: {OD:.4}")
    print(f"[Bot] {squadra_away} wins: {OAW:.4}")
    [home, draw, away] = API.Get_Odds_from_match(game)
    print(f"[BWIN] {squadra_home} wins: {home}")
    print(f"[BWIN] Draw: {draw}")
    print(f"[BWIN] {squadra_away} wins: {away}")

elif tester == "Varsa":
    squadra_home = "Napoli"
    squadra_away = "Juventus"
    game = squadra_home + squadra_away
    [home, draw, away] = API.Get_Odds_from_match(game)
    
    