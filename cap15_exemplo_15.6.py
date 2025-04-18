def le_arquivo(nome_arq):
    for uma_linha in open(nome_arq, "r"):
        yield uma_linha.rstrip()

arquivo = input('Digite o nome do arquivo: ')
for linha in le_arquivo(arquivo):
    print(linha)
print('\nFim do Programa')
