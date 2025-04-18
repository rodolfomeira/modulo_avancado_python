import sqlite3

conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
cursor = conector.cursor()
sql = """
    insert into produto (codigo, descr, preco, qtdeestq)
    values(?, ?, ?, ?)
    """
print('Digite os dados separados por vírgulas')
print('Codigo,Descrição,Preço,Estoque')
Ler = input()
while Ler != '':
    try:
        dados = Ler.split(',')
        print(dados)
        cursor.execute(sql, dados)
        conector.commit()
    except sqlite3.OperationalError as e:
        print(e.sqlite_errorname)
        print('{} Dados inválidos'.format(dados))
    else:
        print(' '*10, '...dados inseridos com sucesso')
    finally:
        print('\nCodigo,Descrição,Preço,Estoque')
    Ler = input()

cursor.close()
conector.close()