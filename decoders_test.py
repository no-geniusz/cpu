from decoders import Decoder2By4

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
