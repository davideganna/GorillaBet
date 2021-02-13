from Enumerators import *
from Partita import Partita 
import math

class Squadra:
    """Classe per la descrizione della singola squadra"""
    def __init__(self, nome):
        self.Nome = nome
        self.PartiteGiocate = []

    def GetPartiteWhereHome(self):
        allMatches:list[Partita] = self.PartiteGiocate
        filteredMatches:list[Partita] = []
        p: Partita
        for p in allMatches:
            if p.SquadraHome == self.Nome:
                filteredMatches.append(p)
        return filteredMatches

    def GetPartiteWhereAway(self):
        allMatches = self.PartiteGiocate
        filteredMatches:allMatches = []
        p : Partita
        for p in allMatches:
            if p.SquadraAway == self.Nome:
                filteredMatches.append(p)
        return filteredMatches

    def GetPartiteWhereWon(self):
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

    def GetPartiteWhereLost(self):
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
    def GetGoalFattiInCasa(self):
        match = self.GetPartiteWhereHome()
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliHome
        return result

    def GetGoalFattiAway(self):
        match:list[Partita] = self.GetPartiteWhereAway()
        result:int = 0
        p: Partita
        for p in match:
            result+= p.GoalFinaliAway
        return result

    def GetGoalSubitiInCasa(self):
        match:list[Partita] = self.GetPartiteWhereHome()
        result:int = 0
        p: Partita
        for p in match: 
            result+= p.GoalFinaliAway
        return result

    def GetGoalSubitiAway(self):
        match = self.GetPartiteWhereAway()
        result:int = 0
        p: Partita
        for p in match:
            result+=p.GoalFinaliHome
        return result

    def GetCoefficenteAttacco(self):
        try:
            return round((self.GetGoalFattiInCasa() + self.GetGoalFattiAway())/(self.GetGoalFattiInCasa() + self.GetGoalFattiAway() + self.GetGoalSubitiInCasa() + self.GetGoalSubitiAway()), 3)
        except ZeroDivisionError:
            return -1 

    def GetCoefficenteDifesa(self):
        try:
            return round((self.GetGoalSubitiInCasa() + self.GetGoalSubitiAway())/(self.GetGoalFattiInCasa() + self.GetGoalFattiAway() + self.GetGoalSubitiInCasa() + self.GetGoalSubitiAway()), 3)
        except ZeroDivisionError:
            return -1   

    def GetValoreAttesoAttaccoHome(self):
        goalFatti:int = self.GetGoalFattiInCasa()
        partiteCasa:list[Partita] = self.GetPartiteWhereHome()
        numeroPartite:int = len(partiteCasa)
        mediaGoalFatti:float = goalFatti/numeroPartite
        return mediaGoalFatti

    def GetValoreAttesoAttaccoAway(self):
        goalFatti:int = self.GetGoalFattiAway()
        partiteAway:list[Partita] = self.GetPartiteWhereAway()
        numeroPartite:int = len(partiteAway)
        mediaGoalFatti:float = goalFatti/numeroPartite
        return mediaGoalFatti

    def GetValoreAttesoSubitiHome(self):
        goalSubiti:int = self.GetGoalSubitiInCasa()
        partiteCasa:list[Partita] = self.GetPartiteWhereHome()
        numeroPartite:int = len(partiteCasa)
        mediaGoalSubiti:float = goalSubiti/numeroPartite
        return mediaGoalSubiti

    def GetValoreAttesoSubitiAway(self):
        goalSubiti:int = self.GetGoalSubitiAway()
        partiteAway:list[Partita] = self.GetPartiteWhereAway()
        numeroPartite:int = len(partiteAway)
        mediaGoalSubiti:float = goalSubiti/numeroPartite
        return mediaGoalSubiti

    def GetPoissonValueHome(self, goalNumber:int):
        lamb:float = self.GetValoreAttesoAttaccoHome()
        poisson:float = (lamb^goalNumber * (math.e^(-lamb)))/math.factorial(goalNumber)
        return poisson

    def GetPoissonValueHome(self, goalNumber:int):
        lamb:float = self.GetValoreAttesoAttaccoAway()
        poisson:float = (lamb^goalNumber * (math.e^(-lamb)))/math.factorial(goalNumber)
        return poisson