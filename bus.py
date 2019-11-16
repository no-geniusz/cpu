class Bus:

    def __init__(self, width):
        self.__width = width
        self.__elems = []
        self.line = [None for _ in range(width)]

    def add(self, register):
        self.__elems.append(register)

    def eval(self):
        for reg in self.__elems:
            for i in range(self.__width):
                reg.d[i] = self.line[i]
            reg.eval()
            for i in range(self.__width):
                if reg.q[i] != None:
                    self.line[i] = reg.q[i]

