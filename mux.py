from gates import AndGate, NotGate

class Multiplexer:

    def __init__(self, width):
        self.__width = width

        self.i0 = [None for _ in range(width)]
        self.i1 = [None for _ in range(width)]
        self.i2 = [None for _ in range(width)]
        self.i3 = [None for _ in range(width)]

        self.sel1 = None
        self.sel2 = None

        self.out = [None for _ in range(width)]

        self.__and0 = AndGate()
        self.__and1 = AndGate()
        self.__and2 = AndGate()
        self.__and3 = AndGate()

        self.__not00 = NotGate()
        self.__not01 = NotGate()
        self.__not10 = NotGate()
        self.__not21 = NotGate()

    def eval(self):
        self.__not00.a = self.sel1
        self.__not00.eval()

        self.__not01.a = self.sel2
        self.__not01.eval()

        self.__and0.a = self.__not00.q
        self.__and0.b = self.__not01.q
        self.__and0.eval()

        if self.__and0.q:
            for k in range(self.__width):
                self.out[k] = self.i0[k]

        self.__not10.a = self.sel1
        self.__not10.eval()
        
        self.__and1.a = self.__not10.q
        self.__and1.b = self.sel2
        self.__and1.eval()

        if self.__and1.q:
            for k in range(self.__width):
                self.out[k] = self.i1[k]

        self.__not21.a = self.sel2
        self.__not21.eval()
        
        self.__and2.a = self.sel1
        self.__and2.b = self.__not21.q
        self.__and2.eval()

        if self.__and2.q:
            for k in range(self.__width):
                self.out[k] = self.i2[k]

        self.__and3.a = self.sel1
        self.__and3.b = self.sel2
        self.__and3.eval()

        if self.__and3.q:
            for k in range(self.__width):
                self.out[k] = self.i3[k]
