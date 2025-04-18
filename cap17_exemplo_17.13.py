class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    @property
    def base(self):
        return self._base
    @base.setter
    def base(self, valor):
        if not isinstance(valor, int | float) or valor <= 0:
            raise ValueError('Número positivo esperado')
        self._base = valor

    def calc_area(self) -> float:
        return self.base * self.altura

    def exibe(self) -> None:
        print(f'retângulo {self.base} x {self.altura}')
        print(f'  área = {self.calc_area()}')

# criação de um objeto correto
r1 = Retangulo(10, 5)
r1.exibe()
r1.base = 9
r1.exibe()
r1

# criação de um objeto com base negativa
r2 = Retangulo(-10, 5)
r2.exibe()
