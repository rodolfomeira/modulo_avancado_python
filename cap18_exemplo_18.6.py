import sqlite3

conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
cursor = conector.cursor()
sql = """
    update produto 
      set custo = ?, aliqicms = ?, qtdemin = ?
      where codigo = ?
    """
nome_arq = 'C:\\CursoPython\\cap18\\papelaria_atualiz.txt'
for linha_arq in open(nome_arq, encoding='utf-8'):
    dados = linha_arq.rstrip().split(';')
    dados.append(dados[0]) # coloca o código no final da lista
    del(dados[0]) # elimina o código do início da lista
    print(dados)
    cursor.execute(sql, dados)
conector.commit()
print('A tabela produto foi atualizada')
cursor.close()
conector.close()