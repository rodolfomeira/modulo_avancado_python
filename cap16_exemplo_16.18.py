import pacote.utils_bool as ub
import pacote.utils_txt as ut

a = 17
print('Uso das funções do módulo utils_bool')
r = ub.primo(a)
print(f'{a} é primo? {r}')
r = ub.paridade(a)
print(f'{a} é par? {r}')

print('\nUso das funções do módulo utils_txt')
ut.primo(a)
ut.paridade(a)
