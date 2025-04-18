def Primo(V):
    '''V deve ser um inteiro maior ou igual a 2.
       Se V for primo retorna True, senão retorna False'''
    if type(V) != int:
        raise TypeError('Tipo incorreto. V deve ser <int>')
    if V < 2:
        raise ValueError('Valor inválido. V deve ser maior que 1')
    if V == 2:        # V é ímpar
        return True
    elif V % 2 == 0:  # V é par maior que 2
        return False
    else:             # testa se V ímpar é primo
        raiz = pow(V, 0.5) # a raiz de V é o limite dos testes necessários
        i = 3
        while i <= raiz:
            if V % i == 0:
                return False # se for divisível retorna falso imediatamente
            i += 2
        return True # se chegar no final do laço então é primo

N = int(input('Digite um inteiro: '))
if Primo(N):
    print(f'{N} é primo')
else:
    print(f'{N} não é primo')
