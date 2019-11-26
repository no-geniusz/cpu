from subtractors import FullSubtractor, RCSubtractor

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

def test_rc_substractor_borrow():
    rc_substractor = RCSubtractor(4)

    rc_substractor.x = [0, 0, 0, 0]
    rc_substractor.y = [1, 1, 1, 1]
    rc_substractor.eval()

    assert rc_substractor.d == [0, 0, 0, 1]
    assert rc_substractor.b == 1

    assert str(rc_substractor) == 'X10000\nY 1111\nD 0001'

def test_rc_substractor():
    rc_substractor = RCSubtractor(4)

    rc_substractor.x = [1, 0, 1, 0]
    rc_substractor.y = [0, 1, 1, 1]
    rc_substractor.eval()

    assert rc_substractor.d == [0, 0, 1, 1]
    assert rc_substractor.b == 0

    assert str(rc_substractor) == 'X01010\nY 0111\nD 0011'
