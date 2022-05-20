# LotteryScraping

This scrapper is useful to read the results from [http://www.loteriasdominicanas.com][web]

[web]: http://www.loteriasdominicanas.com


### How to run
```sh
$ pip install beautifulsoup4
```

```sh
$ python scraper.py
```

The response should be:
```sh
$ python scraper.py
{
  "Americanas": {
    "games": {
      "New York Noche": ["56", "55", "71"],
      "Florida Noche": ["96", "13", "70"],
      "Cash 4 Life": ["41", "47", "51", "58", "60", "03"],
      "New York Tarde": ["69", "36", "71"],
      "Florida D\u00eda": ["76", "08", "19"]
    }
  },
  "Loteria Nacional": {
    "games": {
      "Loter\u00eda Nacional": ["36", "54", "44"],
      "Gana M\u00e1s": ["32", "47", "19"],
      "Juega + Pega +": ["14", "13", "12", "08", "16"]
    }
  },
  "Leidsa": {
    "games": {
      "Super Pal\u00e9": ["11", "36"],
      "Quiniela Leidsa": ["11", "34", "88"],
      "Super Kino TV": [
        "02",
        "04",
        "11",
        "13",
        "19",
        "23",
        "33",
        "34",
        "44",
        "46",
        "47",
        "49",
        "50",
        "56",
        "67",
        "71",
        "72",
        "74",
        "78",
        "79"
      ],
      "Loto Pool": ["03", "07", "13", "15", "20"],
      "Pega 3 M\u00e1s": ["08", "00", "18"]
    }
  },
  "Anguila": {
    "games": {
      "Anguila Noche": ["34", "77", "63"],
      "Anguila Tarde": ["71", "01", "83"],
      "Anguila Medio D\u00eda": ["66", "73", "50"],
      "Anguila Ma\u00f1ana": ["48", "81", "57"]
    }
  },
  "La Primera": {
    "games": {
      "Primera Noche": ["94", "69", "43"],
      "La Primera D\u00eda": ["55", "32", "09"]
    }
  },
  "Loteka": {
    "games": {
      "El Extra": ["27"],
      "MegaLotto": ["07", "13", "17", "19", "31", "49"],
      "Quiniela Loteka": ["63", "87", "77"],
      "MC Repartidera": ["39"],
      "Mega Chances": ["99", "64", "09", "66", "17"],
      "Toca 3": ["2", "5", "7"]
    }
  },
  "King Lottery": {
    "games": {
      "King Lottery 7:30": ["56", "87", "69"],
      "King Lottery 12:30": ["83", "72", "37"]
    }
  },
  "Nueva York": {
    "games": { "Take 5 Midday": ["06", "11", "23", "25", "35"] }
  },
  "LoteDom": {
    "games": {
      "Agarra 4": ["13", "77", "18", "17"],
      "Super Pal\u00e9": ["13", "17"],
      "El Quemaito Mayor": ["17"],
      "Quiniela": ["13", "77", "18"]
    }
  },
  "Loteria Real": {
    "games": {
      "Quiniela Real": ["22", "72", "82"],
      "Nueva Yol Real": ["42", "08", "56", "Verde"],
      "Loto Pool": ["75", "59", "44", "05"],
      "Pega 4 Real": ["0", "3", "3", "1"],
      "Tu Fecha Real": ["29"]
    }
  },
  "La Suerte": { "games": { "Quiniela LASD": ["45", "61", "38"] } }
}

```