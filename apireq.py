from collections import defaultdict
from sortedcontainers import SortedList
import requests
import json
import pymongo 

# LEADERBOARD
PLAYERS = ["mc30_203", "ET-YU", "AyCihihi"]

header = {
  "Authorization": "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIwNzFhNWNlMC05NzQ0LTAxM2ItMTAzNy0wNTFiYTE3ZTlmN2MiLCJpc3MiOiJnYW1lbG9ja2VyIiwiaWF0IjoxNjc3MzM0MjA1LCJwdWIiOiJibHVlaG9sZSIsInRpdGxlIjoicHViZyIsImFwcCI6Ii1hOTNmNjI0Zi04NTgzLTRiZTEtYmQ2Mi04ZTk3MzQzMTBmMDIifQ.t2kVmYFrk6_c2EiSeQZuW8KSZV3vmsEWFdJNiK3WXA0",
  "Accept": "application/vnd.api+json"
}

# with open("player.json", "w") as outfile:
#     # write the data to the file in JSON format
#     json.dump(data, outfile)
    
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["mydatabase"]
mydb = db["mycollection"]

# mydb.drop()

topGames = defaultdict(SortedList)
for player in PLAYERS:
  url = f'https://api.pubg.com/shards/steam/players?filter[playerNames]={player}'
  r = requests.get(url, headers=header)
  data = r.json()
  matches = [item["id"] for item in data["data"][0]['relationships']['matches']["data"]]
  for match_id in matches:
    url_match = f'https://api.pubg.com/shards/steam/matches/{match_id}'
    r_match = requests.get(url_match, headers=header)
    data_match = r_match.json()
    
    statics = [item["attributes"]["stats"] for item in data_match["included"] if item["type"] == "participant"]
    for stat in statics:
        # my_json = json.dumps(stat, indent=None)
        stat["matchType"] = data_match["data"]["attributes"]["matchType"]
        mydb.insert_one(stat)
  
      
  docs = mydb.find({"name": player})
  
  for doc in docs:
    # print(doc)
    if doc["matchType"] == "official":
      rank = 0.4 * doc["timeSurvived"] + 0.3 * doc["walkDistance"] + 0.2 * doc["damageDealt"] + 0.1 * doc["kills"] + 0.05 * doc["heals"] + 0.05 * doc["boosts"]
    elif doc["matchType"] == "arcade":
      rank = 0.4 * doc["kills"] + 0.3 * doc["damageDealt"] + 0.2 * doc["winPlace"] + 0.1 * doc["timeSurvived"]
    else:
      rank = 0.3 * doc["kills"] + 0.3 * doc["damageDealt"] + 0.2 * doc["winPlace"] + 0.1 * doc["timeSurvived"] + 0.05 * doc["walkDistance"] + 0.05 * doc["boosts"] + 0.05 * doc["revives"]
    if len(topGames[player]) < 10:
      topGames[player].add(rank)
    else:
      if topGames[player][0] < rank:
        topGames[player].discard(topGames[player][0])
        topGames[player].add(rank)
  print(topGames)
  print(sum(topGames[player]))

new_dict = {}
for i in topGames:
  new_dict[i] = sum(topGames[i])/len(topGames[i])
  
sorted_dict = dict(sorted(new_dict.items(), key=lambda item: item[1], reverse=True))

print("---LEADERBOARD---")
print("name       rank")
for i in sorted_dict:
  print(i, "   ", sorted_dict[i])
  
  

# TEAMMATES/ENEMY MATCHING
# Classic (survival) mode
# For this mode we will have database which contains attributes which are more important in this mode
data_classic = {
  "DBNOs": 0,
  "assists": 0,
  "boosts": 0,
  "damageDealt": 1703.0154,
  "headshotKills": 4,
  "heals": 0,
  "killPlace": 9,
  "killStreaks": 2,
  "kills": 12,
  "revives": 0,
  "roadKills": 0,
  "teamKills": 0,
  "timeSurvived": 799.362,
  "walkDistance": 0,
  "weaponsAcquired": 0,
  "winPlace": 2
}

# Arcade (kill-based) mode
data_arcade = {
  "DBNOs": 0,
  "assists": 0,
  "boosts": 0,
  "damageDealt": 1703.0154,
  "deaths" : 0,
  "headshotKills": 4,
  "heals": 0,
  "killPlace": 9,
  "killStreaks": 2,
  "kills": 12,
  "longestkill": 87.213,
  "winPlace": 2
}