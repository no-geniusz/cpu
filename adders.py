from gates import XorGate, AndGate, OrGate
from registers import REG_WIDTH
from util import to_bit

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

    def __init__(self):
        self.adders = [FullAdder() for k in range(REG_WIDTH)]
        self.a = [None for k in range(REG_WIDTH)]
        self.b = [None for k in range(REG_WIDTH)]
        self.s = [None for k in range(REG_WIDTH)]
        self.c = None

    def eval(self):
        self.adders[0].a = self.a[0]
        self.adders[0].b = self.b[0]
        self.adders[0].cin = 0
        self.adders[0].eval()
        self.s[0] = self.adders[0].s

        for k in range(1, REG_WIDTH):
            self.adders[k].a = self.a[k]
            self.adders[k].b = self.b[k]
            self.adders[k].cin = self.adders[k - 1].cout
            self.adders[k].eval()
            self.s[k] = self.adders[k].s

        self.c = self.adders[REG_WIDTH - 1].cout

    def __str__(self):
        return 'AAAA BBBB CSSSS\n%s%s%s%s %s%s%s%s %s%s%s%s%s' % (to_bit(self.a[3]), to_bit(self.a[2]), to_bit(self.a[1]), to_bit(self.a[0]),
            to_bit(self.b[3]), to_bit(self.b[2]), to_bit(self.b[1]), to_bit(self.b[0]), to_bit(self.c), 
            to_bit(self.s[3]), to_bit(self.s[2]), to_bit(self.s[1]), to_bit(self.s[0]))
