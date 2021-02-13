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
SquadraList = [
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

SquadraDict = {
    "Atalanta"  : 0,
    "Benevento" : 1,
    "Bologna"   : 2,
    "Cagliari"  : 3,
    "Crotone"   : 4,
    "Fiorentina": 5,
    "Genoa"     : 6,
    "Inter"     : 7,
    "Juventus"  : 8,
    "Lazio"     : 9,
    "Milan"     : 10,
    "Napoli"    : 11,
    "Parma"     : 12,
    "Roma"      : 13,
    "Sampdoria" : 14,
    "Sassuolo"  : 15,
    "Spezia"    : 16,
    "Torino"    : 17,
    "Udinese"   : 18,
    "Verona"    : 19
}

Match2FixtureId_Dict = {
    
}

class Esito:
    """Descrive chi vince"""
    Draw = 0
    HomeWon = 1
    AwayWon = 2
