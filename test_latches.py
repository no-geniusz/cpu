from latches import SRLatch, DLatch

def test_SRLatch():
    sr_latch = SRLatch()

    sr_latch.r = 1
    sr_latch.s = 0
    sr_latch.eval()

    assert sr_latch.q == 0
    assert sr_latch.nq == 1

    sr_latch.r = 0
    sr_latch.s = 0
    sr_latch.eval()

    assert sr_latch.q == 0
    assert sr_latch.nq == 1

    sr_latch.r = 0
    sr_latch.s = 1
    sr_latch.eval()

    assert sr_latch.q == 1
    assert sr_latch.nq == 0

    sr_latch.r = 0
    sr_latch.s = 0
    sr_latch.eval()

    assert sr_latch.q == 1
    assert sr_latch.nq == 0

def test_DLatch():
    d_latch = DLatch()

    d_latch.d = 0
    d_latch.e = 1
    d_latch.eval()

    assert d_latch.q == 0
    assert d_latch.nq == 1

    d_latch.d = 0
    d_latch.e = 0
    d_latch.eval()

    assert d_latch.q == 0
    assert d_latch.nq == 1

    d_latch.d = 1
    d_latch.e = 0
    d_latch.eval()

    assert d_latch.q == 0
    assert d_latch.nq == 1

    d_latch.d = 1
    d_latch.e = 1
    d_latch.eval()

    assert d_latch.q == 1
    assert d_latch.nq == 0

    d_latch.d = 1
    d_latch.e = 0
    d_latch.eval()

    assert d_latch.q == 1
    assert d_latch.nq == 0

    d_latch.d = 0
    d_latch.e = 0
    d_latch.eval()

    assert d_latch.q == 1
    assert d_latch.nq == 0
