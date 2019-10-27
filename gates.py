from util import to_bit

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
        self.nor_gate = NorGate()

        self.a = None
        self.q = None

    def eval(self):
        self.nor_gate.a = self.a
        self.nor_gate.b = self.a
        self.nor_gate.eval()

        self.q = self.nor_gate.q

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

class OrGate:

    def __init__(self):
        self.nor_gate = NorGate()
        self.not_gate = NotGate()

        self.a = None
        self.b = None
        self.q = None

    def eval(self):
        self.nor_gate.a = self.a
        self.nor_gate.b = self.b
        self.nor_gate.eval()

        self.not_gate.a = self.nor_gate.q
        self.not_gate.eval()

        self.q = self.not_gate.q

    def __str__(self):
        return 'ABQ\n' + to_bit(self.a) + to_bit(self.b) + to_bit(self.q)

