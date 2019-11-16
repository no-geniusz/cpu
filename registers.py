from latches import DLatch
from util import to_bit
from gates import NotGate, AndGate, OrGate

REG_WIDTH = 4

class ShiftRegister:

    def __init__(self):
        self.data = []
        self.latches = []

        for i in range(REG_WIDTH):
            self.data.insert(0, None)
            self.latches.insert(0, DLatch())

        self.e = None
        self.d = None

    def eval(self):
        for i in range(REG_WIDTH - 1):
            self.latches[i].d = self.latches[i + 1].q
            self.latches[i].e = self.e
            self.latches[i].eval()
            self.data[i] = self.latches[i].q

        i = REG_WIDTH - 1
        self.latches[i].d = self.d
        self.latches[i].e = self.e
        self.latches[i].eval()
        self.data[i] = self.latches[i].q

    def __str__(self):
        s = 'E%s, D%s\n' % (to_bit(self.e), to_bit(self.d))
        
        for i in range(REG_WIDTH):
            s = s + 'D' + str(REG_WIDTH - i - 1) + ' '
        
        s = s + '\n'
        
        for i in range(REG_WIDTH):
            s = s + ' ' + to_bit(self.data[REG_WIDTH - i - 1]) + ' '

        return s

class FourBitRegister:

    def __init__(self):
        self.d = [None for k in range(REG_WIDTH)]
        self.q = [None for k in range(REG_WIDTH)]
        self.latches = [DLatch() for _ in range(REG_WIDTH)]
        self.e  = None

    def eval(self):
        for i in range(REG_WIDTH):
            self.latches[i].d = self.d[i]
            self.latches[i].e = self.e
            print('before: ' + self.latches[i].__str__())
            self.latches[i].eval()
            print('after: ' + self.latches[i].__str__())
            self.q[i] = self.latches[i].q

    def __str__(self):
        s = 'E%s\n' % (to_bit(self.e))
        s += 'D' * REG_WIDTH + '\n'
        for i in range(REG_WIDTH, 0, -1):
            s = s + to_bit(self.d[i - 1])
        s = s + '\n'
        s += 'Q' * REG_WIDTH + '\n'
        for i in range(REG_WIDTH, 0, -1):
            s = s + to_bit(self.q[i - 1])

        return s

class Register:

    def __init__(self):
        self.load = None
        self.clk = None
        self.d = None
        self.q = None

        self.__not_gate = NotGate()
        self.__and_gate1 = AndGate()
        self.__and_gate2 = AndGate()
        self.__or_gate = OrGate()
        self.__d_latch = DLatch()

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

        self.q = self.__d_latch.q
