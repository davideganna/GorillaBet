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
import json
############## Modify this to test different codes ##############
tester = input("Tester: ").lower() # "Eim", "Jay", "Varsa"
#################################################################
if tester == "eim":
    print(json.dumps(cache.GetFromFile("test.json")))
elif tester == "jay":
    jay_headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "648939b99aca43ba86c7c75455b9fc61" # Chiave Jay
    }
    API.headers = jay_headers
    squadra_home = "Milan"
    squadra_away = "Inter"
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

elif tester == "varsa":
    varsa_headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "fbcab0dc26060c039332cb3bd8f2d62a"
    }
    API.headers = varsa_headers
    print(API.Get_Odds_from_match("veronalazio"))
    
    