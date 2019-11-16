from latches import DLatch
from util import to_bit

REG_WIDTH = 4

class ShiftRegister:

    def __init__(self):
        self.data = []
        self.latches = []

        for i in range(REG_WIDTH):
            self.data.insert(0, None)
            self.latches.insert(0, DLatch())

        self.e = None
        self.d = None

    def eval(self):
        for i in range(REG_WIDTH - 1):
            self.latches[i].d = self.latches[i + 1].q
            self.latches[i].e = self.e
            self.latches[i].eval()
            self.data[i] = self.latches[i].q

        i = REG_WIDTH - 1
        self.latches[i].d = self.d
        self.latches[i].e = self.e
        self.latches[i].eval()
        self.data[i] = self.latches[i].q

    def __str__(self):
        s = 'E%s, D%s\n' % (to_bit(self.e), to_bit(self.d))
        
        for i in range(REG_WIDTH):
            s = s + 'D' + str(REG_WIDTH - i - 1) + ' '
        
        s = s + '\n'
        
        for i in range(REG_WIDTH):
            s = s + ' ' + to_bit(self.data[REG_WIDTH - i - 1]) + ' '

        return s

class FourBitRegister:

    def __init__(self):
        self.d = [None for k in range(REG_WIDTH)]
        self.q = [None for k in range(REG_WIDTH)]
        self.latches = [DLatch() for _ in range(REG_WIDTH)]
        self.e  = None

    def eval(self):
        for i in range(REG_WIDTH):
            self.latches[i].d = self.d[i]
            self.latches[i].e = self.e
            print('before: ' + self.latches[i].__str__())
            self.latches[i].eval()
            print('after: ' + self.latches[i].__str__())
            self.q[i] = self.latches[i].q

    def __str__(self):
        s = 'E%s\n' % (to_bit(self.e))
        s += 'D' * REG_WIDTH + '\n'
        for i in range(REG_WIDTH, 0, -1):
            s = s + to_bit(self.d[i - 1])
        s = s + '\n'
        s += 'Q' * REG_WIDTH + '\n'
        for i in range(REG_WIDTH, 0, -1):
            s = s + to_bit(self.q[i - 1])

        return s
