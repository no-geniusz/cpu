from adders import FullAdder, RCAdder

def test_adding_000():
    adder = FullAdder()

    adder.a = 0
    adder.b = 0
    adder.cin = 0

    adder.eval()

    assert adder.s == 0
    assert adder.cout == 0

def test_adding_001():
    adder = FullAdder()

    adder.a = 0
    adder.b = 0
    adder.cin = 1

    adder.eval()

    assert adder.s == 1
    assert adder.cout == 0

def test_adding_010():
    adder = FullAdder()

    adder.a = 0
    adder.b = 1
    adder.cin = 0

    adder.eval()

    assert adder.s == 1
    assert adder.cout == 0

def test_adding_011():
    adder = FullAdder()

    adder.a = 0
    adder.b = 1
    adder.cin = 1

    adder.eval()

    assert adder.s == 0
    assert adder.cout == 1

def test_adding_100():
    adder = FullAdder()

    adder.a = 1
    adder.b = 0
    adder.cin = 0

    adder.eval()

    assert adder.s == 1
    assert adder.cout == 0

def test_adding_101():
    adder = FullAdder()

    adder.a = 1
    adder.b = 0
    adder.cin = 1

    adder.eval()

    assert adder.s == 0
    assert adder.cout == 1

def test_adding_110():
    adder = FullAdder()

    adder.a = 1
    adder.b = 1
    adder.cin = 0

    adder.eval()

    assert adder.s == 0
    assert adder.cout == 1

def test_adding_111():
    adder = FullAdder()

    adder.a = 1
    adder.b = 1
    adder.cin = 1

    adder.eval()

    assert adder.s == 1
    assert adder.cout == 1

def test_rc_adder_carry():
    rc_adder = RCAdder(4)

    rc_adder.a = [1, 1, 1, 1]
    rc_adder.b = [1, 1, 1, 1]
    rc_adder.eval()

    assert rc_adder.s == [1, 1, 1, 0]
    assert rc_adder.c == 1

    assert str(rc_adder) == 'A 1111\nB 1111\nC11110'

def test_rc_adder():
    rc_adder = RCAdder(4)

    rc_adder.a = [0, 1, 1, 1]
    rc_adder.b = [0, 1, 0, 1]
    rc_adder.eval()

    assert rc_adder.s == [1, 1, 0, 0]
    assert rc_adder.c == 0

    assert str(rc_adder) == 'A 0111\nB 0101\nC01100'
