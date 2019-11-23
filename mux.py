from decoders import Decoder2By4
from three_state import ThreeState

class Multiplexer:

    def __init__(self):
        self.i0 = None
        self.i1 = None
        self.i2 = None
        self.i3 = None

        self.sel1 = None
        self.sel2 = None

        self.out = None

        self.__decoder = Decoder2By4()
        self.__three_state0 = ThreeState()
        self.__three_state1 = ThreeState()
        self.__three_state2 = ThreeState()
        self.__three_state3 = ThreeState()

    def eval(self):
        self.__decoder.a = self.sel1
        self.__decoder.b = self.sel2
        self.__decoder.eval()

        self.__three_state0.a = self.i0
        self.__three_state0.b = self.__decoder.d0
        self.__three_state0.eval()

        self.__three_state1.a = self.i1
        self.__three_state1.b = self.__decoder.d1
        self.__three_state1.eval()

        self.__three_state2.a = self.i2
        self.__three_state2.b = self.__decoder.d2
        self.__three_state2.eval()

        self.__three_state3.a = self.i3
        self.__three_state3.b = self.__decoder.d3
        self.__three_state3.eval()

        print(self.__three_state0.c)
        print(self.__three_state1.c)
        print(self.__three_state2.c)
        print(self.__three_state3.c)
        
        self.out = list(filter(lambda x: x != None, [self.__three_state0.c, self.__three_state1.c, self.__three_state2.c, self.__three_state3.c]))[0]
