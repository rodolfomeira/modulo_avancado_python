"""Programa principal
usa o módulo m_exresolvido_17_1 que está no pacote cap16"""
from cap17.m_exresolvido_17_1 import Retangulo

ret = Retangulo(0,0)
s = input('Digite dois reais (base altura): ')
while s.upper() != 'FIM':
    valores = s.split()
    ret.base = float(valores[0])
    ret.altura = float(valores[1])
    ret.exibe()
    s = input('Digite dois reais (base altura): ')

print('\nFim do Programa')