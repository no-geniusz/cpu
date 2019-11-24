from display import NumDisplay

def test_num_display():
    display = NumDisplay(4)
    display.a = [1, 0, 0, 0]
    
    display.eval()

    assert display.out == 8
