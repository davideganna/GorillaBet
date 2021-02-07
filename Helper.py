from Partita import Partita 
from Enumerators import *
from Squadra import Squadra

class Helper(object):
    """Classe helper con una serie di funzioni utili"""

    @staticmethod
    def GetSquadraFromNome(squadre:list[Squadra], squadraCercata:str) -> Squadra:
        s: Squadra
        for s in squadre:
            if s.Nome == squadraCercata:
                return s
        return None