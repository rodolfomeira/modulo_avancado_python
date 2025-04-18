def Paridade(pValor: int) -> str:
    if type(pValor) != int:
        raise TypeError('A função paridade deve receber um int')
    if pValor % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

n = input('Digite algo: ')
r = Paridade(n)
print(f'{n} é {r}')