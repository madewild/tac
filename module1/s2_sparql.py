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
    # Politiciens belges nes apres 1700 dont le pere OU le ou les freres et soeurs sont des politiciens (accents omis, car ils causent des problemes)
    SELECT ?child ?childLabel ?fatherLabel ?dob ?dod ?siblingLabel
    WHERE 
    {
        ?child wdt:P31 wd:Q5. #humain
        ?child wdt:P27 wd:Q31. #Belge
        ?child wdt:P106 wd:Q82955. # politicien
        {
        ?child wdt:P22 ?father. #ont un pere
        ?father wdt:P106 wd:Q82955. #qui est politicien
        }
        UNION
        {?child wdt:P3373 ?sibling. #ont un frere ou une soeur
        ?sibling wdt:P106 wd:Q82955. #qui est politicien(ne)
        }
        ?child wdt:P569 ?dob
        ?child wdt:P570 ?dod

        FILTER (YEAR(?dob) > 1700)


        SERVICE wikibase:label { bd:serviceParam wikibase:language "[AUTO_LANGUAGE],en". }
    }
    """

    sparql.setQuery(statement)
    sparql.setReturnFormat(JSON)
    results = sparql.query().convert()

    rows = results['results']['bindings']
    print(f"\n{len(rows)} Belgian politicians found\n")
    return rows

def show(rows, name_filter=None, n=10):
    """Display n politicians (default=10)"""
    date_format = "%Y-%m-%dT%H:%M:%SZ"
    if name_filter:
        rows = [row for row in rows if name_filter in row['childLabel']['value'].lower()]
    print(f"Displaying the first {n}:\n")
    for row in rows[:n]:
        try:
            birth_date = dt.strptime(row['dob']['value'], date_format)
            birth_year = birth_date.year
        except ValueError:
            birth_year = "????"
        try:
            death_date = dt.strptime(row['dod']['value'], date_format)
            death_year = death_date.year
        except ValueError: # unknown death date
            death_year = "????"
        except KeyError: # still alive
            death_year = ""
        print(f"{row['childLabel']['value']} ({birth_year}-{death_year})")

if __name__ == "__main__":
    args = parser.parse_args()
    my_rows = get_rows()
    my_filter = args.filter if args.filter else None
    number = args.number if args.number else 10
    show(my_rows, my_filter, number)
