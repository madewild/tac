"""Query sample MySQL database"""

import argparse
import os.path
import sqlite3
import zipfile
from pathlib import Path

import requests

parser = argparse.ArgumentParser()
parser.add_argument('-a', '--artist', type=str, help='Filtering on artist name')
args = parser.parse_args()

if not os.path.isfile('data/db/chinook.db'): 
    url = "https://www.sqlitetutorial.net/wp-content/uploads/2018/03/chinook.zip"
    filename = url.split("/")[-1]
    Path("data/db").mkdir(parents=True, exist_ok=True)
    save_loc = f"data/db/{filename}"
    response = requests.get(url)

    with open(save_loc, 'wb') as f:
        f.write(response.content)

    with zipfile.ZipFile(save_loc, 'r') as zip_ref:
        zip_ref.extractall("data/db/")

conn = sqlite3.connect('data/db/chinook.db')
c = conn.cursor()

artist = args.artist
query1 = "SELECT ArtistId from artists WHERE Name = ?"
c.execute(query1, (artist,))
artist_id = c.fetchone()

if artist_id:
    query2 = "SELECT * from albums where ArtistId = ?"
    albums_ids = []
    for row in c.execute(query2, artist_id):
        albums_ids.append(str(row[0]))

    query3 = f'SELECT Name, AlbumId FROM tracks WHERE AlbumId IN ({",".join(albums_ids)})'
    songs = set()
    for row in c.execute(query3):
        songs.add(row[0])

    print(f"\n{len(songs)} distinct songs found:\n")
    for song in sorted(songs):
        print(song)
else:
    print("Artist not found")
