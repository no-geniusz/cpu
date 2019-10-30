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
    rc_adder = RCAdder()

    rc_adder.a[0] = 1
    rc_adder.a[1] = 1
    rc_adder.a[2] = 1
    rc_adder.a[3] = 1

    rc_adder.b[0] = 1
    rc_adder.b[1] = 1
    rc_adder.b[2] = 1
    rc_adder.b[3] = 1

    rc_adder.eval()

    assert rc_adder.s[0] == 0
    assert rc_adder.s[1] == 1
    assert rc_adder.s[2] == 1
    assert rc_adder.s[3] == 1
    assert rc_adder.c == 1

    assert rc_adder.__str__() == 'AAAA BBBB CSSSS\n1111 1111 11110'

def test_rc_adder():
    rc_adder = RCAdder()

    rc_adder.a[0] = 1
    rc_adder.a[1] = 1
    rc_adder.a[2] = 1
    rc_adder.a[3] = 0

    rc_adder.b[0] = 1
    rc_adder.b[1] = 0
    rc_adder.b[2] = 1
    rc_adder.b[3] = 0

    rc_adder.eval()

    assert rc_adder.s[0] == 0
    assert rc_adder.s[1] == 0
    assert rc_adder.s[2] == 1
    assert rc_adder.s[3] == 1
    assert rc_adder.c == 0

    assert rc_adder.__str__() == 'AAAA BBBB CSSSS\n0111 0101 01100'
