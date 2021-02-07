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