from Enumerators import *
from Partita import Partita 

class Squadra:
    """Classe per la descrizione della singola squadra"""
    def __init__(self, nome):
        self.Nome = nome
        self.PartiteGiocate = []

    def GetPartiteWhereHome(self) -> list[Partita]:
        allMatches:list[Partita] = self.PartiteGiocate
        filteredMatches:list[Partita] = []
        p: Partita
        for p in allMatches:
            if p.SquadraHome == self.Nome:
                filteredMatches.append(p)
        return filteredMatches

    def GetPartiteWhereAway(self) -> list[Partita]:
        allMatches = self.PartiteGiocate
        filteredMatches:allMatches = []
        p : Partita
        for p in allMatches:
            if p.SquadraAway == self.Nome:
                filteredMatches.append(p)
        return filteredMatches

    def GetPartiteWhereWon(self) -> list[Partita]:
        matchHome = self.GetPartiteWhereHome()
        matchAway = self.GetPartiteWhereAway()
        result: list[Partita]
        p: Partita
        for p in matchHome:
            if p.EsitoFinale == Esito.HomeWon:
                result.append(p)
        for p in matchAway:
            if p.EsitoFinale == Esito.AwayWon:
                result.append(p)
        return result

    def GetPartiteWhereLost(self) -> list[Partita]:
        matchHome = self.GetPartiteWhereHome()
        matchAway = self.GetPartiteWhereAway()
        result: list[Partita]
        p : Partita
        for p in matchHome:
            if p.EsitoFinale == Esito.AwayWon:
                result.append(p)
        for p in matchAway:
            if p.EsitoFinale == Esito.HomeWon:
                result.append(p)
        return result


    #goal fatti e subiti in casa e fuori casa
    def GetGoalFattiInCasa(self) -> int:
        match = self.GetPartiteWhereHome()
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliHome
        return result

    def GetGoalFattiAway(self) -> int:
        match:list[Partita] = self.GetPartiteWhereAway()
        result:int = 0
        p: Partita
        for p in match:
            result+= p.GoalFinaliAway
        return result

    def GetGoalSubitiInCasa(self) -> int:
        match:list[Partita] = self.GetPartiteWhereHome()
        result:int = 0
        p: Partita
        for p in match: 
            result+= p.GoalFinaliAway
        return result

    def GetGoalSubitiAway(self) -> int:
        match = self.GetPartiteWhereAway()
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliHome
        return result

    def GetCoefficenteAttacco(self) -> float:
        try:
            return round((self.GetGoalFattiInCasa() + self.GetGoalFattiAway())/(self.GetGoalFattiInCasa() + self.GetGoalFattiAway() + self.GetGoalSubitiInCasa() + self.GetGoalSubitiAway()), 3)
        except ZeroDivisionError:
            return -1 

    def GetCoefficenteDifesa(self) -> float:
        try:
            return round((self.GetGoalSubitiInCasa() + self.GetGoalSubitiAway())/(self.GetGoalFattiInCasa() + self.GetGoalFattiAway() + self.GetGoalSubitiInCasa() + self.GetGoalSubitiAway()), 3)
        except ZeroDivisionError:
            return -1   
