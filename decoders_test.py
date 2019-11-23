from decoders import Decoder2By4, Decoder2By4E, Decoder4By16

def test_decoder00():
    decoder = Decoder2By4()

    decoder.a = 0
    decoder.b = 0
    decoder.eval()

    assert decoder.d0 == 1
    assert decoder.d1 == 0
    assert decoder.d2 == 0
    assert decoder.d3 == 0

def test_decoder01():
    decoder = Decoder2By4()

    decoder.a = 1
    decoder.b = 0
    decoder.eval()

    assert decoder.d0 == 0
    assert decoder.d1 == 1
    assert decoder.d2 == 0
    assert decoder.d3 == 0

def test_decoder10():
    decoder = Decoder2By4()

    decoder.a = 0
    decoder.b = 1
    decoder.eval()

    assert decoder.d0 == 0
    assert decoder.d1 == 0
    assert decoder.d2 == 1
    assert decoder.d3 == 0

def test_decoder11():
    decoder = Decoder2By4()

    decoder.a = 1
    decoder.b = 1
    decoder.eval()

    assert decoder.d0 == 0
    assert decoder.d1 == 0
    assert decoder.d2 == 0
    assert decoder.d3 == 1

def test_enable():
    decoder = Decoder2By4E()

    decoder.a = 0
    decoder.b = 0

    decoder.enable = 0
    decoder.eval()
    assert decoder.d0 == 0

    decoder.enable = 1
    decoder.eval()
    assert decoder.d0 == 1

def test_4_by_16():
    decoder = Decoder4By16()

    for k in range(0xF):
        decoder.a = [k & 0x8, k & 0x4, k & 0x2, k & 0x1]
        decoder.eval()

        for j in range(0, 0xF):
            assert decoder.d[j] == (k == j)
