""" Este é módulo utils_bool
Ele contém objetos e funções que podem ser úteis aos nossos programas.
É recomendável que haja um docstring indicando o conteúdo do módulo"""

texto = 'Neste módulo as funções retornam um booleano'

def paridade(valor):
    """Se valor for par retorna True, senão retorna False"""
    if valor % 2 == 0:
        return True
    else:
        return False

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