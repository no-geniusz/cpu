from registers import REG_WIDTH
from mux import Multiplexer

def test_mux():
    mux = Multiplexer()

    mux.i0[0] = 1
    mux.i0[1] = 0
    mux.i0[2] = 0
    mux.i0[3] = 0

    mux.i1[0] = 0
    mux.i1[1] = 0
    mux.i1[2] = 0
    mux.i1[3] = 1

    mux.i2[0] = 1
    mux.i2[1] = 1
    mux.i2[2] = 0
    mux.i2[3] = 0

    mux.i3[0] = 1
    mux.i3[1] = 1
    mux.i3[2] = 1
    mux.i3[3] = 0

    mux.sel1 = 0
    mux.sel2 = 0

    mux.eval()

    for k in range(REG_WIDTH):
        assert mux.out[k] == mux.i0[k]

    mux.sel1 = 0
    mux.sel2 = 1

    mux.eval()

    for k in range(REG_WIDTH):
        assert mux.out[k] == mux.i1[k]

    mux.sel1 = 1
    mux.sel2 = 0

    mux.eval()

    for k in range(REG_WIDTH):
        assert mux.out[k] == mux.i2[k]

    mux.sel1 = 1
    mux.sel2 = 1

    mux.eval()

    for k in range(REG_WIDTH):
        assert mux.out[k] == mux.i3[k]
