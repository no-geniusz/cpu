from memory import Memory

def test_memory():
    memory = Memory()

    memory.clk = 1
    memory.enable = 0
    memory.write = 1

    memory.a = [0, 0, 0, 0]
    memory.d = [0, 0, 0, 0, 0, 0, 0, 1]
    memory.eval()

    memory.a = [0, 0, 0, 1]
    memory.d = [0, 0, 0, 0, 0, 0, 1, 0]
    memory.eval()

    memory.a = [1, 1, 1, 1]
    memory.d = [1, 0, 0, 0, 0, 0, 0, 1]
    memory.eval()

    memory.enable = 1
    memory.write = 0

    memory.a = [0, 0, 0, 0]
    memory.eval()
    assert memory.o == [0, 0, 0, 0, 0, 0, 0, 1]

    memory.a = [0, 0, 0, 1]
    memory.eval()
    assert memory.o == [0, 0, 0, 0, 0, 0, 1, 0]

    memory.a = [1, 1, 1, 1]
    memory.eval()
    assert memory.o == [1, 0, 0, 0, 0, 0, 0, 1]

    memory.enable = 0
    memory.eval()
    assert memory.o == [None] * 8
