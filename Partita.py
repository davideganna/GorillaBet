import datetime
from Enumerators import *

class Partita(object):
    """Classe per la descrizione della singola riga"""
    Lega: str
    """Divisione nella lega"""
    DataPartita:datetime
    SquadraHome:str
    SquadraAway:str
    EsitoFinale:Esito
    EsitoPrimoTempo:Esito
    GoalPrimoTempoHome:int
    GoalPrimoTempoAway:int
    GoalFinaliHome:int
    GoalFinaliAway:int

    