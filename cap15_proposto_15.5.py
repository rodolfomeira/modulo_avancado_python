def gerador_collatz(n):
    while n != 1:
        yield n
        if n % 2 == 0:
            n = n // 2
        else:
            n = 3 * n + 1
    yield 1

N = int(input('Digite um inteiro positivo: '))
print('Sequência de Collatz')
for elemento in gerador_collatz(N):
    print(elemento, end="  ")

print('\n\nFim do Programa')