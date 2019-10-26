from latches import DLatch
from util import to_bit

class ShiftRegister:

    size = 4

    def __init__(self):
        self.data = []
        self.latches = []

        for i in range(ShiftRegister.size):
            self.data.insert(0, None)
            self.latches.insert(0, DLatch())

        self.e = None
        self.d = None

    def eval(self):
        for i in range(ShiftRegister.size - 1):
            self.latches[i].d = self.latches[i + 1].q
            self.latches[i].e = self.e
            self.latches[i].eval()
            self.data[i] = self.latches[i].q

        i = ShiftRegister.size - 1
        self.latches[i].d = self.d
        self.latches[i].e = self.e
        self.latches[i].eval()
        self.data[i] = self.latches[i].q

    def __str__(self):
        s = 'E%s, D%s\n' % (to_bit(self.e), to_bit(self.d))
        
        for i in range(ShiftRegister.size):
            s = s + 'D' + str(ShiftRegister.size - i - 1) + ' '
        
        s = s + '\n'
        
        for i in range(ShiftRegister.size):
            s = s + ' ' + to_bit(self.data[ShiftRegister.size - i - 1]) + ' '

        return s
