class Radius:
    def __init__(self, s):
        self.s = s
        self.r = (s/3.14)**0.5

    def radius(self):
        return self.r