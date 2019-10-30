from gates import XorGate, AndGate, OrGate, NotGate
from registers import REG_WIDTH
from util import to_bit

class FullSubtractor:

    x = None
    y = None
    bin = None

    d = None
    bout = None

    xor1 = XorGate()
    xor2 = XorGate()
    and1 = AndGate()
    and2 = AndGate()
    or1 = OrGate()
    not2 = NotGate()
    not3 = NotGate()

    def eval(self):
        self.xor1.a = self.x
        self.xor1.b = self.y
        self.xor1.eval()

        self.xor2.a = self.xor1.q
        self.xor2.b = self.bin
        self.xor2.eval()

        self.not2.a = self.x
        self.not2.eval()

        self.and1.a = self.not2.q
        self.and1.b = self.y
        self.and1.eval()

        self.not3.a = self.xor1.q
        self.not3.eval()

        self.and2.a = self.bin
        self.and2.b = self.not3.q
        self.and2.eval()

        self.or1.a = self.and1.q
        self.or1.b = self.and2.q
        self.or1.eval()

        self.d = self.xor2.q
        self.bout = self.or1.q

class RCSubtractor:

    x = [None for k in range(REG_WIDTH)]
    y = [None for k in range(REG_WIDTH)]
    d = [None for k in range(REG_WIDTH)]
    b = None

    _subtractors = [FullSubtractor() for k in range(REG_WIDTH)]

    def eval(self):
        self._subtractors[0].x = self.x[0]
        self._subtractors[0].y = self.y[0]
        self._subtractors[0].bin = 0
        self._subtractors[0].eval()
        self.d[0] = self._subtractors[0].d

        for k in range(1, REG_WIDTH):
            self._subtractors[k].x = self.x[k]
            self._subtractors[k].y = self.y[k]
            self._subtractors[k].bin = self._subtractors[k - 1].bout
            self._subtractors[k].eval()
            self.d[k] = self._subtractors[k].d

        self.b = self._subtractors[REG_WIDTH - 1].bout

    def __str__(self):
        return 'BXXXX YYYY DDDD\n%s%s%s%s%s %s%s%s%s %s%s%s%s' % (to_bit(self.b), to_bit(self.x[3]), to_bit(self.x[2]), to_bit(self.x[1]), to_bit(self.x[0]),
            to_bit(self.y[3]), to_bit(self.y[2]), to_bit(self.y[1]), to_bit(self.y[0]), 
            to_bit(self.d[3]), to_bit(self.d[2]), to_bit(self.d[1]), to_bit(self.d[0]))

