from components.Led import Led

def generateDeviceFromConfig(config):
    devices = {}
    for deviceName in config.keys():
        match config[deviceName]['type']:
            case 'LED':
                 devices[deviceName] = Led(config[deviceName]['pin'])
    return devices

def cleanupDevices(devices):
    for device in devices.values():
        device.cleanup()