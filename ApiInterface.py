import http.client, urllib.parse
import json

class DashApi:
    """Classe middleware per l'API"""

    @staticmethod
    def GetAllSquadre() -> list:    
        headers = {
        'x-rapidapi-host': "v3.football.api-sports.io",
        'x-rapidapi-key': "6fb51c5c8788961e2f02bc09b221b3ce"
        }
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        conn.request("GET", "/teams?league=135&season=2020", headers=headers)
        res = conn.getresponse()
        data = res.read()
        jsonResult = json.loads(data.decode("utf-8"))
        squadre : list = []
        for t in jsonResult["response"]:
            squadre.append(t["team"])
        return squadre
