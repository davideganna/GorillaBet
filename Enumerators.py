class SquadraEnum:
    """Enumeratore per il nome delle squadre"""
    Juventus = "Juventus"
    Fiorentina = "Fiorentina"
    Verona = "Verona"
    Parma = "Parma"
    Genoa = "Genoa"
    Sassuolo = "Sassuolo"
    Milan = "Milan"
    Torino = "Torino"
    Cagliari = "Cagliari"
    Sampdoria = "Sampdoria"
    Inter = "Inter"
    Spezia = "Spezia"
    Napoli = "Napoli"
    Verona = "Verona"
    Crotone = "Crotone"
    Roma = "Roma"
    Bologna = "Bologna"
    Benevento = "Benevento"
    Udinese = "Udinese"
    Lazio = "Lazio"
    Atalanta = "Atalanta"
    ERRORE = "0"

class Esito:
    """Descrive chi vince"""
    Parita = 0
    Ospitante = 1
    Ospite = 2

# Penso sia meglio fare una lista perche dobbiamo iterare. RM: Si, ma usa gli enumeratori
SquadraList:list[SquadraEnum] = [
    SquadraEnum.Juventus,
    SquadraEnum.Fiorentina,
    SquadraEnum.Verona,
    SquadraEnum.Parma,
    SquadraEnum.Genoa,
    SquadraEnum.Sassuolo,
    SquadraEnum.Milan,
    SquadraEnum.Torino,
    SquadraEnum.Cagliari,
    SquadraEnum.Sampdoria,
    SquadraEnum.Inter,
    SquadraEnum.Spezia,
    SquadraEnum.Napoli,
    SquadraEnum.Verona,
    SquadraEnum.Crotone,
    SquadraEnum.Roma,
    SquadraEnum.Bologna,
    SquadraEnum.Benevento,
    SquadraEnum.Udinese,
    SquadraEnum.Lazio,
    SquadraEnum.Atalanta,
    SquadraEnum.ERRORE
]


class Esito:
    """Descrive chi vince"""
    Draw = 0
    HomeWon = 1
    AwayWon = 2
