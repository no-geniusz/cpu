class Bus:

    def __init__(self, width):
        self.__width = width
        self.line = [None for _ in range(width)]

    def apply(self, signals):
        for k in range(self.__width):
            if signals[k] != None:
                self.line[k] = signals[k]
