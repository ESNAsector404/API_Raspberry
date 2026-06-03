# API_Raspberry



# Installation

Initialisation du venv python

`python3 -m venv .venv`

puis activation

`source .venv/bin/activate`

Installation des dependances

`pip install -r requirements.txt`

Lancement de l'API : 

`python api.py` ou `uvicorn api:app --host 0.0.0.0 --port 8000`

## Création d'un service

Afin que l'API tourne en boucle sur le raspberry, nous allons créer un service systemd.

Pour cela :

**1. Création du service : ** 

nous allons créer un fichier de conf :

`sudo nano /etc/systemd/system/raspi-api.service`

avec ce contenu :

```bash
[Unit]
Description=API FastAPI Raspberry
After=network.target

[Service]
User=raspi
WorkingDirectory=/home/raspi/API_Raspberry/
ExecStart=/home/raspi/API_Raspberry/.venv/bin/uvicorn api:app --host 0.0.0.0 --port 8000
Restart=always

[Install]
WantedBy=multi-user.target
```

on relance le daemon : `sudo systemctl daemon-reload`

et on lance le service : `sudo systemctl start raspi-api.service`

check : `sudo systemctl status raspi-api.service`