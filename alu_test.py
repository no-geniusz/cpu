from alu import Alu

def test_alu():
    alu = Alu(4)
    alu.enabled = True

    alu.a = [0, 0, 0, 1]
    alu.b = [0, 1, 1, 0]
    alu.o = [0, 0]
    alu.eval()

    assert alu.x == [0, 1, 1, 1]

    alu.o = [1, 0]
    alu.eval()

    assert alu.x == [0, 1, 0, 0]

    alu.enabled = False
    alu.eval()

    assert alu.x == [None, None, None, None]
