""" Este é módulo utilidades
Ele contém objetos e funções que podem ser úteis aos nossos programas.
É recomendável que haja um docstring indicando o conteúdo do módulo"""

texto = 'Este é o módulo utilidades.py'

meses = ['jan', 'fev', 'mar', 'abr', 'mai', 'jun',
         'jul', 'ago', 'set', 'out', 'nov', 'dez']

def paridade(valor):
    """Retorna PAR ou ÍMPAR conforme o valor passado"""
    if valor % 2 == 0:
        return 'PAR'
    else:
        return 'ÍMPAR'

def primo(valor):
    """Se valor for primo retorna True, senão retorna False"""
    if valor == 2:
        return True
    elif valor % 2 == 0:
        return False
    else:
        raiz = pow(valor, 0.5)
        i = 3
        while i <= raiz:
            if valor % i == 0:
                return False
            i += 2
        return True
