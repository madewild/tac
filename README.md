# TAC

Course material for "Traitement automatique de corpus" (STIC-B545) taught at [ULB](https://ulb.be)

Caution: Python 3.6 or higher required to handle [f-strings](https://www.python.org/dev/peps/pep-0498/) (3.7 is recommended)

It is recommended to run this code in a virtual environment: 

```
git clone git@github.com:madewild/tac.git
cd tac
pip install virtualenv
virtualenv venv --python=python3
source venv/bin/activate
which pip
```

Then install Python dependencies with `pip install -r requirements.txt`

## Module 1

`sql.py`: querying a simple relation database

`sparql.py`: querying the Wikidata SPARQL endpoint

`api.py`: playing with OpenStreetMap and EUcountries APIs

`scrape.py`: scraping the AVB to retrieve 2833 PDF bulletins

## Module 2

`convert.sh`: bash script to convert PDFs to TXTs, move them to dedicated folder and aggregate them in single big text file

`explore.py`: playing with various categories (city, year, decade, type...)

`freq.py`: basic frenquency analysis, hapaxes, long words...

## Module 3

### Keyword extraction

`keyword.py`: using YAKE to extract French keywords in each text file

`wordcloud.sh`: generating a wordcloud for a given year (calling `filter.py` in the background)

### Named-entity recognition

Install SpaCy from requirements then run this command to download French model: `python -m spacy download fr_core_news_sm`

`ner.py`: perform NER with SpaCy FR model

### Sentiment analysis

`sentiment.py`: analyse positive/negative sentences with textblob

## Module 4

Sentence tokenizer and word2vec model builder

## Module 5

Language detection with langid

## Module 6

