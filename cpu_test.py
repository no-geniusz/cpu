from cpu import CPU

def test_out_register():
    cpu = CPU()
    cpu.clk = 1

    cpu.bus.line = [1, 0, 0, 0, 0, 0, 0, 1]

    cpu.out_register.load = 1
    cpu.out_register.enable = 1

    cpu.eval()

    assert cpu.display.out == 129

def test_mem_write_read():

    cpu = CPU()
    cpu.clk = 1

    __mem_addr(cpu, [1, 0, 0, 1])
    __mem_write(cpu, [1, 0, 0, 0, 1, 0, 0, 0])

    __mem_addr(cpu, [0, 0, 0, 1])
    __mem_write(cpu, [0, 1, 1, 1, 0, 1, 1, 1])

    __mem_addr(cpu, [1, 0, 0, 1])
    assert __mem_read(cpu) == [1, 0, 0, 0, 1, 0, 0, 0]

    __mem_addr(cpu, [0, 0, 0, 1])
    assert __mem_read(cpu) == [0, 1, 1, 1, 0, 1, 1, 1]

def test_register_a():
    cpu = CPU()
    cpu.clk = 1

    cpu.bus.line = [1, 0, 0, 1, 1, 1, 0, 0]
    cpu.register_a.enable = 0
    cpu.register_a.load = 1
    cpu.eval()

    cpu.bus.line = [0, 0, 0, 0, 0, 0, 0, 0]
    cpu.register_a.load = 0
    cpu.eval()

    cpu.register_a.enable = 1
    cpu.eval()

    assert cpu.bus.line == [1, 0, 0, 1, 1, 1, 0, 0]

def test_register_b():
    cpu = CPU()
    cpu.clk = 1

    cpu.bus.line = [1, 0, 0, 1, 1, 1, 0, 0]
    cpu.register_b.enable = 0
    cpu.register_b.load = 1
    cpu.eval()

    cpu.bus.line = [0, 0, 0, 0, 0, 0, 0, 0]
    cpu.register_b.load = 0
    cpu.eval()

    cpu.register_b.enable = 1
    cpu.eval()

    assert cpu.bus.line == [1, 0, 0, 1, 1, 1, 0, 0]

def __mem_addr(cpu, addr):
    cpu.bus.line = [0, 0, 0, 0] + addr
    cpu.memory.write = 0
    cpu.memory.enable = 0
    cpu.memory_register.load = 1
    cpu.memory_register.enable = 0
    cpu.eval()

def __mem_write(cpu, word):
    cpu.bus.line = word
    cpu.memory.write = 1
    cpu.memory.enable = 0
    cpu.memory_register.load = 0
    cpu.memory_register.enable = 1
    cpu.eval()

def __mem_read(cpu):
    cpu.memory.write = 0
    cpu.memory.enable = 1
    cpu.memory_register.load = 0
    cpu.memory_register.enable = 1
    cpu.eval()

    return cpu.bus.line
