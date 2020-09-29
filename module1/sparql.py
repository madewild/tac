"""Query Wikidata for Belgian politicians"""

import argparse
from datetime import datetime as dt

from SPARQLWrapper import SPARQLWrapper, JSON

parser = argparse.ArgumentParser()
parser.add_argument('-f', '--filter', type=str, help='Filtering on name')
parser.add_argument('-n', '--number', type=int, help='Number of rows to display')

def get_rows():
    """Retrieve results from SPARQL"""
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?person ?personLabel ?dateBirth ?dateDeath WHERE {
        ?person wdt:P27 wd:Q31 .
        ?person wdt:P106 wd:Q82955 .
        ?person wdt:P569 ?dateBirth .
        OPTIONAL {?person wdt:P570 ?dateDeath .}
        SERVICE wikibase:label { bd:serviceParam wikibase:language "en" . }
    }
    ORDER BY ?personLabel
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Belgian politicians found\n")
    return rows

def show(rows, filter=None, n=10):
    """Display n politicians (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    if filter:
        rows = [row for row in rows if filter in row['personLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            birth_date = dt.strptime(row['dateBirth']['value'], date_format)
            birth_year = birth_date.year
        except ValueError:
            birth_year = "????"
        try:
            death_date = dt.strptime(row['dateDeath']['value'], date_format)
            death_year = death_date.year
        except ValueError:
            death_year = "????"
        except KeyError:
            death_year = "????"
        print(f"{row['personLabel']['value']} ({birth_year}-{death_year})")

if __name__ == "__main__":
    args = parser.parse_args()
    rows = get_rows()
    filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(rows, filter, number)
