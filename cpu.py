from bus import Bus
from registers import WideRegister
from display import NumDisplay
from memory import Memory
from alu import Alu
from three_state import WideThreeState

class CPU:

    REG_WIDTH = 8

    def __init__(self):
        self.clk = None

        self.bus = Bus(CPU.REG_WIDTH)
        self.memory_register = WideRegister(4)
        self.memory = Memory()
        self.register_a = WideRegister(CPU.REG_WIDTH)
        self.register_a_three_state = WideThreeState(CPU.REG_WIDTH)
        self.register_b = WideRegister(CPU.REG_WIDTH)
        self.register_b_three_state = WideThreeState(CPU.REG_WIDTH)
        self.alu = Alu(CPU.REG_WIDTH)
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
        self.register_a.enable = True
        self.register_a.eval()
        self.register_a_three_state.a = self.register_a.q
        self.register_a_three_state.eval()
        self.bus.apply(self.register_a_three_state.c)

        self.register_b.clk = self.clk
        self.register_b.d = self.bus.line
        self.register_b.enable = True
        self.register_b.eval()
        self.register_b_three_state.a = self.register_b.q
        self.register_b_three_state.eval()
        self.bus.apply(self.register_b_three_state.c)

        self.alu.a = self.register_a.q
        self.alu.b = self.register_b.q
        self.alu.eval()
        self.bus.apply(self.alu.x)

        self.out_register.clk = self.clk
        self.out_register.d = self.bus.line
        self.out_register.eval()

        self.display.a = self.out_register.d
        self.display.eval()
