"""Scraping the AVB for PDFs of bulletins"""

import os
import re
import requests
import time
import sys

def get_urls():
    """Initialize process"""
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

def download(urls, n=0):
    """Dowloading all files starting from n"""
    for url in urls[n:]:
        filename = url.split("/")[-1]
        print(f"Dowloading {filename}...")
        start_time = time.time()
        response = requests.get(url)
        print(f"   done in {(time.time() - start_time):.1f} seconds")
        with open(f"data/pdf/{filename}", 'wb') as f:
            f.write(response.content)

def check(urls):
    """Check if all files have been downloaded"""
    for url in urls:
        filename = url.split("/")[-1]
        downloads = os.listdir('data/pdf')
        if filename not in downloads:
            print(f"{filename} is missing!")

if __name__ == "__main__":
    all_urls = get_urls()
    try:
        task = sys.argv[1]
    except IndexError:
        print("No task provided, please use either 'download' or 'check'")
        sys.exit(1)
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
        sys.exit(1)
