def AoQuadrado(dados):
    if not isinstance(dados, list) and not isinstance(dados, tuple):
        raise TypeError(f'Lista ou Tupla esperados e você usou {type(dados)}')
    if not all(isinstance(x, int) or isinstance(x, float) for x in dados):
        raise ValueError(f'Os elementos de dados devem ser numéricos')
    return [v**2 for v in dados]

