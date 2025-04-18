import os

def lista_arqs(pcaminho):
    for raiz, pastas, arquivos in os.walk(pcaminho):
        for arq in arquivos:
            yield os.path.join(raiz, arq)

caminho = input('Digite o caminho: ')
for nomearquivo in lista_arqs(caminho):
    print(nomearquivo)