from fastapi import APIRouter, HTTPException

router = APIRouter()

# Les devices seront injectés depuis api.py
devices = None

@router.get("/{ledID}/toggle")
def toggle_led(ledID: str):

    if ledID not in devices.keys():
        raise HTTPException(status_code=404, detail="Unknown device")

    devices[ledID].toggle()
    return {"device": ledID, "state": devices[ledID].get_state()}

@router.get("/{ledID}/on")
def set_led_on(ledID: str):

    if ledID not in devices.keys():
        raise HTTPException(status_code=404, detail="Unknown device")

    devices[ledID].on()
    return {"device": ledID, "state": devices[ledID].get_state()}

@router.get("/{ledID}/off")
def set_led_off(ledID: str):

    if ledID not in devices.keys():
        raise HTTPException(status_code=404, detail="Unknown device")

    devices[ledID].off()
    return {"device": ledID, "state": devices[ledID].get_state()}