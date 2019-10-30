from subtractors import FullSubtractor

def test_subtract_000():
    subtractor = FullSubtractor()

    subtractor.x = 0
    subtractor.y = 0
    subtractor.bin = 0

    subtractor.eval()

    assert subtractor.d == 0
    assert subtractor.bout == 0

def test_subtract_001():
    subtractor = FullSubtractor()

    subtractor.x = 0
    subtractor.y = 0
    subtractor.bin = 1

    subtractor.eval()

    assert subtractor.d == 1
    assert subtractor.bout == 1

def test_subtract_010():
    subtractor = FullSubtractor()

    subtractor.x = 0
    subtractor.y = 1
    subtractor.bin = 0

    subtractor.eval()

    assert subtractor.d == 1
    assert subtractor.bout == 1

def test_subtract_011():
    subtractor = FullSubtractor()

    subtractor.x = 0
    subtractor.y = 1
    subtractor.bin = 1

    subtractor.eval()

    assert subtractor.d == 0
    assert subtractor.bout == 1

def test_subtract_100():
    subtractor = FullSubtractor()

    subtractor.x = 1
    subtractor.y = 0
    subtractor.bin = 0

    subtractor.eval()

    assert subtractor.d == 1
    assert subtractor.bout == 0

def test_subtract_101():
    subtractor = FullSubtractor()

    subtractor.x = 1
    subtractor.y = 0
    subtractor.bin = 1

    subtractor.eval()

    assert subtractor.d == 0
    assert subtractor.bout == 0

def test_subtract_110():
    subtractor = FullSubtractor()

    subtractor.x = 1
    subtractor.y = 1
    subtractor.bin = 0

    subtractor.eval()

    assert subtractor.d == 0
    assert subtractor.bout == 0

def test_subtract_111():
    subtractor = FullSubtractor()

    subtractor.x = 1
    subtractor.y = 1
    subtractor.bin = 1

    subtractor.eval()

    assert subtractor.d == 1
    assert subtractor.bout == 1
