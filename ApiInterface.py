import http.client
import urllib.parse
import json, asyncio
from Enumerators import *
from CacheHelper import CacheHelper as cache
class DashApi:
    """Classe middleware per l'API"""

    url = "v3.football.api-sports.io"
    headers = {
        'x-rapidapi-host': url,
        'x-rapidapi-key': "6fb51c5c8788961e2f02bc09b221b3ce" # Chiave Mirko
        #'x-rapidapi-key': "648939b99aca43ba86c7c75455b9fc61" # Chiave Davide
        # 'x-rapidapi-key': "e5c09ffce045356e24a0c225e2352a4d" # Chiave Varsa
    }

    @staticmethod
    def GetAllSquadre():
        conn = http.client.HTTPSConnection("v3.football.api-sports.io")
        fileName : str = "AllSquadre"
        if cache.IsFileUpdated(fileName):
            return cache.GetFromFile(fileName)
        else:
            conn.request("GET", "/teams?league=135&season=2020", headers=DashApi.headers)
            res = conn.getresponse()
            data = res.read()
            jsonResult = DashApi.GetJsonResponse(data)
            cache.UpdateFile(fileName, json.dumps(jsonResult["response"]))
            return jsonResult["response"]

    @staticmethod
    def Create_Match_2_Dict():
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
           matches.append(result["teams"]["home"]["name"].lower() + result["teams"]["away"]["name"].lower())
        Match2FixtureId_Dict = dict.fromkeys(matches, 0)
        for n, match in enumerate(matches):
            Match2FixtureId_Dict[match] = fixture_ids[n]
        return Match2FixtureId_Dict
    
    @staticmethod
    def Get_Odds_from_match(match):
        Match2FixtureId_Dict = DashApi.Create_Match_2_Dict()
        target_id = Match2FixtureId_Dict[match]
        conn = http.client.HTTPSConnection(DashApi.url)
        conn.request(
            "GET", "/odds?league=135&season=2020&fixture=" + str(target_id), headers=DashApi.headers)
        res = conn.getresponse()
        data = res.read()
        jsonResult = DashApi.GetJsonResponse(data)
        for n, result in enumerate(jsonResult["response"][0]["bookmakers"][0]["bets"][0]["values"]):
            if result["value"] == "Home":
                home_wins_odds = result["odd"]
            elif result["value"] == "Draw":
                draw_odds = result["odd"]
            elif result["value"] == "Away":
                away_wins_odds = result["odd"]
        return [home_wins_odds, draw_odds, away_wins_odds]

    @staticmethod
    def GetJsonResponse(data):
        return json.loads(data.decode("utf-8"))
