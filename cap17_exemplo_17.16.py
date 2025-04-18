class NumeroPositivo:
    def __set_name__(self, owner, name):
        self._name = name
        
    def __get__(self, obj, objtype=None):
        return obj.__dict__[self._name]
    
    def __set__(self, obj, value):
        if not isinstance(value, int | float) or value <= 0:
            raise ValueError('Número positivo esperado')
        obj.__dict__[self._name] = value


class Retangulo:
    base = NumeroPositivo()
    altura = NumeroPositivo()
    
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura

    def calc_area(self):
        return self.base * self.altura

    def exibe(self):
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
