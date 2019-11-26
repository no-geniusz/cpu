from three_state import ThreeState, WideThreeState

def test_three_state_off():
    three_state = ThreeState()
    
    three_state.a = 1
    three_state.b = 0
    three_state.eval()

    assert three_state.c == None

def test_three_state_on():
    three_state = ThreeState()

    three_state.a = 1
    three_state.b = 1
    three_state.eval()

    assert three_state.c == 1

def test_wide_three_state():
    three_state = WideThreeState(4)

    three_state.a = [1, 0, 1, 0]
    three_state.b = 0
    three_state.eval()

    assert three_state.c == [None] * 4

    three_state.a = [1, 0, 1, 0]
    three_state.b = 1
    three_state.eval()

    assert three_state.c == [1, 0, 1, 0]
