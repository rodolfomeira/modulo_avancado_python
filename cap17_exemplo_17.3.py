from cap16.m_exemplo_16_3 import Veiculo

# leitura e carga dos dados
LstV = [] # lista de veículos
for s in open('veiculos.txt', 'r'):
    s = s.split(';')
    v = Veiculo(
        s[0], # placa
        s[1], # modelo
        int(s[2]), # ano
        int(s[3])  # km
    )
    LstV.append(v)  # inclui o objeto v na lista

# apresentação dos dados na tela
for v in LstV:
    v.exibe()
print('\nFim do Programa')