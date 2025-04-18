import sqlite3

conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
cursor = conector.cursor()
try: # tenta criar a tabela
    sql = """
        create table produto
        (codigo integer, descr text, preco decimal, qtdeestq integer)
        """
    cursor.execute(sql)
except sqlite3.OperationalError: # se a tabela já existe elimina seu conteúdo
    sql = """delete from produto"""
    cursor.execute(sql)
conector.commit()

sql = """
    insert into produto (codigo, descr, preco, qtdeestq)
    values(?, ?, ?, ?)
    """
nome_arq = 'C:\\CursoPython\\cap18\\papelaria.txt'
for linha_arq in open(nome_arq, encoding='utf-8'):
    dados = linha_arq.rstrip().split(';')
    print(dados)
    cursor.execute(sql, dados)
conector.commit()
cursor.close()
conector.close()
print('\nFim do Programa')