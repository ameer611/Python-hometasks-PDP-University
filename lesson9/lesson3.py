class YuzVaPerimetriniTopish:
    def __init__(self, a, b):
        self.a = a
        self.b = b
        self.c = ((a**2)+(b**2))**0.5
    def parametr(self):
        return self.a+self.b+self.c
    def yuza(self):
        return (self.a*self.b)/2
    def __str__(self):
        return f"yuzi: {self.yuza()}, parametr: {self.parametr()}"

uchburchak = YuzVaPerimetriniTopish(4, 3)
print(uchburchak)