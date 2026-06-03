from components.Led import Led
from components.Servo import Servo

def generateDeviceFromConfig(config):
    devices = {}
    for deviceName in config.keys():
        match config[deviceName]['type']:
            case 'LED':
                 devices[deviceName] = Led(config[deviceName]['pin'])
            case 'SERVO':
                 devices[deviceName] = Servo(config[deviceName]['pin'])
    return devices

def cleanupDevices(devices):
    for device in devices.values():
        device.cleanup()