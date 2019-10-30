from gates import XorGate, AndGate, OrGate, NotGate

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


