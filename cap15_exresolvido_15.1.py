def gerador_primos():
    yield 2
    v = 3
    while True:
        raiz = v ** 0.5
        i = 3
        while i <= raiz and v % i != 0:
            i += 2
        if i > raiz:
            yield v
        v += 2

gen = gerador_primos()
Qtde = int(input('Digite a quantidade de primos: '))
for cont in range(Qtde):
    print(next(gen), end = ' ')
print('\nFim do Programa')