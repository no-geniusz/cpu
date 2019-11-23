from registers import WideRegister
from decoders import Decoder4By16
from gates import AndGate

class Memory:
    
    WORD_SIZE = 8
    ADDR_SIZE = 4
    MEM_SIZE = 2 ** ADDR_SIZE

    def __init__(self):
        self.write = None
        self.enable = None
        self.clk = None
        self.d = [None] * Memory.WORD_SIZE
        self.o = [None] * Memory.WORD_SIZE
        self.a = [None] * Memory.ADDR_SIZE

        self.__words = [WideRegister(Memory.WORD_SIZE) for _ in range(Memory.MEM_SIZE)]
        self.__decoder = Decoder4By16()
        self.__enable_ands = [AndGate() for _ in range(Memory.MEM_SIZE)]
        self.__write_ands = [AndGate() for _ in range(Memory.MEM_SIZE)]

    def eval(self):
        self.__decoder.a = self.a
        self.__decoder.eval()

        for k in range(Memory.MEM_SIZE):
            gate = self.__enable_ands[k]
            gate.a = self.enable
            gate.b = self.__decoder.d[k]
            gate.eval()

        for k in range(Memory.MEM_SIZE):
            gate = self.__write_ands[k]
            gate.a = self.write
            gate.b = self.__decoder.d[k]
            gate.eval()

        for k in range(Memory.MEM_SIZE):
            word = self.__words[k]
            
            word.enable = self.__enable_ands[k].q
            word.load = self.__write_ands[k].q
            word.clk = self.clk
            word.d = self.d
            
            word.eval()

        for j in range(Memory.WORD_SIZE):
            for k in range(Memory.MEM_SIZE):
                word = self.__words[k]
                
                self.o[j] = word.q[j]
                if word.q[j] != None:
                    break
