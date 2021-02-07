class SquadraEnum:
    """Enumeratore per il nome delle squadre"""
    Atalanta = "Atalanta"
    Benevento = "Benevento"
    Bologna = "Bologna"
    Cagliari = "Cagliari"
    Crotone = "Crotone"
    Fiorentina = "Fiorentina"
    Genoa = "Genoa"
    Inter = "Inter"
    Juventus = "Juventus"
    Lazio = "Lazio"
    Milan = "Milan"
    Napoli = "Napoli"
    Parma = "Parma"
    Roma = "Roma"
    Sampdoria = "Sampdoria"
    Sassuolo = "Sassuolo"
    Spezia = "Spezia"
    Torino = "Torino"
    Udinese = "Udinese"
    Verona = "Verona"

# Penso sia meglio fare una lista perche dobbiamo iterare. RM: Si, ma usa gli enumeratori
SquadraList:list[SquadraEnum] = [
    SquadraEnum.Atalanta,
    SquadraEnum.Benevento,
    SquadraEnum.Bologna,
    SquadraEnum.Cagliari,
    SquadraEnum.Crotone,
    SquadraEnum.Fiorentina,
    SquadraEnum.Genoa,
    SquadraEnum.Inter,
    SquadraEnum.Juventus,
    SquadraEnum.Lazio,
    SquadraEnum.Milan,
    SquadraEnum.Napoli,
    SquadraEnum.Parma,
    SquadraEnum.Roma,
    SquadraEnum.Sampdoria,
    SquadraEnum.Sassuolo,
    SquadraEnum.Spezia,
    SquadraEnum.Torino,
    SquadraEnum.Udinese,
    SquadraEnum.Verona
]

class Esito:
    """Descrive chi vince"""
    Draw = 0
    HomeWon = 1
    AwayWon = 2
