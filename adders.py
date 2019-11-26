from gates import XorGate, AndGate, OrGate
from util import to_bit, to_bit_arr

class FullAdder:

    def __init__(self):
        self.xor1 = XorGate()
        self.xor2 = XorGate()
        self.and1 = AndGate()
        self.and2 = AndGate()
        self.or_gate = OrGate()

        self.a = None
        self.b = None
        self.cin = None

        self.s = None
        self.cout = None

    def eval(self):
        self.xor1.a = self.a
        self.xor1.b = self.b
        self.xor1.eval()
        
        self.xor2.a = self.xor1.q
        self.xor2.b = self.cin
        self.xor2.eval()

        self.s = self.xor2.q

        self.and1.a = self.xor1.q
        self.and1.b = self.cin
        self.and1.eval()

        self.and2.a = self.a
        self.and2.b = self.b
        self.and2.eval()

        self.or_gate.a = self.and1.q
        self.or_gate.b = self.and2.q
        self.or_gate.eval()

        self.cout = self.or_gate.q

class RCAdder:

    def __init__(self, width):
        self.__width = width

        self.a = [None] * width
        self.b = [None] * width
        self.s = [None] * width
        self.c = None

        self.__adders = [FullAdder() for _ in range(width)]

    def eval(self):
        for k in range(self.__width - 1, -1, -1):
            adder = self.__adders[k]
            
            adder.a = self.a[k]
            adder.b = self.b[k]
            if k == self.__width - 1:
                adder.cin = 0
            else:
                adder.cin = self.__adders[k + 1].cout
            adder.eval()
            self.s[k] = adder.s

        self.c = self.__adders[0].cout

    def __str__(self):
        return 'A ' + to_bit_arr(self.a) + '\nB ' + to_bit_arr(self.b) + '\nC' + to_bit(self.c) + to_bit_arr(self.s)
