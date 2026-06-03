from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes import ledRouteur
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


devices = generateDeviceFromConfig(config)

print(devices)


# -------------------------
# FASTAPI
# -------------------------

devices = generateDeviceFromConfig(config)

# On donne l'accès aux devices au module
ledRouteur.devices = devices

@app.get("/health")
def health():
    return {"status": "ok"}

@app.get("/conf")
def get_config():
    return config


ledRouteur.devices = devices

app.include_router(
    ledRouteur.router,
    prefix="/led",
    tags=["LED"]
)

"""
@app.get("/led/{ledID}/toggle")
def get_gpio_state(ledID: str):

    if ledID not in devices.keys():
        raise HTTPException(status_code=404, detail="Unknown device")

    devices[ledID].toggle()
    return {"device": ledID, "state": devices[ledID].get_state()}

@app.on_event("shutdown")
def cleanup_gpio():
    cleanupDevices(devices)

"""
if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=False)
