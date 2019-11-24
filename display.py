class NumDisplay:

    def __init__(self, width):
        self.__width = width
        self.a = [None] * width
        self.out = None

    def eval(self):
        bin_string = ''.join(map(lambda i: str(i), self.a))
        self.out = int(bin_string, 2)

        print(self.out)
