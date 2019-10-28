from adders import FullAdder

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
