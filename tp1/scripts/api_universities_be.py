from pathlib import Path
import csv, json, requests

# On force HTTP et on interdit les redirections (pour éviter HTTPS)
API_URL = "http://universities.hipolabs.com/search?country=Belgium"

ROOT = Path(__file__).resolve().parents[1]
OUT_DIR = ROOT / "output" / "api"
OUT_DIR.mkdir(parents=True, exist_ok=True)

OUT_JSONL = OUT_DIR / "universities_be.jsonl"
OUT_CSV   = OUT_DIR / "universities_be.csv"

def fetch_universities_be():
    headers = {"User-Agent": "tac-tp1-eduina/1.0"}
    r = requests.get(API_URL, headers=headers, timeout=30, allow_redirects=False)
    r.raise_for_status()
    return r.json()

def write_jsonl(items, path):
    with path.open("w", encoding="utf-8") as f:
        for it in items:
            f.write(json.dumps(it, ensure_ascii=False) + "\n")

def write_csv(items, path):
    fields = ["name", "country", "alpha_two_code", "domains", "web_pages"]
    with path.open("w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=fields)
        w.writeheader()
        for it in items:
            w.writerow({
                "name": it.get("name"),
                "country": it.get("country"),
                "alpha_two_code": it.get("alpha_two_code"),
                "domains": ", ".join(it.get("domains", [])),
                "web_pages": ", ".join(it.get("web_pages", [])),
            })

def main():
    data = fetch_universities_be()
    write_jsonl(data, OUT_JSONL)
    write_csv(data, OUT_CSV)
    print(f"OK: {len(data)} universités → {OUT_JSONL} ; {OUT_CSV}")

if __name__ == "__main__":
    main()
