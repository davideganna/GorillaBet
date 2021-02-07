from Partita import Partita 
from datetime import datetime
from Enumerators import *

class Row(object):
    """Classe per la descrizione della singola riga"""
    div: str
    """Divisione nella lega"""
    date: str
    """Data della partita"""
    time: str
    """Ora della partita"""
    homeTeam: str
    """Team che gioca in casa"""
    awayTeam: str
    """Team ospite"""
    FTHG: str
    """Goal fatti entro fine partita squadra in casa"""
    FTAG: str
    """Goal fatti entro fine partita squadra ospite"""
    FTR: str
    """Squadra vincente, H = team in casa, D = parità, A = team ospite"""
    HTHG: str 
    """Risultato squadra in casa a primo tempo"""
    HTAG: str 
    """Risultato squadra ospite a primo tempo"""
    HTR: str
    """"Squadra vincente a fine primo tempo, H = team in casa, D = parità, A = team ospite"""
    HS: str
    """Tiri squadra ospitante"""
    AS: str
    """Tiri squadra ospite"""
    HST: str
    """Tiri in porta squadra ospitante"""
    AST: str
    """Tiri in porta squadra ospite"""
    HHW: str
    """Pali colpiti squadra ospitante"""
    AHW: str
    """Pali colpiti squadra ospite"""
    HC:str
    """Angoli squadra ospitante"""
    AC:str
    """Angoli squadra ospite"""
    HF:str
    """Falli squadra ospitante"""
    AF:str
    """falli squadra ospite"""
    HO:str
    """Fuori giochi squadra ospitante"""
    AO:str
    """Fuori giochi squadra ospite"""
    HY:str
    """Cartellini gialli squadra ospitante"""
    AY:str
    """Cartellini gialli squadra ospite"""
    HR:str
    """Cartellini rossi squadra ospitante"""
    AR:str
    """Cartellini rossi squadra ospite"""
    HBP:str
    """Numero di cartellini totali della squadra ospitante, 10 = giallo, 25 = rosso"""
    ABP:str
    """Numero di cartellini totali della squadra ospite, 10 = giallo, 25 = rosso"""

    def GetPartita(self:Row) -> Partita :
        partita:Parita = Partita()
        partita.Lega = self.div
        partita.DataPartita = Row.GetDataPartita(self.date, self.time)
        partita.SquadraOspitante = Row.GetSquadraFromString(self.homeTeam)
        partita.SquadraOspite = Row.GetSquadraFromString(self.awayTeam)
        partita.EsitoFinale = Row.GetEsito(self.FTR)
        partita.EsitoPrimoTempo = Row.GetEsito(self.HTR)
        partita.GoalPrimoTempoOspitante = Row.GetGoals(self.HTHG)
        partita.GoalPrimoTempoOspite = Row.GetGoals(self.HTAG)
        partita.GoalFinaliOspitante = Row.GetGoals(self.FTHG)
        partita.GoalPrimoTempoOspite = Row.GetGoals(self.FTAG)
        return partita

    @staticmethod
    def GetDataPartita(data, orario) -> datetime:
        dataParsed = data.split('/')
        timeSplit = orario.split(':')
        return datetime(dataParsed[2], dataParsed[1], dataParsed[0], timeSplit[1], timeSplit[0])

    @staticmethod
    def GetDataPartita(squad) -> Squadra:
        if not squad:
            return Squadra.ERRORE
        elif squad.lower() == "juventus":
            return Squadra.Juventus
        elif squad.lower() == "fiorentina":
            return Squadra.Fiorentina
        elif squad.lower() == "verona":
            return Squadra.Verona  
        elif squad.lower() == "parma":
            return Squadra.Parma  
        elif squad.lower() == "genoa":
            return Squadra.Genoa   
        elif squad.lower() == "sassuolo":
            return Squadra.Sassuolo   
        elif squad.lower() == "milan":
            return Squadra.Milan   
        elif squad.lower() == "torino":
            return Squadra.Torino   
        elif squad.lower() == "cagliari":
            return Squadra.Cagliari   
        elif squad.lower() == "sampdoria":
            return Squadra.Sampdoria   
        elif squad.lower() == "inter":
            return Squadra.Inter   
        elif squad.lower() == "spezia":
            return Squadra.Spezia   
        elif squad.lower() == "napoli":
            return Squadra.Napoli   
        elif squad.lower() == "verona":
            return Squadra.Verona   
        elif squad.lower() == "crotone":
            return Squadra.Crotone   
        elif squad.lower() == "roma":
            return Squadra.Roma   
        elif squad.lower() == "bologna":
            return Squadra.Bologna
        elif squad.lower() == "benevento":
            return Squadra.Benevento
        elif squad.lower() == "udinese":
            return Squadra.Udinese
        elif squad.lower() == "lazio":
            return Squadra.Lazio
        else:
            return Squadra.ERRORE

    @staticmethod
    def GetEsito(text) -> Esito:
        if not text:
            return Esito.Parita
        elif text == "H":
            return Esito.HomeWon
        elif text == "A":
            return Esito.AwayWon
        else:
            return Esito.Parita
    
    @staticmethod
    def GetGoals(text) -> int:
        return