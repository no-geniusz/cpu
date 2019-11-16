from bus import Bus
from registers import WideRegister

def test_bus_add():
    bus = Bus(4)
    reg = WideRegister(4)
    reg.clk = 1

    bus.add(reg)

    bus.line = [0, 1, 0, 1]
    reg.enable = 0
    reg.load = 1
    bus.eval()

    reg.load = 0
    reg.enable = 1
    bus.line = [0, 0, 0, 0]
    bus.eval()

    assert bus.line == [0, 1, 0, 1]
