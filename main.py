from ApiInterface import DashApi as API
from FileHelper import FileHelper
from Enumerators import *
from BettingStrategy import *
import json

############## Modify this to test different codes ##############
#tester = input("Tester: ").lower() # "Eim", "Jay", "Varsa"
tester = "jay"
#################################################################

if tester == "jay":
    with open(f'API_keys.txt', 'r') as f:
        for line in f:
            if "jay_key" in line:
                key = line.partition("=")[2].partition("\n")[0]
    jay_headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': key # Chiave Jay
    }
    API.headers = jay_headers
    FileHelper.txt_generator(38)

    home_team = "Atalanta"
    away_team = "Juventus"

    df = create_df()

    [GPh, GPa] = calc_exp_goals(df, home_team, away_team)
    [OHW, OD, OAW] = calc_odds(GPh, GPa)

    [squadra_home, squadra_away] = FileHelper.get_flexible_names(home_team, away_team)
    [home, draw, away] = API.Get_Odds_from_match(home_team + away_team)
    
    print(f"[Bot] {squadra_home} wins: {OHW:.4}")
    print(f"[Bot] Draw: {OD:.4}")
    print(f"[Bot] {squadra_away} wins: {OAW:.4}")
    print(f"[BWin] {squadra_home} wins: {home}")
    print(f"[BWin] Draw: {draw}")
    print(f"[BWin] {squadra_away} wins: {away}")
    