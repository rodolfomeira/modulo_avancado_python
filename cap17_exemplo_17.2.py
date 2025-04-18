class Retangulo:
    def __init__(self, base: float, altura: float):
        self.base = base
        self.altura = altura

    def calc_area(self) -> float:
        return self.base * self.altura

    def exibe(self) -> None:
        print(f'retângulo {self.base} x {self.altura}')
        print(f'  área = {self.calc_area()}')

print('Início do programa principal')
r1 = Retangulo(12, 5)
print('r1: ', end='')
r1.exibe()
print('r2: ', end='')
r2 = Retangulo(3.5, 9.0)
r2.exibe()

r2.base = 9.5     # alteração no atributo base de r2
r2.altura = 16.3  # alteração no atributo altura de r2
print('\nAcessos individuais a atributos e métodos')
print(f'Medidas do retângulo r2: {r2.base} x {r2.altura}')
area = r2.calc_area()
print(f'Área do retângulo r2 = {area:.3f}')
