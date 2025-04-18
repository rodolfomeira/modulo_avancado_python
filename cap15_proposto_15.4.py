def gerador_fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

gen = gerador_fibonacci()
Qtde = int(input('Digite a quantidade de termos: '))
for _ in range(Qtde):
    print(next(gen), end = ' ')
print('\n\nFim do Programa')