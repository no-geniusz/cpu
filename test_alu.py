from alu import Alu

def test_alu():
    alu = Alu()

    alu.a[0] = 0
    alu.a[1] = 0
    alu.a[2] = 0
    alu.a[3] = 1

    alu.b[0] = 0
    alu.b[1] = 1
    alu.b[2] = 1
    alu.b[3] = 0

    alu.o[0] = 0
    alu.o[1] = 0
    alu.eval()

    assert alu.x[0] == 0
    assert alu.x[1] == 1
    assert alu.x[2] == 1
    assert alu.x[3] == 1

    alu.o[0] = 1
    alu.o[1] = 0
    alu.eval()

    assert alu.x[0] == 0
    assert alu.x[1] == 1
    assert alu.x[2] == 0
    assert alu.x[3] == 0
