import requests
from granary import atom, jsonfeed, microformats2, rss
import datetime
import json
from tqdm import tqdm
import time

with open("acronyms_final.json", "r") as f:
    acronyms = json.load(f)

# https://www.reddit.com/dev/api/#GET_search
URL = "https://www.reddit.com/r/taylorswift/search.rss?q={acronym}&t=year&type=link&sort=relevance&restrict_sr=on&limit=100"

for acronym in tqdm(acronyms.keys()):
    if isinstance(acronyms[acronym], dict):
        print("Skipping", acronym)
        continue

    resp = requests.get(URL.format(acronym=acronym), headers={"User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36"})

    if resp.status_code != 200:
        print(resp.status_code, resp.text)
        print("Failed to fetch", acronym)
        continue

    activities = rss.to_activities(resp.text)

    acronyms[acronym] = {
        "song_name": acronyms[acronym],
        "mentions_in_year": len(activities),
    }

    print(acronym, acronyms[acronym])

    time.sleep(1.5)
    
    with open("acronyms_final.json", "w+") as f:
        json.dump(acronyms, f, indent=4)