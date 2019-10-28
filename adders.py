from gates import XorGate, AndGate, OrGate

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

