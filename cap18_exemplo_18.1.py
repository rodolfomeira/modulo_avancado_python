import sqlite3

conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
# Criação da tabela
cursor = conector.cursor()
sql = """
    create table produto
    (codigo integer, descr text, preco numeric, qtdeestq integer)
    """
cursor.execute(sql)
# inserção de alguns dados
sql = """
    insert into produto (codigo, descr, preco, qtdeestq)
    values (1138, 'lápis preto', 1.90, 376)
"""
cursor.execute(sql)
sql = """
    insert into produto (codigo, descr, preco, qtdeestq)
    values (1138, 'papel sulfite A4 100fls', 7.25, 188)
"""
cursor.execute(sql)

conector.commit() # salva a tabela e os dados no disco

cursor.close()
conector.close()
print('\nFim do Programa')
