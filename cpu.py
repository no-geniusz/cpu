from bus import Bus
from registers import WideRegister
from display import NumDisplay

class CPU:

    REG_WIDTH = 4

    def __init__(self):
        self.bus = Bus(CPU.REG_WIDTH)
        self.out_register = WideRegister(CPU.REG_WIDTH)
        self.bus.add(self.out_register)
        self.display = NumDisplay(CPU.REG_WIDTH)

    def eval(self):
        self.bus.line = [1, 0, 0, 1, 1, 0, 0, 1]
        self.out_register.load = 1
        self.out_register.clk = 1
        self.bus.eval()

        self.display.a = self.out_register.d
        self.display.eval()

cpu = CPU()
cpu.eval()

