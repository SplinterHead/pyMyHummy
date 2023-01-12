from bleak import BleakScanner
from bleak.backends.device import BLEDevice

HUMMY_PREFIX = "IQSZM"


async def discover() -> list[BLEDevice]:
    devices = await BleakScanner.discover()
    return [device for device in devices if device.name.startswith(HUMMY_PREFIX)]
