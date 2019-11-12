from latches import JKFlipFlop
from gates import AndGate
from util import to_bit

class Counter:

    REG_WIDTH = 4
    
    def __init__(self):
        self.clk = None
        self.out = [None for _ in range(Counter.REG_WIDTH)]

        self.__flip_flops = [JKFlipFlop() for _ in range(Counter.REG_WIDTH)]
        self.__and_gates = [AndGate() for _ in range(Counter.REG_WIDTH - 2)]

    def reset(self):
        for ff in self.__flip_flops:
            ff.j = 0
            ff.k = 1
            ff.clk = 1
            ff.eval()
        for k in range(Counter.REG_WIDTH):
            self.out[k] = self.__flip_flops[k].q

    def eval(self):
        for k in range(Counter.REG_WIDTH):
            current_ff = self.__flip_flops[Counter.REG_WIDTH - k - 1]
            prev_ff = self.__flip_flops[Counter.REG_WIDTH - k] if k > 0 else None
            
            if k == 0:
                current_ff.j = 1
                current_ff.k = 1
            elif k == 1:
                current_ff.j = prev_ff.q
                current_ff.k = prev_ff.q
            else:
                and_gate = self.__and_gates[Counter.REG_WIDTH - k - 2]
                and_gate.a = prev_ff.q
                and_gate.b = prev_ff.j
                and_gate.eval()

                current_ff.j = and_gate.q
                current_ff.k = and_gate.q

            current_ff.clk = self.clk

        for k in range(Counter.REG_WIDTH - 1, -1, -1):
            current_ff = self.__flip_flops[k]
            current_ff.eval()
            self.out[k] = self.__flip_flops[k].q

    def __str__(self):
        q_str = ''
        for f in self.out:
            q_str += to_bit(f)
        return 'Q' * Counter.REG_WIDTH + '\n' + q_str

