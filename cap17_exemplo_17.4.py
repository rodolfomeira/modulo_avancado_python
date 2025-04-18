from cap16.m_exemplo_16_3 import Veiculo

# leitura e carga dos dados
DictV = {} # dicionário de veículos
for s in open('veiculos.txt', 'r'):
    s = s.split(';')
    v = Veiculo(
        s[0], # placa - será usada como chave para o dicionário
        s[1], # modelo
        int(s[2]), # ano
        int(s[3])  # km
    )
    DictV[s[0]] = v  # inclui o objeto v no dicionário

# apresentação dos dados na tela
for v in DictV.values():
    v.exibe()
print('\nFim do Programa')