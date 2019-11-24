from latches import DLatch
from util import to_bit
from gates import NotGate, AndGate, OrGate
from three_state import ThreeState

class ShiftRegister:

    def __init__(self, width):
        self.__width = width
        self.data = []
        self.latches = []

        for i in range(self.__width):
            self.data.insert(0, None)
            self.latches.insert(0, DLatch())

        self.e = None
        self.d = None

    def eval(self):
        for i in range(self.__width - 1):
            self.latches[i].d = self.latches[i + 1].q
            self.latches[i].e = self.e
            self.latches[i].eval()
            self.data[i] = self.latches[i].q

        i = self.__width - 1
        self.latches[i].d = self.d
        self.latches[i].e = self.e
        self.latches[i].eval()
        self.data[i] = self.latches[i].q

    def __str__(self):
        s = 'E%s, D%s\n' % (to_bit(self.e), to_bit(self.d))
        
        for i in range(self.__width):
            s = s + 'D' + str(self.__width - i - 1) + ' '
        
        s = s + '\n'
        
        for i in range(self.__width):
            s = s + ' ' + to_bit(self.data[self.__width - i - 1]) + ' '

        return s

class WideRegister:

    def __init__(self, width):
        self.__width = width
        self.load = None
        self.clk = None
        self.d = [None for _ in range(width)]
        self.q = [None for _ in range(width)]
        self.enable = None
        self.__regs = [Register() for _ in range(width)]

    def eval(self):
        for i in range(self.__width):
            reg = self.__regs[i]
            reg.load = self.load
            reg.clk = self.clk
            reg.d = self.d[i]
            reg.enable = self.enable
            reg.eval()

            self.q[i] = reg.q

    def __str__(self):
        s = 'load=%s, clk=%s, enable=%s\n' % (to_bit(self.load), to_bit(self.clk), to_bit(self.enable))
        s += 'Q'
        for i in range(self.__width, 0, -1):
            s = s + str(i)
        s += '\n '
        for i in range(self.__width, 0, -1):
            s = s + to_bit(self.q[i - 1])

        return s

class Register:

    def __init__(self):
        self.load = None
        self.clk = None
        self.d = None
        self.q = None
        self.enable = None

        self.__not_gate = NotGate()
        self.__and_gate1 = AndGate()
        self.__and_gate2 = AndGate()
        self.__or_gate = OrGate()
        self.__d_latch = DLatch()
        self.__three_state = ThreeState()

    def eval(self):
        self.__not_gate.a = self.load
        self.__not_gate.eval()
        
        self.__and_gate1.a = self.__d_latch.q
        self.__and_gate1.b = self.__not_gate.q
        self.__and_gate1.eval()

        self.__and_gate2.a = self.load
        self.__and_gate2.b = self.d
        self.__and_gate2.eval()
        
        self.__or_gate.a = self.__and_gate1.q
        self.__or_gate.b = self.__and_gate2.q
        self.__or_gate.eval()

        self.__d_latch.d = self.__or_gate.q
        self.__d_latch.e = self.clk
        self.__d_latch.eval()

        self.__three_state.a = self.__d_latch.q
        self.__three_state.b = self.enable
        self.__three_state.eval()

        self.q = self.__three_state.c
