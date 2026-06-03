from fastapi import APIRouter, HTTPException

router = APIRouter()

# Les devices seront injectés depuis api.py
devices = None

@router.get("/{servoID}/setAngle/{angle}")
def set_servo_angle(servoID: str, angle: int):

    if servoID not in devices.keys():
        raise HTTPException(status_code=404, detail="Unknown device")

    devices[servoID].set_angle(angle)
    return {"device": servoID, "state": devices[servoID].get_angle()}

