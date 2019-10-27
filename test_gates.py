from gates import *

def test_or():
    or_gate = OrGate()

    or_gate.a = 0
    or_gate.b = 0
    or_gate.eval()

    assert or_gate.q == 0
    assert or_gate.__str__() == 'ABQ\n000'

    or_gate.a = 1
    or_gate.b = 0
    or_gate.eval()

    assert or_gate.q == 1
    assert or_gate.__str__() == 'ABQ\n101'

    or_gate.a = 0
    or_gate.b = 1
    or_gate.eval()

    assert or_gate.q == 1
    assert or_gate.__str__() == 'ABQ\n011'

    or_gate.a = 1
    or_gate.b = 1
    or_gate.eval()

    assert or_gate.q == 1
    assert or_gate.__str__() == 'ABQ\n111'

def test_xor():
    xor_gate = XorGate()

    xor_gate.a = 0
    xor_gate.b = 0
    xor_gate.eval()

    assert xor_gate.q == 0
    assert xor_gate.__str__() == 'ABQ\n000'

    xor_gate.a = 1
    xor_gate.b = 0
    xor_gate.eval()

    assert xor_gate.q == 1
    assert xor_gate.__str__() == 'ABQ\n101'

    xor_gate.a = 0
    xor_gate.b = 1
    xor_gate.eval()

    assert xor_gate.q == 1
    assert xor_gate.__str__() == 'ABQ\n011'

    xor_gate.a = 1
    xor_gate.b = 1
    xor_gate.eval()

    assert xor_gate.q == 0
    assert xor_gate.__str__() == 'ABQ\n110'
