from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import ledRouteur, servoRouteur
import uvicorn
import yaml

from util import generateDeviceFromConfig, cleanupDevices
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BOARD)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origin_regex=r"http://localhost:\d+",
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

#Load configuration
with open("conf.yml", "r") as file:
    # Charger le contenu du fichier en tant que dictionnaire Python
    config = yaml.safe_load(file)

# -------------------------
# FASTAPI
# -------------------------


devices = generateDeviceFromConfig(config)

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/conf")
def get_config():
    return config


ledRouteur.devices = devices
servoRouteur.devices = devices

app.include_router(
    ledRouteur.router,
    prefix="/led",
    tags=["LED"]
)

app.include_router(
    servoRouteur.router,
    prefix="/servo",
    tags=["SERVO"]
)

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=False)
