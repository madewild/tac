"""Scraping the AVB for PDFs of bulletins"""

import os
from pathlib import Path
import re
import time
import sys

import requests

def get_urls():
    """Retrieve all URLs from root AVB page"""
    root_url = "https://archives.bruxelles.be/bulletins/date"
    resp = requests.get(root_url)
    print(f"Status: {resp.status_code}")
    print(f"Encoding: {resp.encoding}")
    html = resp.text
    print(f"Text length: {len(html)}")

    pattern = r"https://archief.brussel.be/Colossus/BulletinsCommunaux/Bulletins/Documents/.*\.pdf"
    urls = re.findall(pattern, html)
    print(f"{len(urls)} PDF files found")
    return urls

def download(urls, offset=0):
    """Dowloading all files starting from offset"""
    for url in urls[offset:]:
        filename = url.split("/")[-1]
        print(f"Dowloading {filename}...")
        start_time = time.time()
        response = requests.get(url)
        print(f"   done in {(time.time() - start_time):.1f} seconds")
        Path("data/pdf").mkdir(parents=True, exist_ok=True)
        with open(f"data/pdf/{filename}", 'wb') as f:
            f.write(response.content)

def check(urls):
    """Check if all files have been downloaded"""
    ok_count = 0
    for url in urls:
        filename = url.split("/")[-1]
        downloads = os.listdir('data/pdf')
        if filename not in downloads:
            print(f"{filename} is missing!")
        else:
            ok_count += 1
    print(f"{ok_count} PDFs found on {len(urls)}!")

if __name__ == "__main__":
    all_urls = get_urls()
    try:
        task = sys.argv[1]
    except IndexError:
        print("No task provided, please use either 'download' or 'check'")
        exit()
    if task == "download":
        try:
            start_from = int(sys.argv[2])
        except IndexError:
            start_from = 0
        download(all_urls, start_from)
        check(all_urls)
    elif task == "check":
        check(all_urls)
    else:
        print("Unknown task, please use either 'download' or 'check'")
        exit()
