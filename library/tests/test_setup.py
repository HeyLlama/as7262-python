# noqa D100
import sys
import mock
from tools import SMBusFakeAS7262


def test_fw_info():
    """Test against fake device information stored in hardware mock."""
    smbus = mock.Mock()
    smbus.SMBus = SMBusFakeAS7262
    sys.modules['smbus'] = smbus
    import as7262

    hw_type, hw_version, fw_version = as7262.get_version()

    assert hw_version == 0x77
    assert hw_type == 0x88
    assert fw_version == '15.63.62'
