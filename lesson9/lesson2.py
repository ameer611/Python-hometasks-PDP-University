class Calc:
    def __init__(self, son1, son2):
        self.son1 = son1
        self.son2 = son2

    def qushish(self):
        return self.son1+self.son2
    def ayrish(self):
        return self.son1-self.son2
    def kupaytirish(self):
        return self.son1*self.son2
    def bulish(self):
        return self.son1/self.son2

son = Calc(25, 5)
print(son.ayrish())