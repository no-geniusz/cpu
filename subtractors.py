from gates import XorGate, AndGate, OrGate, NotGate
from util import to_bit, to_bit_arr

class FullSubtractor:

    def __init__(self):
        self.x = None
        self.y = None
        self.bin = None

        self.d = None
        self.bout = None

        self.__xor1 = XorGate()
        self.__xor2 = XorGate()
        self.__and1 = AndGate()
        self.__and2 = AndGate()
        self.__or1 = OrGate()
        self.__not2 = NotGate()
        self.__not3 = NotGate()

    def eval(self):
        self.__xor1.a = self.x
        self.__xor1.b = self.y
        self.__xor1.eval()

        self.__xor2.a = self.__xor1.q
        self.__xor2.b = self.bin
        self.__xor2.eval()

        self.__not2.a = self.x
        self.__not2.eval()

        self.__and1.a = self.__not2.q
        self.__and1.b = self.y
        self.__and1.eval()

        self.__not3.a = self.__xor1.q
        self.__not3.eval()

        self.__and2.a = self.bin
        self.__and2.b = self.__not3.q
        self.__and2.eval()

        self.__or1.a = self.__and1.q
        self.__or1.b = self.__and2.q
        self.__or1.eval()

        self.d = self.__xor2.q
        self.bout = self.__or1.q

class RCSubtractor:

    def __init__(self, width):
        self.__width = width
        self.x = [None for _ in range(width)]
        self.y = [None for _ in range(width)]
        self.d = [None for _ in range(width)]
        self.b = None

        self.__subtractors = [FullSubtractor() for _ in range(width)]

    def eval(self):
        for k in range(self.__width - 1, -1, -1):
            subtractor = self.__subtractors[k]
            subtractor.x = self.x[k]
            subtractor.y = self.y[k]
            if k == self.__width - 1:
                subtractor.bin = 0
            else:
                subtractor.bin = self.__subtractors[k + 1].bout
            subtractor.eval()
            self.d[k] = self.__subtractors[k].d
        self.b = self.__subtractors[0].bout

    def __str__(self):
        return 'X' + to_bit(self.b) + to_bit_arr(self.x) + '\nY ' + to_bit_arr(self.y) + '\nD ' + to_bit_arr(self.d)
