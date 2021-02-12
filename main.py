from ApiInterface import DashApi as API
from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
from BettingStrategy import *
from ReadableBettingStrategy import ReadableBettingStrategy

############## Modify this to test different codes ##############
tester = "Jay" # "Eim", "Jay", "Varsa"
#################################################################
if tester == "Eim":
    API.GetFixtureAll()
    rows:list[Row] = FileHelper.GetRowsFromFiles()
    partite:list[Partita] = []
    r:Row
    for r in rows:
        partite.append(r.GetPartita())
    squadre: list[Squadra] = []
    sE: SquadraEnum
    for s in SquadraList:
        newSquadra:Squadra = Squadra(s)
        squadre.append(newSquadra)
    p:Partita
    for p in partite:
        squadraHome:Squadra = Helper.GetSquadraFromNome(squadre, p.SquadraHome)
        squadraAway:Squadra = Helper.GetSquadraFromNome(squadre, p.SquadraAway)
        squadraHome.PartiteGiocate.append(p)
        squadraAway.PartiteGiocate.append(p)
        print(len(squadraHome.PartiteGiocate))
    ReadableBettingStrategy.CalculateStats(squadre)

elif tester == "Jay":
    squadra_home = "Napoli"
    squadra_away = "Juventus"
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
    
    