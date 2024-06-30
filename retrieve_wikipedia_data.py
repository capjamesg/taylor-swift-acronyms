import requests
import json
from bs4 import BeautifulSoup
import string
import re

url = "https://en.wikipedia.org/wiki/List_of_songs_by_Taylor_Swift"
page_content = requests.get(url).text

soup = BeautifulSoup(page_content, "html.parser")

tables = soup.find_all("table", class_="wikitable")

song_names = []
albums = []
for table in tables:
    rows = table.find_all("tr")
    for row in rows[1:]:
        heading = row.find("th")
        album = row.find_all("td")[2]
        if heading:
            song_names.append(heading.text.strip().replace('"', ""))

            albums.append(album.text.strip())
        else:
            print("No heading found for row", row)

acronyms = {}
duplicate_acronyms = {}

with open("acronyms.html", "w+") as f:
    for song in song_names:
        if not " " in song:
            continue

        # remove all punct
        original_song = song
        album = albums[song_names.index(song)]
        song = song.translate(str.maketrans("", "", string.punctuation)).replace(
            "  ", " "
        )

        words = song.split(" ")
        acronym = "".join([word[0] for word in words])

        # save to file if in album in albums more than 3 times
        count = albums.count(album)
        if count >= 3 and len(acronym) > 1:
            f.write(f"<li>{original_song} ({acronym})</li>")

        if acronym == "ATW1MV":
            acronym = "ATW10MV"

        if acronym in acronyms:
            if acronym not in duplicate_acronyms:
                duplicate_acronyms[acronym] = [acronyms[acronym]]
            duplicate_acronyms[acronym].append(original_song)
            continue

        acronyms[acronym] = {
            "song_name": original_song,
            "mentions_in_year": 0,
            "album": album,
        }

# remove all duplicates from the list used for frequency analysis
for acronym in duplicate_acronyms:
    del acronyms[acronym]

with open("duplicates.json", "w") as f:
    json.dump(duplicate_acronyms, f, indent=4)

with open("acronyms.json", "w") as f:
    json.dump(acronyms, f, indent=4)
