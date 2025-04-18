import random
def gerador_aleatorio(ini, fim):
    while True:
        yield random.randint(ini, fim)

# Programa principal
inicio = int(input('Digite o início da faixa: '))
final = int(input('Digite o final da faixa: '))
qtde = int(input('Digite quantos valores quer gerar: '))
# Cria o gerador
gen = gerador_aleatorio(inicio, final)
for _ in range(qtde):
    print(next(gen), end='  ')

print('\n\nFim do Programa')

