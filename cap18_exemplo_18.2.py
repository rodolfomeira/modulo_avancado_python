import sqlite3

conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
cursor = conector.cursor()
# exclui a tabela, caso exista
try:
    sql = "drop table produto"
    cursor.execute(sql)
    conector.commit()
except sqlite3.OperationalError:
    pass
# cria a tabela
sql = """
    create table produto
    (codigo integer not null, descr text, preco numeric, qtdeestq integer,
    primary key (codigo))        
    """                   # note a cláusula primary key que define a chave primária
cursor.execute(sql)
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