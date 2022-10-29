import json
from urllib import parse, request



def gif_links(recherche):
  url = "http://api.giphy.com/v1/gifs/search"

  params = parse.urlencode({
    "q": recherche,
    "api_key": "ta44Kv2nKNkQ1OfOKoovjgpPWBDaUZCS",
    "limit": "5"
  })

  with request.urlopen("".join((url, "?", params))) as response:
    data = json.loads(response.read())

  print(json.dumps(data, sort_keys=True, indent=4))

  return data

liste = []
def formater(data):
  global liste
  for elem in data["data"]:
    liste.append(elem["images"]["original"]["url"])
    print(elem["images"]["original"]["webp"])
  return liste


