from bleak import BleakScanner
from bleak.backends.device import BLEDevice

HUMMY_PREFIX = "IQSZM"


async def discover() -> list[BLEDevice]:
    devices = await BleakScanner.discover()
    return _filter_devices(devices)


def _filter_devices(discovered_devices: list[BLEDevice]) -> list[BLEDevice]:
    return [
        device for device in discovered_devices if device.name.startswith(HUMMY_PREFIX)
    ]
