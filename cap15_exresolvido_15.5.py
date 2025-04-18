def gera_permutacoes(texto):
    if len(texto) <= 1:
        yield texto
    else:
        for i in range(len(texto)):
            caractere_atual = texto[i]
            demais_caracteres = texto[:i] + texto[i+1:]
            for permutacao in gera_permutacoes(demais_caracteres):
                yield caractere_atual + permutacao

lista = input('Digite um texto: ')
for l in gera_permutacoes(lista):
    print(l)
print('\nFim do Programa')