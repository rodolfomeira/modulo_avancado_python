class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    @property  # getter
    def base(self):
        return self._base

    @base.setter
    def base(self, valor):
        if not isinstance(valor, int | float):
            raise TypeError('Valor numérico esperado.')
        if valor <= 0:
            raise ValueError('Valor positivo esperado.')
        self._base = valor

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        print(f'retângulo ({self.base} x {self.altura})')
        print(f'  área = {self.calc_area():.3f}')
