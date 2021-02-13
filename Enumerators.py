class SquadraEnum:
    """Enumeratore per il nome delle squadre"""
    Atalanta = "atalanta"
    Benevento = "benevento"
    Bologna = "bologna"
    Cagliari = "cagliari"
    Crotone = "crotone"
    Fiorentina = "fiorentina"
    Genoa = "genoa"
    Inter = "inter"
    Juventus = "juventus"
    Lazio = "lazio"
    Milan = "milan"
    Napoli = "napoli"
    Parma = "parma"
    Roma = "roma"
    Sampdoria = "sampdoria"
    Sassuolo = "sassuolo"
    Spezia = "spezia"
    Torino = "torino"
    Udinese = "udinese"
    Verona = "verona"

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
    "atalanta"  : 0,
    "benevento" : 1,
    "bologna"   : 2,
    "cagliari"  : 3,
    "crotone"   : 4,
    "fiorentina": 5,
    "genoa"     : 6,
    "inter"     : 7,
    "juventus"  : 8,
    "lazio"     : 9,
    "milan"     : 10,
    "napoli"    : 11,
    "parma"     : 12,
    "roma"      : 13,
    "sampdoria" : 14,
    "sassuolo"  : 15,
    "spezia"    : 16,
    "torino"    : 17,
    "udinese"   : 18,
    "verona"    : 19
}

Match2FixtureId_Dict = {
    
}

class Esito:
    """Descrive chi vince"""
    Draw = 0
    HomeWon = 1
    AwayWon = 2
