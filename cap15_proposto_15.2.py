def EPrimo(n):
    """Função auxiliar que verifica se n é primo"""
    if n == 2:
        return True
    elif n < 2 or n % 2 == 0:
        return False
    else:
        i = 3;
        while i <= n ** 0.5:
            if n % i == 0:
                return False
            i += 2
        return True


def gerador_primos():
    valor = 0
    while True:
        if EPrimo(valor):
            inicial = (yield valor)
            if inicial is not None:
                valor = inicial
        valor += 1

# parte principal
gen = gerador_primos()   # cria o gerador
next(gen)          # inicializa o gerador
# permanece em laço gerando primos conforme solicitação do usuário
Qtde = int(input('Qtde de primos (0 para sair): '))
while Qtde > 0:
    Inicial = int(input('Valor inicial: '))
    Primos = []
    Primos.append(gen.send(Inicial))  # envia o Inicial e recebe o primeiro primo
    for cont in range(Qtde-1):
        Primos.append(next(gen))      # recebe os demais primos

    print(f'Os primeiros {Qtde} primos maiores que {Inicial} são:')
    print(Primos)

    Qtde = int(input('\n\nDigite a quantidade de primos: '))

print('\nFim do Programa')
