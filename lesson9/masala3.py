import math


class YuzVaUzunlik:
    def __init__(self, r):
        self.r = r
        self.uzunlik = 2*math.pi*r
        self.yuza = math.pi*r**2

    def yuza(self):
        return self.yuza
    def uzunlik(self):
        return self.uzunlik

    def __str__(self):
        return f'yuza: {self.yuza}, uzunlik: {self.uzunlik}'

aylana = YuzVaUzunlik(1)
print(aylana)