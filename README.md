# TAC

Ce répertoire contient le matériel pour le cours de "Traitement automatique de corpus" ([STIC-B545](https://www.ulb.be/fr/programme/stic-b545)) donné à l'[ULB](https://ulb.be).

## Installation

1. Créez un compte Github et générez un `fork` du répertoire [tac](https://github.com/madewild/tac). Votre version du répertoire se trouvera alors à l'adresse `https://github.com/<YOUR-GITHUB-ID>/tac`
2. Installez [uv](https://docs.astral.sh/uv/getting-started/installation/), l'outil qui gère à la fois Python, l'environnement virtuel et les dépendances du projet:
    - Windows (PowerShell):

        ```powershell
        powershell -ExecutionPolicy ByPass -c "irm https://astral.sh/uv/install.ps1 | iex"
        ```
        Vous aurez peut-être à ajouter votre .local/bin au chemin d'exécution pour pouvoir exécuter les commandes `uv`:
        
        ```powershell
        $env:Path = "$env:Path = "$HOME\.local\bin;$env:Path"
        ```
        
        Et autoriser l'exécution de scripts via le terminal : 
        ```powershell
        Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
        ```


    - MacOS / Linux:

        ```bash
        curl -LsSf https://astral.sh/uv/install.sh | sh
        ```

    - !! Vous n'avez pas besoin d'installer Python vous-même: `uv` télécharge et gère automatiquement la version requise (>= 3.11, < 3.14) au moment de l'installation du projet.
    - !! Si votre ordinateur ne supporte pas les versions récentes de Python, vous pouvez utiliser une machine virtuelle Docker. Vous trouverez les instructions [ici](./Installation_Docker.md)
3. Téléchargez et installez [Git](https://git-scm.com/downloads)
4. Téléchargez et installez [Visual Studio Code](https://code.visualstudio.com/)
5. Dans Visual Studio Code, ouvrez un terminal (`Terminal > New Terminal`) et déplacez-vous dans le dossier qui contiendra les documents du cours (utilisez la commande `cd`)
6. Exécutez les commandes suivantes **une ligne à la fois**:

```bash
git clone https://github.com/<YOUR-GITHUB-ID>/tac

cd tac

uv sync
```

Cette dernière commande télécharge la bonne version de Python si nécessaire, crée l'environnement virtuel dans `.venv`, et installe toutes les dépendances du projet (listées dans `pyproject.toml`, versions figées dans `uv.lock`) — en une seule étape.

7. Vous pouvez maintenant utiliser et exécuter le code qui se trouve dans les notebooks (fichiers `.ipynb`) en choisissant l'environnement Python situé dans `.venv` (VS Code devrait le proposer automatiquement)

### Installer une librairie supplémentaire

Certains notebooks utilisent des librairies additionnelles (par exemple `transformers`, `torch` dans le module 5) qui ne sont volontairement pas installées par défaut, car lourdes et propres à un seul notebook. Une cellule en début de notebook s'en charge via:

```bash
!uv pip install <nom-de-la-librairie>
```

Si vous voulez ajouter une librairie de façon permanente au projet (utilisée dans plusieurs notebooks), utilisez plutôt depuis un terminal, à la racine du répertoire:

```bash
uv add <nom-de-la-librairie>
```

Cette commande met à jour `pyproject.toml` et `uv.lock` automatiquement.

## Module 1

[`s1_sql`](module1/s1_sql.ipynb): requêtes dans une base de données SQL

[`s2_api`](module1/s2_api.ipynb): requêtes sur les APIs _OpenStreetMap_ et _EUcountries_

[`s3_scrape`](module1/s3_scrape.ipynb): scraping d'articles dans les archives du journal _Le Soir_

## Module 2

[`s1_convert`](module2/s1_convert.ipynb): conversion de fichiers `.pdf` en fichier `.txt`, et aggrégation en un long fichier texte

[`s2_explore`](module2/s2_explore.ipynb): statistiques de fréquences de fichiers

[`s3_freq`](module2/s3_freq.ipynb): Analyse des fréquences, des _hapax_, recherche des mots les plus longs...

## Module 3

### Extraction de mots-clés

[`s1_keywords`](module3/s1_keywords.ipynb): utilisation de YAKE pour extraire des keywords au sein de chacun des fichiers

[`s2_wordcloud`](module3/s2_wordcloud.ipynb): génération d'un nuage de mots

### Reconnaissance d'entités nommées

[`s3_ner`](module3/s3_ner.ipynb): reconnaissance d'entités à l'aide d'un modèle SpaCy

### Analyse de sentiments

[`s4_sentiment`](module3/s4_sentiment.ipynb): analyse de sentiment à l'aide de Textblob

## Module 4

[`s1_classification`](module4/s1_classification.ipynb): classification supervisée de textes

[`s2_clustering`](module4/s2_clustering.ipynb): clustering non supervisé à l'aide de K-means

[`s3_word_embeddings`](module4/s3_word_embeddings.ipynb): exploration du modèle Word2Vec sur un corpus

## Module 5

[`s1_language_detection`](module5/s1_language_detection.ipynb): identification de la langue d'un texte

[`s2_machine_translation`](module5/s2_machine_translation.ipynb): traduction automatique à l'aide de modèle _transformers_

[`s3_anonymization`](module5/s3_anonymization.ipynb): anonymisation/pseudonymisation de données with Faker

## Module 6

[`s1_extraction`](module6/s1_extraction.ipynb): extraction de texte à partir de formats variés

[`s2_fuzzy_matching`](module6/s2_fuzzy_matching.ipynb): correction d'erreurs OCR à l'aide de distances d'édition

[`s3_ai_pair_programming`](module6/s3_ai_pair_programming.ipynb): génération de code Python à l'aide d'une intelligence artificielle

[`s4_sparql`](module6/s4_sparql.ipynb): interrogation de la base de connaissances _Wikidata_ à l'aide de requêtes SPARQL
