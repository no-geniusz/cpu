from bus import Bus
from registers import WideRegister
from display import NumDisplay
from memory import Memory

class CPU:

    REG_WIDTH = 8

    def __init__(self):
        self.clk = None

        self.bus = Bus(CPU.REG_WIDTH)
        self.memory_register = WideRegister(4)
        self.memory = Memory()
        self.register_a = WideRegister(CPU.REG_WIDTH)
        self.register_b = WideRegister(CPU.REG_WIDTH)
        self.out_register = WideRegister(CPU.REG_WIDTH)
        self.display = NumDisplay(CPU.REG_WIDTH)

    def eval(self):
        self.memory_register.clk = self.clk
        self.memory_register.d = self.bus.line[4:]
        self.memory_register.eval()

        self.memory.clk = self.clk
        self.memory.a = self.memory_register.q
        self.memory.d = self.bus.line
        self.memory.eval()
        self.bus.apply(self.memory.o)

        self.register_a.clk = self.clk
        self.register_a.d = self.bus.line
        self.register_a.eval()
        self.bus.apply(self.register_a.q)

        self.register_b.clk = self.clk
        self.register_b.d = self.bus.line
        self.register_b.eval()
        self.bus.apply(self.register_b.q)

        self.out_register.clk = self.clk
        self.out_register.d = self.bus.line
        self.out_register.eval()

        self.display.a = self.out_register.d
        self.display.eval()

cpu = CPU()
cpu.clk = 1

cpu.bus.line = [0, 0, 0, 0, 1, 0, 0, 1]
cpu.memory.write = 0
cpu.memory.enable = 0
cpu.memory_register.load = 1
cpu.memory_register.enable = 0
cpu.eval()

cpu.bus.line = [1, 0, 0, 0, 1, 0, 0, 0]
cpu.memory.write = 1
cpu.memory_register.load = 0
cpu.memory_register.enable = 1
cpu.eval()

