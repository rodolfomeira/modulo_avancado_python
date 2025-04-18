import sqlite3
conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
cursor = conector.cursor()
sql = "select * from produto"
cursor.execute(sql)
dados = cursor.fetchall()
cursor.close()
conector.close()

print('\nConsulta ao Banco de Dados "loja.db" \n')
print('Dados da tabela "produto"')
print("-" * 79)
print("{:7}{:40}{:>7}{:>6}{:>7}{:>6}{:>6}".format('Código', 'Descrição', 'Preço', 'Estq', 'Custo', 'Aliq.', 'qMin'))
print("- " * 40)
for d in dados:
    print("{:<7}{:40}{:7.2f}{:6}{:7.2f}{:6}{:6}".format(d[0], d[1], d[2], d[3], d[4], d[5], d[6]))
print("-" * 79)
print("Encontrados {} registros".format(len(dados)))
print("\nFim do programa")
