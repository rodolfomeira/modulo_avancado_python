import pacote.utils_bool
import pacote.utils_txt

a = 17
print('Uso das funções do módulo utils_bool')
r = pacote.utils_bool.primo(a)
print(f'{a} é primo? {r}')
r = pacote.utils_bool.paridade(a)
print(f'{a} é par? {r}')

print('\nUso das funções do módulo utils_txt')
pacote.utils_txt.primo(a)
pacote.utils_txt.paridade(a)
