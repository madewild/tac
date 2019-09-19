"""Query Wikidata for Belgian politicians"""

from datetime import datetime as dt
import sys

from SPARQLWrapper import SPARQLWrapper, JSON

def get_rows():
    endpoint = "https://query.wikidata.org/bigdata/namespace/wdq/sparql"
    sparql = SPARQLWrapper(endpoint)

    statement = """
    SELECT DISTINCT ?person ?personLabel ?dateBirth ?dateDeath WHERE {
    ?person wdt:P27 wd:Q31 .
    ?person wdt:P106 wd:Q82955 .
    ?person wdt:P569 ?dateBirth .
    ?person wdt:P570 ?dateDeath .
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

def show(rows, n=10):
    """Display n politicians (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        birth_date = dt.strptime(row['dateBirth']['value'], date_format)
        death_date = dt.strptime(row['dateDeath']['value'], date_format)
        print(f"{row['personLabel']['value']} ({birth_date.year}-{death_date.year})")

if __name__ == "__main__":
    rows = get_rows()
    try:
        n = int(sys.argv[1])
    except IndexError:
        n = 10
    show(rows, n)
