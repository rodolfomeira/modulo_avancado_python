def fg():
    resto = 0
    num = 2
    while True:
        if num % 2 == resto:  # resto calculado é comparado com o objeto resto
            dado = (yield num)
            if dado is not None:
                if dado in (0, 1):
                    resto = dado  # troca o valor de resto
                    num = 0  # reseta o valor de num
                else:
                    raise ValueError(f'Esperado argumento 0 ou 1 - passado {dado}')
        num += 1

gen = fg()
print('Gera 5 pares')
for i in range(5):
    print(next(gen))

print('\nGera 5 ímpares')
ret = gen.send(1)  # este método retorna o 1º valor da sequência
print(ret)
for i in range(4): # então precisamos gerar o próximos 4
    print(next(gen))

# tentativa de usar send com valor diferente de 0 ou 1
print('\nParâmetro incorreto')
ret = gen.send(2)  # causa um loop infinito

print('\nFim do Programa')
