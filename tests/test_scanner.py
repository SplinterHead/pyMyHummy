from unittest.mock import patch

import pytest

from pymyhummy.scanner import discover


@pytest.mark.asyncio
@patch("bleak.BleakScanner.discover")
async def test_scanner_returns_hummy_devices(mock_discover, hummy_device):
    mock_discover.return_value = [hummy_device]
    devices = await discover()
    assert len(devices) == 1


@pytest.mark.asyncio
@patch("bleak.BleakScanner.discover")
async def test_scanner_does_not_return_non_hummy_devices(
    mock_discover, non_hummy_device
):
    mock_discover.return_value = [non_hummy_device]
    devices = await discover()
    assert len(devices) == 0


@pytest.mark.asyncio
@patch("bleak.BleakScanner.discover")
async def test_scanner_only_returns_hummy_devices(
    mock_discover, hummy_device, non_hummy_device
):
    mock_discover.return_value = [hummy_device, non_hummy_device]
    devices = await discover()
    assert len(devices) == 1
