import json

import requests

url = "https://akabab.github.io/superhero-api/api/all.json"
params = {"work"}
intellect = {}
response = requests.get(url)
all_heroes = response.json()


for x in all_heroes:
    if x["name"] == "Hulk":
        intellect["Hulk"] = x["powerstats"]["intelligence"]
    elif x["name"] == "Captain America":
        intellect["Captain America"] = x["powerstats"]["intelligence"]
    elif x["name"] == "Thanos":
        intellect["Thanos"] = x["powerstats"]["intelligence"]
   

max_int_hero = list(max(intellect.items(), key=lambda int_hero: int_hero[1]))


print(f"Самым умным являеться {max_int_hero[0]} его интелект равен {max_int_hero[1]}")
