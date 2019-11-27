from util import to_bit

class TwoInGate:

    def __init__(self):
        self.a = None
        self.b = None
        self.q = None

    def __str__(self):
        return 'ABQ\n' + to_bit(self.a) + to_bit(self.b) + to_bit(self.q)

class NorGate:

    def __init__(self):
        self.a = None
        self.b = None
        self.q = None

    def eval(self):
        self.q = not (self.a or self.b)

    def __str__(self):
        return "NorGate{'a': %s, 'b': %s, 'q': %s}" % (to_bit(self.a), to_bit(self.b), to_bit(self.q))

class NotGate:

    def __init__(self):
        self.a = None
        self.q = None

        self.__nor_gate = NorGate()

    def eval(self):
        self.__nor_gate.a = self.a
        self.__nor_gate.b = self.a
        self.__nor_gate.eval()

        self.q = self.__nor_gate.q

    def __str__(self):
        return "NorGate{'a': %s, 'q': %s}" % (to_bit(self.a), to_bit(self.q))

class AndGate:

    def __init__(self):
        self.not_gate_1 = NotGate()
        self.not_gate_2 = NotGate()
        self.nor_gate = NorGate()

        self.a = None
        self.b = None
        self.q = None

    def eval(self):
        self.not_gate_1.a = self.a
        self.not_gate_1.eval()

        self.not_gate_2.a = self.b
        self.not_gate_2.eval()

        self.nor_gate.a = self.not_gate_1.q
        self.nor_gate.b = self.not_gate_2.q
        self.nor_gate.eval()

        self.q = self.nor_gate.q

    def __str__(self):
        return "AndGate{'a': %s, 'b': %s, 'q': %s}" % (to_bit(self.a), to_bit(self.b), to_bit(self.q))

class NandGate:

    def __init__(self):
        self.and_gate = AndGate()
        self.not_gate = NotGate()

        self.a = None
        self.b = None
        self.q = None

    def eval(self):
        self.and_gate.a = self.a
        self.and_gate.b = self.b
        self.and_gate.eval()

        self.not_gate.a = self.and_gate.q
        self.not_gate.eval()

        self.q = self.not_gate.q

    def __str__(self):
        return "NandGate{'a': %s, 'b': %s, 'q': %s}" % (to_bit(self.a), to_bit(self.b), to_bit(self.q))

class OrGate(TwoInGate):

    def __init__(self):
        super(OrGate, self).__init__()
        self.nor_gate = NorGate()
        self.not_gate = NotGate()

    def eval(self):
        self.nor_gate.a = self.a
        self.nor_gate.b = self.b
        self.nor_gate.eval()

        self.not_gate.a = self.nor_gate.q
        self.not_gate.eval()

        self.q = self.not_gate.q

class XorGate(TwoInGate):

    def __init__(self):
        super(XorGate, self).__init__()
        self.nand_gate = NandGate()
        self.or_gate = OrGate()
        self.and_gate = AndGate()

    def eval(self):
        self.nand_gate.a = self.a
        self.nand_gate.b = self.b
        self.nand_gate.eval()

        self.or_gate.a = self.a
        self.or_gate.b = self.b
        self.or_gate.eval()

        self.and_gate.a = self.nand_gate.q
        self.and_gate.b = self.or_gate.q
        self.and_gate.eval()

        self.q = self.and_gate.q

class MultiInAndGate:

    def __init__(self, width):
        self.__width = width

        self.d = [None] * width
        self.q = None
        self.__gates = [AndGate() for _ in range(width - 1)]

    def eval(self):
        self.__gates[0].a = self.d[0]
        self.__gates[0].b = self.d[1]
        self.__gates[0].eval()

        for k in range(1, self.__width - 1):
            self.__gates[k].a = self.__gates[k - 1].q
            self.__gates[k].b = self.d[k + 1]
            self.__gates[k].eval()

        self.q = self.__gates[self.__width - 2].q
