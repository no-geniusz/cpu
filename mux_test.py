from mux import Multiplexer

def test_mux00():
    mux = Multiplexer()

    mux.i0 = 1
    mux.i1 = 0
    mux.i2 = 0
    mux.i3 = 0

    mux.sel1 = 0
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 1

    mux.sel1 = 1
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 0
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 1
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 0

def test_mux01():
    mux = Multiplexer()

    mux.i0 = 0
    mux.i1 = 1
    mux.i2 = 0
    mux.i3 = 0

    mux.sel1 = 0
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 1
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 1

    mux.sel1 = 0
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 1
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 0

def test_mux10():
    mux = Multiplexer()

    mux.i0 = 0
    mux.i1 = 0
    mux.i2 = 1
    mux.i3 = 0

    mux.sel1 = 0
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 1
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 0
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 1

    mux.sel1 = 1
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 0

def test_mux11():
    mux = Multiplexer()

    mux.i0 = 0
    mux.i1 = 0
    mux.i2 = 0
    mux.i3 = 1

    mux.sel1 = 0
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 1
    mux.sel2 = 0
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 0
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 0

    mux.sel1 = 1
    mux.sel2 = 1
    mux.eval()
    assert mux.out == 1
