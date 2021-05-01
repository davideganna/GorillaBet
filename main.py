from ApiInterface import DashApi as API
from FileHelper import FileHelper
from Enumerators import *
from BettingStrategy import *
import json

############## Modify this to test different codes ##############
#tester = input("Tester: ").lower() # "Eim", "Jay", "Varsa"
#################################################################

#if tester == "jay":
    #jay_headers = {
    #    'x-rapidapi-host': "v3.football.api-sports.io",
    #    'x-rapidapi-key': "648939b99aca43ba86c7c75455b9fc61" # Chiave Jay
    #}
    #API.headers = jay_headers
    #squadra_home = "crotone"
    #squadra_away = "inter"
    #squadra_home = squadra_home.lower()
    #squadra_away = squadra_away.lower()

    #[GPh, GPa] = calc_poisson_goals(squadra_home, squadra_away)
    #[OHW, OD, OAW] = calc_odds(GPh, GPa)

    #print(f"[Bot] {squadra_home} wins: {OHW:.4}")
    #print(f"[Bot] Draw: {OD:.4}")
    #print(f"[Bot] {squadra_away} wins: {OAW:.4}")

    #[squadra_home, squadra_away] = FileHelper.get_flexible_names(squadra_home, squadra_away)
    #game = squadra_home + squadra_away
    #[home, draw, away] = API.Get_Odds_from_match(game)

    #print(f"[BWin] {squadra_home} wins: {home}")
    #print(f"[BWin] Draw: {draw}")
    #print(f"[BWin] {squadra_away} wins: {away}")
    