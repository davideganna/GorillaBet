from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
from BettingStrategy import *

#Fase 1 Aprire i file sorgente e ottenerne la struttura dati per ogni riga
rows:list[Row] = FileHelper.GetRowsFromFiles()
#conversione in una più cristiana variabile partita
partite:list[Partita] = []
r:Row
for r in rows:
    partite.append(r.GetPartita())
######################################

#Mapping delle squadre
squadre: list[Squadra] = []
sE: SquadraEnum
for s in SquadraList:
    newSquadra:Squadra = Squadra()
    newSquadra.Nome = s
    squadre.append(newSquadra)
p:Partita
for p in partite:
    squadraHome:Squadra = Helper.GetSquadraFromNome(squadre, p.SquadraHome)
    squadraAway:Squadra = Helper.GetSquadraFromNome(squadre, p.SquadraAway)
    squadraHome.PartiteGiocate.append(p)
    squadraAway.PartiteGiocate.append(p)
#######################

print_squadre(squadre)


