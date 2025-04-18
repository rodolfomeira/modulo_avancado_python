# módulo m_exresolvido_16_2.py
class Retangulo:
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
        if self.base <= 0:
            raise ValueError('Base: valor numérico maior que zero esperado')
        if self.altura <= 0:
            raise ValueError('Altura: valor numérico maior que zero esperado')
        print(f'retângulo {self.base} x {self.altura}')
        print(f'  área = {self.calc_area():.3f}')
