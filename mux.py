from gates import AndGate, NotGate
from registers import REG_WIDTH

class Multiplexer:

    i0 = [None for k in range(REG_WIDTH)]
    i1 = [None for k in range(REG_WIDTH)]
    i2 = [None for k in range(REG_WIDTH)]
    i3 = [None for k in range(REG_WIDTH)]

    sel1 = None
    sel2 = None

    out = [None for k in range(REG_WIDTH)]

    _and0 = AndGate()
    _and1 = AndGate()
    _and2 = AndGate()
    _and3 = AndGate()

    _not00 = NotGate()
    _not01 = NotGate()
    _not10 = NotGate()
    _not21 = NotGate()

    def eval(self):
        self._not00.a = self.sel1
        self._not00.eval()

        self._not01.a = self.sel2
        self._not01.eval()

        self._and0.a = self._not00.q
        self._and0.b = self._not01.q
        self._and0.eval()

        if self._and0.q:
            for k in range(REG_WIDTH):
                self.out[k] = self.i0[k]

        self._not10.a = self.sel1
        self._not10.eval()
        
        self._and1.a = self._not10.q
        self._and1.b = self.sel2
        self._and1.eval()

        if self._and1.q:
            for k in range(REG_WIDTH):
                self.out[k] = self.i1[k]

        self._not21.a = self.sel2
        self._not21.eval()
        
        self._and2.a = self.sel1
        self._and2.b = self._not21.q
        self._and2.eval()

        if self._and2.q:
            for k in range(REG_WIDTH):
                self.out[k] = self.i2[k]

        self._and3.a = self.sel1
        self._and3.b = self.sel2
        self._and3.eval()

        if self._and3.q:
            for k in range(REG_WIDTH):
                self.out[k] = self.i3[k]
