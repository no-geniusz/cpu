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
