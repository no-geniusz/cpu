from util import to_bit
from gates import *

class SRLatch:

    def __init__(self):
        self.r = None
        self.s = None
        self.q = None
        self.nq = None

        self.__nor_gate_1 = NorGate()
        self.__nor_gate_2 = NorGate()

    def eval(self):
        self.__nor_gate_1.a = self.r
        self.__nor_gate_1.b = self.__nor_gate_2.q
        self.__nor_gate_1.eval()

        self.__nor_gate_2.a = self.s
        self.__nor_gate_2.b = self.__nor_gate_1.q
        self.__nor_gate_2.eval()

        self.__nor_gate_1.a = self.r
        self.__nor_gate_1.b = self.__nor_gate_2.q
        self.__nor_gate_1.eval()

        self.q = self.__nor_gate_1.q
        self.nq = self.__nor_gate_2.q

    def __str__(self):
        return "RSQQ\n%s%s%s%s" % (to_bit(self.r), to_bit(self.s), to_bit(self.q), to_bit(self.nq))

class DLatch:

    def __init__(self):
        self.d = None
        self.e = None
        self.q = None
        self.nq = None

        self.__and_gate_1 = AndGate()
        self.__and_gate_2 = AndGate()
        self.__not_gate = NotGate()
        self.__rs_latch = SRLatch()

    def eval(self):
        self.__not_gate.a = self.d
        self.__not_gate.eval()

        self.__and_gate_1.a = self.__not_gate.q
        self.__and_gate_1.b = self.e
        self.__and_gate_1.eval()

        self.__and_gate_2.a = self.e
        self.__and_gate_2.b = self.d
        self.__and_gate_2.eval()

        self.__rs_latch.r = self.__and_gate_1.q
        self.__rs_latch.s = self.__and_gate_2.q
        self.__rs_latch.eval()

        self.q = self.__rs_latch.q
        self.nq = self.__rs_latch.nq

    def __str__(self):
        return "DEQQ\n%s%s%s%s" % (to_bit(self.d), to_bit(self.e), to_bit(self.q), to_bit(self.nq))

class JKFlipFlop():
    
    def __init__(self):
        self.j = None
        self.k = None
        self.clk = None

        self.q = None
        self.nq = None

        self.__sr_latch = SRLatch()
        self.__and_j = AndGate()
        self.__and_k = AndGate()
        self.__and_jclk = AndGate()
        self.__and_kclk = AndGate()

    def eval(self):
        self.__sr_latch.eval()

        self.__and_j.a = self.j
        self.__and_j.b = self.__sr_latch.nq
        self.__and_j.eval()

        self.__and_jclk.a = self.__and_j.q
        self.__and_jclk.b = self.clk
        self.__and_jclk.eval()

        self.__and_k.a = self.k
        self.__and_k.b = self.__sr_latch.q
        self.__and_k.eval()

        self.__and_kclk.a = self.__and_k.q
        self.__and_kclk.b = self.clk
        self.__and_kclk.eval()

        self.__sr_latch.r = self.__and_kclk.q
        self.__sr_latch.s = self.__and_jclk.q
        self.__sr_latch.eval()

        self.q = self.__sr_latch.q
        self.nq = self.__sr_latch.nq
