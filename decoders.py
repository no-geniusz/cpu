from gates import AndGate, NotGate

class Decoder2By4:
    
    def __init__(self):
        self.a = None
        self.b = None

        self.d0 = None
        self.d1 = None
        self.d2 = None
        self.d3 = None

        self.__not0 = NotGate()
        self.__not1 = NotGate()

        self.__and0 = AndGate()
        self.__and1 = AndGate()
        self.__and2 = AndGate()
        self.__and3 = AndGate()

    def eval(self):
        self.__not0.a = self.a
        self.__not0.eval()
        self.__not1.a = self.b
        self.__not1.eval()

        self.__and0.a = self.__not0.q
        self.__and0.b = self.__not1.q
        self.__and0.eval()

        self.__and1.a = self.a
        self.__and1.b = self.__not1.q
        self.__and1.eval()

        self.__and2.a = self.b
        self.__and2.b = self.__not0.q
        self.__and2.eval()

        self.__and3.a = self.b
        self.__and3.b = self.a
        self.__and3.eval()

        self.d0 = self.__and0.q
        self.d1 = self.__and1.q
        self.d2 = self.__and2.q
        self.d3 = self.__and3.q
