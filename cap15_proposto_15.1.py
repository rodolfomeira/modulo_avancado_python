def gerador_primos():
    p = [2]
    yield 2
    v = 3
    while True:
        raiz = v ** 0.5
        i = 0
        naoPrimo = False
        while i < len(p) and p[i] <= raiz:
            if v % p[i] == 0:
                naoPrimo = True
            i += 1
        if not naoPrimo:
            p.append(v)
            yield v
        v += 2

gen = gerador_primos()
Qtde = int(input('Digite a quantidade de primos: '))
primos = []
for _ in range(Qtde):
    primos.append(next(gen))
print(primos)
print('\nFim do Programa')