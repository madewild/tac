"""Scraping the AVB for PDFs of bulletins"""

import re
import requests
import time

pdf_list = []

root_url = "https://archives.bruxelles.be/bulletins/date"
resp = requests.get(root_url)
print(f"Status: {resp.status_code}")
print(f"Encoding: {resp.encoding}")
html = resp.text
print(f"Text length: {len(html)}")

pattern = r"https://archief.brussel.be/Colossus/BulletinsCommunaux/Bulletins/Documents/.*\.pdf"
urls = re.findall(pattern, html)
print(f"{len(urls)} PDF files found")

for url in urls:
    filename = url.split("/")[-1]
    print(f"Dowloading {filename}...")
    start_time = time.time()
    response = requests.get(url)
    print(f"   done in {time.time() - start_time} seconds")
    with open(f"data/{filename}", 'wb') as f:
        f.write(response.content)
