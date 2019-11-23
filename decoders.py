from gates import AndGate, NotGate
import math

class Decoder2By4:
    
    def __init__(self):
        self.a = None
        self.b = None

        self.d0 = None
        self.d1 = None
        self.d2 = None
        self.d3 = None

        self.__nots = [NotGate() for _ in range(2)]
        self.__ands = [AndGate() for _ in range(4)]

    def eval_internal(self):
        self.__nots[0].a = self.a
        self.__nots[0].eval()
        self.__nots[1].a = self.b
        self.__nots[1].eval()

        self.__ands[0].a = self.__nots[0].q
        self.__ands[0].b = self.__nots[1].q
        self.__ands[0].eval()

        self.__ands[1].a = self.a
        self.__ands[1].b = self.__nots[1].q
        self.__ands[1].eval()

        self.__ands[2].a = self.b
        self.__ands[2].b = self.__nots[0].q
        self.__ands[2].eval()

        self.__ands[3].a = self.b
        self.__ands[3].b = self.a
        self.__ands[3].eval()

    def eval(self):
        self.eval_internal()

        self.d0 = self.__ands[0].q
        self.d1 = self.__ands[1].q
        self.d2 = self.__ands[2].q
        self.d3 = self.__ands[3].q

class Decoder2By4E:
    
    def __init__(self):
        self.enable = None

        self.a = None
        self.b = None

        self.d0 = None
        self.d1 = None
        self.d2 = None
        self.d3 = None

        self.__decoder_2_by_4 = Decoder2By4()
        self.__enable_ands = [AndGate() for _ in range(4)]

    def eval(self):
        self.__decoder_2_by_4.a = self.a
        self.__decoder_2_by_4.b = self.b

        for k in range(4):
            setattr(self.__decoder_2_by_4, f'd{k}', getattr(self, f'd{k}'))

        self.__decoder_2_by_4.eval()

        for k in range(4):
            self.__enable_ands[k].a = getattr(self.__decoder_2_by_4, f'd{k}')
            self.__enable_ands[k].b = self.enable
            self.__enable_ands[k].eval()

        self.d0 = self.__enable_ands[0].q
        self.d1 = self.__enable_ands[1].q
        self.d2 = self.__enable_ands[2].q
        self.d3 = self.__enable_ands[3].q

class Decoder4By16:
    
    def __init__(self):
        self.a = [None] * 4
        self.d = [None] * 0x10

        self.__e_decs = [Decoder2By4E() for _ in range(4)]
        self.__entry_dec = Decoder2By4()

    def eval(self):
        self.__entry_dec.b = self.a[0]
        self.__entry_dec.a = self.a[1]
        self.__entry_dec.eval()

        for k in range(4):
            self.__e_decs[k].b = self.a[2]
            self.__e_decs[k].a = self.a[3]
            self.__e_decs[k].enable = getattr(self.__entry_dec, f'd{k}')
            self.__e_decs[k].eval()
        
        for k in range(0x10):
            self.d[k] = getattr(self.__e_decs[math.floor(k / 4)], f'd{k % 4}')
