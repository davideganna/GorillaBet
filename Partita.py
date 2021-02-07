import datetime
from Enumerators import *

class Partita:
    """Classe per la descrizione della singola riga"""
    def __init__(self):
        Lega: str
        DataPartita:datetime
        SquadraHome:str
        SquadraAway:str
        EsitoFinale:Esito
        EsitoPrimoTempo:Esito
        GoalPrimoTempoHome:int
        GoalPrimoTempoAway:int
        GoalFinaliHome:int
        GoalFinaliAway:int

    