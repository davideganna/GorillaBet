class Squadra:
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
    ERRORE = "0"

class Esito:
    """Descrive chi vince"""
    Parita = 0
    Ospitante = 1
    Ospite = 2

# Penso sia meglio fare una lista perche dobbiamo iterare. RM: Si, ma usa gli enumeratori
SquadraList:List[Squadra] = [
    """Lista con tutte le squadre partecipanti"""
    Squadra.Juventus,
    Squadra.Fiorentina,,
    Squadra.Verona,
    Squadra.Parma,
    Squadra.Genoa,,
    Squadra.Sassuolo,
    Squadra.Milan,
    Squadra.Torino,
    Squadra.Cagliari,
    Squadra.Sampdoria,
    Squadra.Inter,
    Squadra.Spezia,
    Squadra.Napoli,
    Squadra.Verona,
    Squadra.Crotone,
    Squadra.Roma,
    Squadra.Bologna,
    Squadra.Benevento,
    Squadra.Udinese,
    Squadra.Lazio,
]


class Esito:
    """Descrive chi vince"""
    Draw = 0
    HomeWon = 1
    AwayWon = 2
