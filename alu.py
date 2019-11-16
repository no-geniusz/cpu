from adders import RCAdder
from subtractors import RCSubtractor
from mux import Multiplexer

class Alu:

    def __init__(self, width):
        self.__width = width

        self.a = [None for k in range(width)]
        self.b = [None for k in range(width)]
        self.o = [None for k in range(2)]
        self.x = [None for k in range(width)]

        self.__adder = RCAdder(width)
        self.__subtractor = RCSubtractor(width)
        self.__mux = Multiplexer(width)

    def eval(self):
        for k in range(self.__width):
            self.__adder.a[k] = self.a[k]
            self.__adder.b[k] = self.b[k]
            self.__subtractor.x[k] = self.a[k]
            self.__subtractor.y[k] = self.b[k]
        self.__adder.eval()
        self.__subtractor.eval()

        for k in range(self.__width):
            self.__mux.i0[k] = self.__adder.s[k]
            self.__mux.i1[k] = self.__subtractor.d[k]
        self.__mux.sel2 = self.o[0]
        self.__mux.sel1 = self.o[1]
        self.__mux.eval()

        for k in range(self.__width):
            self.x[k] = self.__mux.out[k]
