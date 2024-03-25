class Car:
    def __int__(self, model, year, color):
        self.model = model
        self.year = year
        self.color = color

    def __str__(self):
        return f'model:{self.model}, year: {self.year}, color: {self.color}'



        