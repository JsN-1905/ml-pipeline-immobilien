from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
import joblib
import pandas as pd

modell = joblib.load('modell.pkl')
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

class Immobilie(BaseModel):
    MedInc: float
    HouseAge: float
    AveRooms: float
    AveBedrms: float
    Population: float
    AveOccup: float
    Latitude: float
    Longitude: float

@app.get("/")
def startseite():
    return {"nachricht": "Immobilienpreis API läuft! ✅"}

@app.post("/vorhersage")
def vorhersage(immobilie: Immobilie):
    daten = pd.DataFrame([immobilie.model_dump()])
    preis = modell.predict(daten)[0]
    return {"preis_100k": round(float(preis), 2),
            "preis_dollar": round(float(preis) * 100000, 2)}