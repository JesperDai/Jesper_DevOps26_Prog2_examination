Individuell examensuppgift i programmering 2 – API-klient med Flask och Pytest

# 🌤️ Väderapplikation – Flask--

## Om projektet

Detta projekt är en webbaserad väderapplikation utvecklad med Python, Flask, Pandas. Applikationen hämtar väderdata från ett externt väder-API (Open-meteo) och presenterar informationen med en enkel tabell.

Syftet med projektet är att hämta, bearbeta och visualisera väderdata samt ge användaren möjlighet att välja olika städer och sen får väderinformation om den valda staden för dem kommande 3 dagar.

## Funktioner

- Hämta väderdata från ett externt API.
- Visa väderinformation i webbläsaren.
- Presentera temperatur och nederbörd.
- Filtrera väderdata baserat på en lista med olika städer i Sverige.
- Bearbeta och analysera data med Pandas.
- Hantera API-fel och saknad data.

## Tekniker

Projektet använder följande tekniker:

- **Python** : Programmeringsspråk.
- **Flask** : Webbramverk för att skapa webbapplikationen.
- **Jinja2** : Hantering av HTML-mallar.
- **Bootstrap** : Styling och responsiv design.
- **Pandas** : Bearbetning och analys av väderdata.
- **Requests** : Kommunikation med ett externt API.
- **Pytest** : Testning av applikationens funktioner.

## Installation

### 1. Klona projektet

```bash
git clone https://github.com/JesperDai/Jesper_DevOps26_Prog2_examination.git
```

### 2. Skapa en venv för att begränsa programmet till en separat miljö som inte har kontakt med resten av din dator.

Windows:

```bash
python -m venv venv
```
MacOS och/eller Linux:

```bash
python3 -m venv venv
```

När din venv är skapad kan du aktivera miljön med denna kod:

Windows:

```bash
venv\Scripts\activate
```
MacOS och/eller Linux:

```bash
source .venv/bin/activate
```

### 3. Installera beroenden

```bash
pip install -r requirements.txt
```

### 4. Starta applikationen

```bash
flask run
```

Öppna sedan följande adress i webbläsaren:

```text
http://127.0.0.1:5000
```

## Testning

Projektet använder Pytest för att testa applikationens funktioner.

### Installera verktyg

```bash
pip install -r requirements-dev.txt
```

Kör samtliga tester med:

```bash
pytest --cov
```

```bash
ruff check
```

```bash
ruff format
```

## Vidareutveckling

Möjliga framtida förbättringar:

- Fler möjligheter att filtrera och jämföra väderdata.
- typer av diagram och visualiseringar.

## Författare
Jesper Dai

1. Varför mockar du anropen mot API:et i dina tester, och vad skulle hända om du inte gjorde
det?

svar: testerna kollar att ens kod fungerar som det ska. När ens egna API förlitar sig på en extern API för att göra sina tjänster, kan ens API sluta fungera när den externa APi ligger nere eller inte fungerar. Men om dina tester också förlitar sig på att den externa API måste fungera för att kolla vems eller vart felet uppstod. Ens egna kod eller den externa API blir det svårt att avgöra. Därför skrivs mock tester när det gäller anrop mot ett externt API, eftersom mock testerna inte förlitar sig på en fungerande uppkoppling till internet eller ett fungerande externt API. Utan mock tester kollar enbart om din kod fungerar mot dem testerna som du anser är nödvändiga till att din API ska fungera.

2. Vad gör timeout och raise_for_status(), och varför behövs de?

svar: Timeout sätter en tidsgräns på hur länge din applikation väntar på en svar från en server. Om servern inte svarar inom den angivna tiden, avbryts väntan automatiskt och applikationen ger ut en timeout error. Denna gräns sätts för att inte låta användaren fastna allt för länge utan att dem kan göra något.

svar: raise_for_status() kontrollerar HTTP-statuskod från servern du är kopplad till. Om servern returnerar ett HTTP-fel som 404 eller 500 så skickas en HTTP-error. Dessa HTTP-error kan fångas upp för helhantering och för att hjälpa användarna förstå vart felet uppstod.

3. Hur fungerar mallarv i Jinja2? Förklara med exempel från dina egna mallar.

svar: mallarv i Jinja2 är metoden där man skapar en grund-mall eller en kallad bas-mall som utgör hur strukturen för din webbsida ska se ut och med denna bas-mall så ärver alla andra sidor som du skapar den exakta strukturen som basen. Vilket 1 du behöver inte skriva om html strukturen för alla ens olika sidor om och om igen, Detta följer DRY-principen (Don't Repeat Yourself) och 2 det hjälper så att alla webbsidor följer en viss röd tråd och ser ut att webbsidorna hör ihop med varandra. Såklart så kan man lägga till eller ersätta specifikt innehåll som skiljer sidor åt men att den gör så med samma struktur i åtanket.
Min kod till exempel använder bas-mall-html för att sätta strukturen för mina sidor och sen med mina andra html filer som utgör andra webbsidor så använder jag {% extends "bas-mall.html" %} för att ärva ner samma struktur till mina andra webbsidor som startsida.html, prognossida.html osv.

4. Vad är en fixture, och vilken använder du?

svar: En fixture är en typ av miljö som man skapar för pytester där man vill förbereda något som ens tester ska använda när den ska köras. Det kan vara testdata eller funktioner som körs innan varje test ska utföras och tanken är att du ska slippa skriva samma förberedande kod i varje test fall. @pytest.fixture markerar vilken funktion eller testdata som ska innehålla i miljön och kan då anropas automatiskt med pytest när ett test använder den. Och i mitt fall så skapade jag en klient som hjälpte mig testa att anropa olika sidor till min flask server utan att faktiskt öppna flask servern varje gång jag ville köra mina tester.

## källa

API:et hämtar väderdata för Stockholm från Open-Meteo Historical weather (https://open-meteo.com/en/docs/historical-weather-api) 

API data är licenserad under: CC BY 4.0