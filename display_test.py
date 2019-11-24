from display import NumDisplay

def test_num_display():
    display = NumDisplay(4)
    display.a = [True, False, False, False]
    
    display.eval()

    assert display.out == 8
