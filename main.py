from FileHelper import FileHelper
from Row import Row
from Enumerators import *
from Partita import Partita 
from Squadra import Squadra
from Helper import Helper
from BettingStrategy import *
from ReadableBettingStrategy import ReadableBettingStrategy
rows:list[Row] = FileHelper.GetRowsFromFiles()
partite:list[Partita] = []
r:Row
for r in rows:
    partite.append(r.GetPartita())
squadre: list[Squadra] = []
sE: SquadraEnum
for s in SquadraList:
    newSquadra:Squadra = Squadra(s)
    squadre.append(newSquadra)
p:Partita
for p in partite:
    squadraHome:Squadra = Helper.GetSquadraFromNome(squadre, p.SquadraHome)
    squadraAway:Squadra = Helper.GetSquadraFromNome(squadre, p.SquadraAway)
    squadraHome.PartiteGiocate.append(p)
    squadraAway.PartiteGiocate.append(p)
    print(len(squadraHome.PartiteGiocate))
create_matrix()
ReadableBettingStrategy.CalculateStats(squadre)