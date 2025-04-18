def funcao_fatorial():
    num, fat = 0, 1
    while True:
        i = (yield num, fat)
        num += 1
        fat *= num
        if i is not None:
            if i < 0:
                raise ValueError(f'Erro! Esperado um número natural. Fornecido {i}.')
            num, fat = i, 1
            for a in range(1, num+1):
                fat *= a

qtde = int(input('Digite a quantidade de fatoriais: '))
gen = funcao_fatorial()
next(gen)

fim = False
while not fim:
    entrada = input('\nDigite o valor inicial ou "fim" para sair: ')
    if entrada.upper() == 'FIM':
        fim = True
    else:
        prim = int(entrada)
        r = gen.send(prim)
        fat = [r]
        for _ in range(qtde-1):
            fat.append(next(gen))
        print(f'Sequência de fatoriais iniciando em {prim}!')
        print(fat)

print('\nFim do Programa')
