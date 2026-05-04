from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import pandas as pd

# Modell laden
modell = joblib.load('modell.pkl')

# API erstellen
app = FastAPI()

# Eingabeformat definieren
class Immobilie(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

# Route erstellen
@app.get("/")
def startseite():
    return {"nachricht": "Immobilienpreis API läuft! ✅"}

@app.post("/vorhersage")
def vorhersage(immobilie: Immobilie):
    daten = pd.DataFrame([immobilie.model_dump()])
    preis = modell.predict(daten)[0]
    return {"preis_100k": round(float(preis), 2),
            "preis_dollar": round(float(preis) * 100000, 2)}