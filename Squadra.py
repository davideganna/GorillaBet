from Partita import Partita 
from Enumerators import *

class Squadra(object):
    """Classe per la descrizione della singola squadra"""
    Nome: str = ""
    PartiteGiocate:list[Partita] =  []
    
    def GetPartiteWhereHome(self) -> list[Partita]:
        allMatches = self.PartiteGiocate
        filteredMatches:list[Partita] = []
        p : Partita
        for p in self.PartiteGiocate:
            if p.SquadraHome == self.Nome:
                filteredMatches.append(p)
        return filteredMatches

    def GetPartiteWhereAway(self) -> list[Partita]:
        allMatches = self.PartiteGiocate
        filteredMatches:list[Partita] = []
        p : Partita
        for p in self.PartiteGiocate:
            if p.SquadraAway == self.Nome:
                filteredMatches.append(p)
        return filteredMatches

    def GetPartiteWhereWon(self) -> list[Partita]:
        matchHome = self.GetPartiteWhereHome(self)
        matchAway = self.GetPartiteWhereAway(self)
        result: list[Partita]
        p : Partita
        for p in matchHome:
            if p.EsitoFinale == Esito.HomeWon:
                result.append(p)
        for p in matchAway:
            if p.EsitoFinale == Esito.AwayWon:
                result.append(p)

    def GetPartiteWhereLost(self) -> list[Partita]:
        matchHome = self.GetPartiteWhereHome(self)
        matchAway = self.GetPartiteWhereAway(self)
        result: list[Partita]
        p : Partita
        for p in matchHome:
            if p.EsitoFinale == Esito.AwayWon:
                result.append(p)
        for p in matchAway:
            if p.EsitoFinale == Esito.HomeWon:
                result.append(p)

    #goal fatti e subiti in casa e fuori casa
    def GetGoalFattiInCasa(self) -> int:
        match = self.GetPartiteWhereHome(self)
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliHome
        return result
    def GetGoalFattiAway(self) -> int:
        match = self.GetPartiteWhereAway(self)
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliAway
        return result
    def GetGoalSubitiInCasa(self) -> int:
        match = self.GetPartiteWhereHome(self)
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliAway
        return result

    def GetGoalSubitiAway(self) -> int:
        match = self.GetPartiteWhereAway(self)
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliHome
        return result