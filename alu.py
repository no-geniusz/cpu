from adders import RCAdder
from subtractors import RCSubtractor
from mux import Multiplexer

class Alu:

    def __init__(self, width):
        self.__width = width

        self.a = [None for _ in range(width)]
        self.b = [None for _ in range(width)]
        self.o = [None for _ in range(2)]
        self.x = [None for _ in range(width)]

        self.__adder = RCAdder(width)
        self.__subtractor = RCSubtractor(width)
        self.__muxes = [Multiplexer() for _ in range(width)]

    def eval(self):
        for k in range(self.__width):
            self.__adder.a[k] = self.a[k]
            self.__adder.b[k] = self.b[k]
            self.__subtractor.x[k] = self.a[k]
            self.__subtractor.y[k] = self.b[k]
        self.__adder.eval()
        self.__subtractor.eval()

        for k in range(self.__width):
            self.__muxes[k].i0 = self.__adder.s[k]
            self.__muxes[k].i1 = self.__subtractor.d[k]
            self.__muxes[k].sel1 = self.o[0]
            self.__muxes[k].sel2 = self.o[1]
            self.__muxes[k].eval()

        for k in range(self.__width):
            self.x[k] = self.__muxes[k].out
