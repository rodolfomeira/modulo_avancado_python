def soma(*args):
    r = 0
    for x in args:
        r = r + x
    return r

def multi(*args):
    r = 1
    for x in args:
        r = r * x
    return r

print('Início do módulo')