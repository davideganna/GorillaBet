import datetime
from Enumerators import *

class Partita(object):
    """Classe per la descrizione della singola riga"""
    Lega: str
    """Divisione nella lega"""
    DataPartita:datetime
    SquadraOspitante:Squadra
    SquadraOspite:Squadra
    