import http.client
import urllib.parse
import json


class DashApi:
    """Classe middleware per l'API"""
    url: str = "v3.football.api-sports.io"
    headers = {
        'x-rapidapi-host': url,
        # 'x-rapidapi-key': "6fb51c5c8788961e2f02bc09b221b3ce"  # Chiave Mirko
        # 'x-rapidapi-key': "6fb51c5c8788961e2f02bc09b221b3ce" #Chiave Davide
        'x-rapidapi-key': "e5c09ffce045356e24a0c225e2352a4d"  # Chiave Varsa
    }

    @staticmethod
    def GetAllSquadre() -> list:
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        conn.request("GET", "/teams?league=135&season=2020",
                     headers=DashApi.headers)
        res = conn.getresponse()
        data = res.read()
        jsonResult = DashApi.GetJsonResponse(data)
        squadre: list = []
        for t in jsonResult["response"]:
            squadre.append(t["team"])
        return squadre

    @staticmethod
    def GetAllFixturesIds():
        conn = http.client.HTTPSConnection(DashApi.url)
        conn.request(
            "GET", "/fixtures?next=10&league=135&season=2020", headers=DashApi.headers)
        res = conn.getresponse()
        data = res.read()
        jsonResult = DashApi.GetJsonResponse(data)
        fixture_ids: list = []
        matches: list = []
        for result in jsonResult["response"]:
           fixture_ids.append(result["fixture"]["id"])
           matches.append(result["teams"]["home"]["name"] + result["teams"]["away"]["name"])
        return [fixture_ids, matches]

    @staticmethod
    def GetJsonResponse(data):
        return json.loads(data.decode("utf-8"))
