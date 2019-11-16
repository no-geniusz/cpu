from registers import REG_WIDTH
from adders import RCAdder
from subtractors import RCSubtractor
from mux import Multiplexer

class Alu:

    a = [None for k in range(REG_WIDTH)]
    b = [None for k in range(REG_WIDTH)]
    o = [None for k in range(2)]
    x = [None for k in range(REG_WIDTH)]

    _adder = RCAdder(REG_WIDTH)
    _subtractor = RCSubtractor()
    _mux = Multiplexer()

    def eval(self):
        for k in range(REG_WIDTH):
            self._adder.a[k] = self.a[k]
            self._adder.b[k] = self.b[k]
            self._subtractor.x[k] = self.a[k]
            self._subtractor.y[k] = self.b[k]
        self._adder.eval()
        self._subtractor.eval()

        for k in range(REG_WIDTH):
            self._mux.i0[k] = self._adder.s[k]
            self._mux.i1[k] = self._subtractor.d[k]
        self._mux.sel2 = self.o[0]
        self._mux.sel1 = self.o[1]
        self._mux.eval()

        for k in range(REG_WIDTH):
            self.x[k] = self._mux.out[k]
