from _pytest.fixtures import fixture
from bleak import BLEDevice


@fixture()
def non_hummy_device() -> BLEDevice:
    return BLEDevice(address="AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE", name="NOTHUMMY")


@fixture()
def hummy_device() -> BLEDevice:
    return BLEDevice(address="AAAAAAAA-BBBB-CCCC-DDDD-EEEEEEEEEEEE", name="IQSZM020A")
