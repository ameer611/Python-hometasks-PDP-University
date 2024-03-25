class UchXonaliSon:
    def __init__(self, a):
        self.a = a
        self.aBirlik = a%10
        self.aOnlik = a//10%10
        self.aYuzlik = a//100

    def yigindi(self):
        return self.aBirlik+self.aOnlik+self.aYuzlik

    