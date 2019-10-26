from util import to_bit
from gates import *

class RSLatch:

    def __init__(self):
        self.nor_gate_1 = NorGate()
        self.nor_gate_2 = NorGate()

        self.r = None
        self.s = None
        self.q = None
        self.nq = None

    def eval(self):
        self.nor_gate_1.a = self.r
        self.nor_gate_1.b = self.nor_gate_2.q
        self.nor_gate_1.eval()

        self.nor_gate_2.a = self.s
        self.nor_gate_2.b = self.nor_gate_1.q
        self.nor_gate_2.eval()

        self.nor_gate_1.a = self.r
        self.nor_gate_1.b = self.nor_gate_2.q
        self.nor_gate_1.eval()

        self.q = self.nor_gate_1.q
        self.nq = self.nor_gate_2.q

    def __str__(self):
        return "RSQQ\n%s%s%s%s" % (to_bit(self.r), to_bit(self.s), to_bit(self.q), to_bit(self.nq))

class DLatch:

    def __init__(self):
        self.and_gate_1 = AndGate()
        self.and_gate_2 = AndGate()
        self.not_gate = NotGate()
        self.rs_latch = RSLatch()

        self.d = None
        self.e = None
        self.q = None
        self.nq = None

    def eval(self):
        self.not_gate.a = self.d
        self.not_gate.eval()

        self.and_gate_1.a = self.not_gate.q
        self.and_gate_1.b = self.e
        self.and_gate_1.eval()

        self.and_gate_2.a = self.e
        self.and_gate_2.b = self.d
        self.and_gate_2.eval()

        self.rs_latch.r = self.and_gate_1.q
        self.rs_latch.s = self.and_gate_2.q
        self.rs_latch.eval()

        self.q = self.rs_latch.q
        self.nq = self.rs_latch.nq

    def __str__(self):
        return "DEQQ\n%s%s%s%s" % (to_bit(self.d), to_bit(self.e), to_bit(self.q), to_bit(self.nq))
