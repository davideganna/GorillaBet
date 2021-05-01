import csv
import json, os.path
import pandas as pd

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
        return path

    @staticmethod
    def get_dataframe():
        fullPath = FileHelper.GetFilePath(_FILE_LIST_[0])
        with open(fullPath) as sourceFile:
            with open(fullPath) as sourceFile:
                df = pd.read_csv(sourceFile)
        return df
