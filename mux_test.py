from registers import REG_WIDTH
from mux import Multiplexer

def test_mux():
    mux = Multiplexer(4)

    mux.i0 = [1, 0, 0, 0]
    mux.i1 = [0, 0, 0, 1]
    mux.i2 = [1, 1, 0, 0]
    mux.i3 = [1, 1, 1, 0]

    mux.sel1 = 0
    mux.sel2 = 0
    mux.eval()
    assert mux.out == mux.i0

    mux.sel1 = 0
    mux.sel2 = 1
    mux.eval()
    assert mux.out == mux.i1

    mux.sel1 = 1
    mux.sel2 = 0
    mux.eval()
    assert mux.out == mux.i2

    mux.sel1 = 1
    mux.sel2 = 1
    mux.eval()
    assert mux.out == mux.i3
