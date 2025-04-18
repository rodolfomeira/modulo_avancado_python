import utilidades

x = int(input('Digite um inteiro: '))
while x != 0:
    parid = utilidades.paridade(x) # chamada à função do módulo utilidades
    xPrimo = utilidades.primo(x)   # chamada à função do módulo utilidades
    print(f'{x} é {parid}')
    if xPrimo:
        print(f'{x} é primo')
    else:
        print(f'{x} não é primo')
    x = int(input('Digite um inteiro: '))

print('\nFim do Programa')
