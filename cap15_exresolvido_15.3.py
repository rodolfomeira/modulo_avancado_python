def funcao_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat)
        num += 1
        fat *= num
        if i is not None:
            num, fat = i, 1
            for a in range(1, num+1):
                fat *= a

qtde = int(input('Digite a quantidade de fatoriais: '))
gen = funcao_fatorial()
next(gen)

prim = int(input('\nDigite valor inicial para a próxima sequência: '))
while prim >= 0:
    r = gen.send(prim)
    fatoriais  = [r]
    for _ in range(qtde-1):
        fatoriais .append(next(gen))
    print(f'Sequência de fatoriais iniciando em {prim}!')
    print(fatoriais )

    prim = int(input('\nDigite valor inicial para a próxima sequência: '))
print('\nFim do Programa')
