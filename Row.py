from Partita import Partita 
from datetime import datetime
from Enumerators import *

class Row:
    """Classe per la descrizione della singola riga"""
    def __init__(self):
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
        """Risultato squadra in casa primo tempo"""
        HTAG: str 
        """Risultato squadra ospite primo tempo"""
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

    def GetPartita(self) -> Partita :
        partita:Partita = Partita()
        partita.Lega = self.div
        partita.DataPartita = Row.GetDataPartita(self.date, self.time)
        partita.SquadraHome = Row.GetSquadraFromString(self.homeTeam)
        partita.SquadraAway = Row.GetSquadraFromString(self.awayTeam)
        partita.EsitoFinale = Row.GetEsito(self.FTR)
        partita.EsitoPrimoTempo = Row.GetEsito(self.HTR)
        partita.GoalPrimoTempoHome = Row.GetGoals(self.HTHG)
        partita.GoalPrimoTempoAway = Row.GetGoals(self.HTAG)
        partita.GoalFinaliHome = Row.GetGoals(self.FTHG)
        partita.GoalFinaliAway = Row.GetGoals(self.FTAG)
        return partita

    @staticmethod
    def GetDataPartita(data, orario) -> datetime:
        dataParsed = data.split('/')
        timeSplit = orario.split(':')
        return datetime(int(dataParsed[2]), int(dataParsed[1]), int(dataParsed[0]), int(timeSplit[0]), int(timeSplit[1]))

    @staticmethod
    def GetSquadraFromString(squad) -> SquadraEnum:
        if not squad:
            return SquadraEnum.ERRORE
        elif squad.lower() == "juventus":
            return SquadraEnum.Juventus
        elif squad.lower() == "fiorentina":
            return SquadraEnum.Fiorentina
        elif squad.lower() == "verona":
            return SquadraEnum.Verona  
        elif squad.lower() == "parma":
            return SquadraEnum.Parma  
        elif squad.lower() == "genoa":
            return SquadraEnum.Genoa   
        elif squad.lower() == "sassuolo":
            return SquadraEnum.Sassuolo   
        elif squad.lower() == "milan":
            return SquadraEnum.Milan   
        elif squad.lower() == "torino":
            return SquadraEnum.Torino   
        elif squad.lower() == "cagliari":
            return SquadraEnum.Cagliari   
        elif squad.lower() == "sampdoria":
            return SquadraEnum.Sampdoria   
        elif squad.lower() == "inter":
            return SquadraEnum.Inter   
        elif squad.lower() == "spezia":
            return SquadraEnum.Spezia   
        elif squad.lower() == "napoli":
            return SquadraEnum.Napoli   
        elif squad.lower() == "verona":
            return SquadraEnum.Verona   
        elif squad.lower() == "crotone":
            return SquadraEnum.Crotone   
        elif squad.lower() == "roma":
            return SquadraEnum.Roma   
        elif squad.lower() == "bologna":
            return SquadraEnum.Bologna
        elif squad.lower() == "benevento":
            return SquadraEnum.Benevento
        elif squad.lower() == "udinese":
            return SquadraEnum.Udinese
        elif squad.lower() == "lazio":
            return SquadraEnum.Lazio
        elif squad.lower() == "atalanta":
            return SquadraEnum.Atalanta
        else:
            return SquadraEnum.ERRORE

    @staticmethod
    def GetEsito(text) -> int:
        if not text:
            return Esito.Draw
        elif text == "H":
            return Esito.HomeWon
        elif text == "A":
            return Esito.AwayWon
        else:
            return Esito.Draw
    
    @staticmethod
    def GetGoals(text) -> int:
        if not text:
            return None
        return int(text)