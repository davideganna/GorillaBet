import datetime

class Partita(object):
    """Classe per la descrizione della singola riga"""
    Lega: str
    """Divisione nella lega"""

    
    _x:datetime
    @property
    def x(self) -> datetime:
        return self._x
    @x.setter
    def x(self, value):
        self._x = value
    