from bus import Bus
from registers import WideRegister

def test_bus_apply():
    bus = Bus(4)

    bus.line = [0, 1, 0, 1]
    bus.apply([1, None, None, 0])

    assert bus.line == [1, 1, 0, 0]
