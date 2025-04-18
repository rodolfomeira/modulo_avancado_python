class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        print(f'retângulo ({self.base} x {self.altura})')
        print(f'  área = {self.calc_area():.3f}')