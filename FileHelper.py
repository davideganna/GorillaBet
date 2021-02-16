import csv
from Row import Row
import json, os.path

# .csv results source: https://www.football-data.co.uk/italym.php
_FILE_LIST_ = ["latest_results.csv"]
""""Elenco dei file che saranno letti dall'helper"""
_FILE_PATH_ = "SourceFiles\\"
"""Path della cartella dei file"""



class FileHelper(object):

    @staticmethod
    def compare_odds(program_odds, bwin_odds):
        positive_odds = []
        for i in range(len(program_odds)):
            positive_odds.append(bwin_odds[i] - program_odds[i])
            if positive_odds[i] < 0:
                positive_odds[i] = 0
        return positive_odds
    
    @staticmethod
    def get_flexible_names(squadra_home, squadra_away):
        if squadra_home == "milan":
            squadra_home = "ac milan"
        elif squadra_away == "milan":
            squadra_away = "ac milan"
        if squadra_home == "roma":
            squadra_home = "as roma"
        elif squadra_away == "roma":
            squadra_away = "as roma"
        return  [squadra_home, squadra_away]

    @staticmethod
    def GetFilePath(fileName):
        path = os.path.realpath(fileName)
        #return os.path.join(_FILE_PATH, fileName)
        return path

    @staticmethod
    def GetRowsFromFiles():
        result = []
        for file in _FILE_LIST_:
            fullPath = FileHelper.GetFilePath(file)
            #inserire un controllo se il file esiste o meno
            with open(fullPath) as sourceFile:
                sourceFile = csv.reader(sourceFile, delimiter=',')
                isFirst = True
                firstRow = ""
                for r in sourceFile:
                    #va modellizato il nuovo elemento e salvato in result
                    if  isFirst != True:
                        newElement = FileHelper.Mapping(firstRow, r)
                        result.append(newElement)
                    else:
                        firstRow = r
                        isFirst = False
        return result

    @staticmethod
    def Mapping(firstRow, r):
        newElement = Row()
        #da rivedere nel caso i merdoni del file cambiano la struttura del file nella remota possibilità
        #per Davide: si, sono un merdone
        newElement.div = r[0]
        newElement.date = r[1]
        newElement.time = r[2]
        newElement.homeTeam = r[3]
        newElement.awayTeam = r[4]
        newElement.FTHG = r[5]
        newElement.FTAG = r[6]
        newElement.FTR = r[7]
        newElement.HTHG = r[8]
        newElement.HTAG = r[9]
        newElement.HTR = r[10]
        newElement.HS = r[11]
        newElement.AS = r[12]
        newElement.HST = r[13]
        newElement.AST = r[14]
        newElement.HF = r[15]
        newElement.AF = r[16]
        newElement.HC = r[17]
        newElement.AC = r[18]
        newElement.HY = r[19]
        newElement.AY = r[20]
        newElement.HR = r[21]
        newElement.AR = r[22]  
        return newElement
