# 🏠 Immobilienpreis-Vorhersage | ML Pipeline

Eine End-to-End Machine Learning Pipeline zur Vorhersage von Immobilienpreisen – 
von der Datenanalyse bis zur produktionsreifen REST API.
> ⚠️ **Hinweis:** Dieses Modell wurde auf dem California Housing Dataset 
> trainiert und dient als Demonstration einer End-to-End ML Pipeline.

## 🎯 Ergebnis

| Metrik | Basis-Modell | Optimiertes Modell |
|--------|-------------|-------------------|
| R² Score | 0.83 | 0.85 |
| MAE | 31.000$ | 29.000$ |

## 🛠️ Technologien

- **Python** – Programmiersprache
- **Pandas** – Datenanalyse & Bereinigung
- **XGBoost** – Machine Learning Modell
- **Scikit-learn** – Modellauswertung & Tuning
- **FastAPI** – REST API
- **Uvicorn** – Web Server
- **Jupyter Notebook** – Explorative Datenanalyse

## 🏗️ Projektstruktur
ml-pipeline-immobilien/
│
├── analyse.ipynb      # Datenanalyse, Training & Tuning
├── api.py             # FastAPI REST API
├── requirements.txt   # Abhängigkeiten
└── README.md

## 🚀 Live testen

Die API läuft live auf Render.com – kein Setup nötig.
(Bald kommt eine interaktive Karte und benutzeroberfläche hinzu.)

⚠️ Hinweis: Render.com fährt inaktive Services nach einigen Minuten herunter. Beim ersten Aufruf kann es 20–30 Sekunden dauern bis die API antwortet – einfach kurz warten.


Schritt-für-Schritt: Immobilienpreis vorhersagen
Schritt 1 – API-Dokumentation öffnen
Gehe auf: https://ml-pipeline-immobilien.onrender.com/docs
Man sieht eine interaktive Oberfläche mit allen verfügbaren Endpunkten.

Schritt 2 – Endpunkt öffnen
Auf POST /vorhersage und dann auf den Button „Try it out" (oben rechts im Abschnitt) klicken.

Schritt 3 – Beispieldaten einfügen
Den Inhalt im Textfeld mit folgendem Beispiel ersetzen (ein Haus in San Francisco):
json{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.984127,
  "AveBedrms": 1.023810,
  "Population": 322.0,
  "AveOccup": 2.555556,
  "Latitude": 37.88,
  "Longitude": -122.23
}

Schritt 4 – Ausführen & Ergebnis lesen
Klicke auf „Execute". Die API antwortet mit dem vorhergesagten Preis:


Lokale Installation (optional)
<details>
<summary>Für Entwickler – lokal ausführen</summary>
bashgit clone https://github.com/JsN-1905/ml-pipeline-immobilien.git
cd ml-pipeline-immobilien
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
# analyse.ipynb ausführen, dann:
uvicorn api:app --reload
</details>


## 📡 API Dokumentation

### Endpunkte

| Methode | Route | Beschreibung |
|---------|-------|-------------|
| GET | `/` | Status der API |
| POST | `/vorhersage` | Immobilienpreis vorhersagen |

### Beispiel Anfrage

```json
POST /vorhersage
{
  "MedInc": 8.3252,
  "HouseAge": 41.0,
  "AveRooms": 6.984127,
  "AveBedrms": 1.023810,
  "Population": 322.0,
  "AveOccup": 2.555556,
  "Latitude": 37.88,
  "Longitude": -122.23
}
```

### Beispiel Antwort

```json
{
  "preis_100k": 4.04,
  "preis_dollar": 403997.37
}
```

## 📊 Methodik

1. **Explorative Datenanalyse** – Korrelationsmatrix, Verteilungen, Ausreißer
2. **Feature Engineering** – Auswahl relevanter Features
3. **Modelltraining** – XGBoost Regressor
4. **Hyperparameter Tuning** – GridSearchCV mit 270 Kombinationen
5. **Deployment** – FastAPI REST API

## 📈 Vorher vs. Nachher Tuning

Das GridSearchCV Tuning mit 54 Parameterkombinationen × 5-facher 
Cross Validation verbesserte den R² Score von 0.83 auf 0.85 und 
reduzierte den durchschnittlichen Fehler um 2.000$.
