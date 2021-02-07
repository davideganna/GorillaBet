from Partita import Partita 
from datetime import datetime

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
        partita.Esito =
        return partita

    @staticmethod
    def GetDataPartita(data, orario) -> datetime:
        dataParsed = data.split('/')
        timeSplit = orario.split(':')
        return datetime(dataParsed[2], dataParsed[1], dataParsed[0], timeSplit[1], timeSplit[0])

    @staticmethod
    def GetDataPartita(squad) -> Squadra:
        if not myString:
            return Squadra.ERRORE
        if squad.lower() == "juventus":
            return Squadra.juventus
        else if squad.lower() == "fiorentina":
            return Squadra.fiorentina
        else if squad.lower() == "verona":
            return Squadra.verona  
        else if squad.lower() == "parma":
            return Squadra.parma  
        else if squad.lower() == "genoa":
            return Squadra.genoa   
        else if squad.lower() == "sassuolo":
            return Squadra.sassuolo   
        else if squad.lower() == "milan":
            return Squadra.milan   
        else if squad.lower() == "torino":
            return Squadra.torino   
        else if squad.lower() == "cagliari":
            return Squadra.cagliari   
        else if squad.lower() == "sampdoria":
            return Squadra.sampdoria   
        else if squad.lower() == "inter":
            return Squadra.inter   
        else if squad.lower() == "spezia":
            return Squadra.spezia   
        else if squad.lower() == "napoli":
            return Squadra.napoli   
        else if squad.lower() == "verona":
            return Squadra.verona   
        else if squad.lower() == "crotone":
            return Squadra.crotone   
        else if squad.lower() == "roma":
            return Squadra.roma   
        else if squad.lower() == "bologna":
            return Squadra.bologna
        else if squad.lower() == "benevento":
            return Squadra.benevento
        else if squad.lower() == "udinese":
            return Squadra.udinese
        else if squad.lower() == "lazio":
            return Squadra.lazio
        else:
            return Squadra.ERRORE