import re, sys
from pathlib import Path
import requests, urllib3
from bs4 import BeautifulSoup
from tqdm import tqdm

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

LISTING_URL = "http://max.de.wilde.web.ulb.be/camille/"
ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "pdfs"
OUT_DIR.mkdir(parents=True, exist_ok=True)

def list_pdf_urls(listing_url: str):
    r = requests.get(listing_url, timeout=30, verify=False)
    r.raise_for_status()
    soup = BeautifulSoup(r.text, "html.parser")
    urls = []
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if href.lower().endswith(".pdf"):
            if href.startswith("http://") or href.startswith("https://"):
                href = href.replace("https://", "http://")
                urls.append(href)
            else:
                urls.append(requests.compat.urljoin(listing_url, href))
    return urls[:51]

def sanitize(name: str) -> str:
    return re.sub(r"[^\w\-.]+", "_", name)

def download(url: str, out_dir: Path):
    filename = sanitize(url.split("/")[-1]) or "file.pdf"
    dest = out_dir / filename
    if dest.exists():
        return dest
    with requests.get(url, stream=True, timeout=60, verify=False) as r:
        r.raise_for_status()
        total = int(r.headers.get("content-length", 0))
        with open(dest, "wb") as f, tqdm(total=total, unit="B", unit_scale=True, desc=filename) as pbar:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
                    pbar.update(len(chunk))
    return dest

def main():
    urls = list_pdf_urls(LISTING_URL)
    if not urls:
        print("Aucun PDF détecté. Vérifie la page:", LISTING_URL)
        sys.exit(1)
    print(f"{len(urls)} PDF détectés. Téléchargement vers {OUT_DIR} ...")
    ok = ko = 0
    for u in urls:
        try:
            download(u, OUT_DIR)
            ok += 1
        except Exception as e:
            ko += 1
            print(f"[ERREUR] {u}: {e}")
    print(f"Terminé. Succès: {ok}, Échecs: {ko}, Dossier: {OUT_DIR}")

if __name__ == "__main__":
    main()
