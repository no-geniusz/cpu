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
