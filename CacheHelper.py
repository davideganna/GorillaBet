import os.path, time, datetime, pathlib, json
from pathlib import Path

class CacheHelper:
    """Classe per gestire la cache"""
    filePath:str = "CacheFiles\\"
    fileExtension:str = ".json"
    @staticmethod
    def UpdateFile(fileName, jsonValue):
        fullPath : str = CacheHelper.filePath + fileName + CacheHelper.fileExtension
        filePointer = open(fullPath, "w")
        filePointer.write(jsonValue)
        filePointer.close()
        return
    @staticmethod
    def GetFromFile(fileName):
        fullPath : str = CacheHelper.GetFilePath(fileName)
        filePointer = open (fullPath, "r") 
        data = json.loads(filePointer.read())
        return data
    @staticmethod
    def IsFileUpdated(fileName) :
        """Serve per sapere se il file è aggiornato o meno"""
        fullPath = CacheHelper.GetFilePath(fileName)
        fname = pathlib.Path(fullPath)
        today = datetime.date.today()
        if os.path.isfile(fullPath):
            fileUpdateTime : datetime = datetime.datetime.fromtimestamp(fname.stat().st_mtime)
            datePart =  fileUpdateTime.date()
            if datePart >= today:
                return True
        return False
    @staticmethod 
    def GetFilePath(fileName):
        data_folder = Path(CacheHelper.filePath)
        file_to_open = data_folder / fileName
        print(file_to_open)
        return file_to_open