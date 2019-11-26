class ThreeState:
    
    def __init__(self):
        self.a = None
        self.b = None
        self.c = None

    def eval(self):
        if (self.b):
            self.c = self.a
        else:
            self.c = None

class WideThreeState:

    def __init__(self, width):
        self.__width = width

        self.a = [None] * width
        self.b = None
        self.c = [None] * width

        self.__three_state = [ThreeState() for _ in range(width)]

    def eval(self):
        for k in range(self.__width):
            three_state = self.__three_state[k]
            three_state.a = self.a[k]
            three_state.b = self.b
            three_state.eval()
            self.c[k] = three_state.c
