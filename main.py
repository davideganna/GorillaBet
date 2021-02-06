from FileHelper import FileHelper
from Row import Row
from Enumerators import *

#Fase 1 Aprire i file sorgente e ottenerne la struttura dati per ogni riga

#forse l'idea delle classi è diversa in python?
rows:list[Row] = FileHelper.GetRowsFromFiles()

yuveInCasa : list[Row] = []
r: Row
for r in rows:
    if r.homeTeam == Squadra.Juventus:
        yuveInCasa.append(r)
for r in yuveInCasa:
    print(r.FTHG)
