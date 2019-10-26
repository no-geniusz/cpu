from gates import NorGate

class RSLatch:

    def __init__(self):
        self.nor_gate_1 = NorGate()
        self.nor_gate_2 = NorGate()
        self.r = False
        self.s = False
        self.q = '?'
        self.nq = '?'

    def eval(self):
        self.nor_gate_1.a = self.r
        self.nor_gate_1.b = self.nor_gate_2.q
        self.nor_gate_1.eval()
        self.q = self.nor_gate_1.q

        self.nor_gate_2.a = self.s
        self.nor_gate_2.b = self.nor_gate_1.q
        self.nor_gate_2.eval()
        self.nq = self.nor_gate_2.q

    def __str__(self):
        return "RSLatch{'r': %s, 's': %s, 'q': %s, 'nq': %s}" % (self.r, self.s, self.q, self.nq)

