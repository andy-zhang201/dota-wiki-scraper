import requests
from requests.exceptions import RequestException
from contextlib import closing
from bs4 import BeautifulSoup
#from dotahero import heroids

match_id = 5482502874
r= requests.get("https://api.opendota.com/api/matches/%s"%match_id)

jstring = r.json()
# Dict
print(type(jstring))

# Print match id
print(jstring["match_id"])

print("the Heroes are: ")
# print(jstring["picks_bans"][0])

for i in range(len(jstring["picks_bans"])):
    if (jstring["picks_bans"][i]["is_pick"]!=1):
        print("Banned Hero: ")
    else:
        print("Picked Hero: ")
    print(jstring["picks_bans"][i]["hero_id"])

