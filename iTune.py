import requests
import sys
import json

if len(sys.argv) != 2:
    sys.exit()

response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1]) # term = weezer

result = response.json()
for song in result["results"]:
    # print("CollectionName:", song['collectionName'])
    print("TrackName:", song['trackName'])
# print(json.dumps(result["results"], indent=4))


