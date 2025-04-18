"""Programa principal
usa o módulo m_exresolvido_16_2 que está no pacote cap16"""
from cap17.m_exresolvido_17_2 import Retangulo

ret = Retangulo(0,0)
s = input('\nDigite dois reais (base altura): ')
while s.upper() != 'FIM':
    valores = s.split()
    try:
        ret.base = float(valores[0])
        ret.altura = float(valores[1])
        ret.exibe()
    except ValueError as e:
        print(f'Erro! {e}')
    s = input('Digite dois reais (base altura): ')

print('\nFim do Programa')
