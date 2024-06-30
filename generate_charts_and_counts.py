from matplotlib import pyplot as plt
import json
import os
from collections import Counter
import re

# make album dir
if not os.path.exists("results"):
    os.mkdir("results")

with open("acronyms.json", "r") as f:
    album_acronyms = json.load(f)

with open("acronyms_final.json", "r") as f:
    acronyms = json.load(f)

# strip all album names
for k, v in album_acronyms.items():
    v["album"] = v["album"].strip()

albums = [v["album"] for v in album_acronyms.values()]

# get all albums with at least four entries
albums = [k for k, v in Counter(albums).items() if v >= 4]

for album in albums:
    album_acronyms_filtered = {f"{album_acronyms.get(k)['song_name']} ({k})": {
        "mentions_in_year": v.get("mentions_in_year", 0),
        "acronym": k,
    } for k, v in acronyms.items() if album_acronyms.get(k, {}).get("album") == album and len(k) > 2}
    # sort by mentions
    album_acronyms_filtered = {k: v for k, v in sorted(album_acronyms_filtered.items(), key=lambda x: x[1].get("mentions_in_year", 0), reverse=True)}

    if album_acronyms_filtered:
        # plot, has 150 values, so needs to be big
        plt.figure(figsize=(30, 10))
        # plot sideways, not up and down; if acronym in last parenthesis is length 2, color lightgrey, else royalblue
        colors = ["lightgrey" if len(k.get("acronym", "")) == 2 else "royalblue" for k in album_acronyms_filtered.values()]
        print([len(k.get("acronym", "")) for k in album_acronyms_filtered.values()])

        plt.barh(list(album_acronyms_filtered.keys()), [v.get("mentions_in_year", 0) for v in album_acronyms_filtered.values()], color=colors)
        plt.title(f"Mentions of {album} songs in r/taylorswift subreddit (last year)")
        plt.ylabel("Song (acronym)")
        plt.xlabel("Number of mentions")
        plt.xticks(rotation=45)
        # save as results/album.png
        plt.savefig(f"results/{album}.png")
        plt.close()
        # print results as text
        print(f"Results for {album}:")
        for k, v in album_acronyms_filtered.items():
            print(f"{k}: {v.get('mentions_in_year')} mentions")
        print("\n\n")

# print top 5 most used acronyms
most_used = sorted(acronyms.items(), key=lambda x: x[1].get("mentions_in_year", 0), reverse=True)[:50]
# remove if 2 letters long
most_used = [(k, v) for k, v in most_used if len(k) > 2]

print("Top 5 most used acronyms:")
for acronym, data in most_used:
    print(f"{data.get('song_name')} ({acronym}): {data.get('mentions_in_year')} mentions")
