from counters import Counter

def test_counter():
    counter = Counter()
    counter.clk = 1
    counter.reset()

    assert counter.out == [False, False, False, False]
    assert counter.__str__() == 'QQQQ\n0000'

    for i in range(1, 2 ** Counter.REG_WIDTH + 1):
        counter.eval()

        for k in range(Counter.REG_WIDTH):
            assert counter.out[k] == bool(i & (2 ** (Counter.REG_WIDTH - k - 1)))

    assert counter.__str__() == 'QQQQ\n0000'
