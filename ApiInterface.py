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
        'x-rapidapi-key': "" # It's replaced depending on the tester
    }

    @staticmethod
    def GetJsonResponse(data):
        return json.loads(data.decode("utf-8"))

    @staticmethod
    def MakeCall(endpoint):
        conn = http.client.HTTPSConnection(DashApi.url)
        conn.request("GET", endpoint, headers=DashApi.headers)
        res = conn.getresponse()
        data = res.read()
        return DashApi.GetJsonResponse(data)

    @staticmethod
    def GetResult(endpoint, fileName):
        if cache.IsFileUpdated(fileName):
            return cache.GetFromFile(fileName)
        else:
            jsonResult = MakeCall(endpoint)
            response = jsonResult["response"]
            cache.UpdateFile(fileName, json.dumps(response))
            return response

    @staticmethod
    def GetAllSquadre():
        fileName : str = "AllSquadre"
        endpoint : str = "/teams?league=135&season=2020"
        return GetResult(endpoint, fileName)

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
        if match in Match2FixtureId_Dict:
            target_id = Match2FixtureId_Dict[match]
            conn = http.client.HTTPSConnection(DashApi.url)
            conn.request("GET", "/odds?league=135&season=2020&fixture=" + str(target_id), headers=DashApi.headers)
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
        else: 
            print("Partita non trovata")
            return [-1, -1, -1]
