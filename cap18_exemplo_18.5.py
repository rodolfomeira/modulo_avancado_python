import sqlite3

conector = sqlite3.connect('C:\\CursoPython\\cap18\\loja.db')
cursor = conector.cursor()
# insere os novos campos
sql = "alter table produto add custo numeric"
cursor.execute(sql)
sql = "alter table produto add aliqicms numeric"
cursor.execute(sql)
sql = "alter table produto add qtdemin integer"
cursor.execute(sql)
# atribui 0 aos novos campos
sql = "update produto set custo = 0, aliqicms = 0, qtdemin = 0"
cursor.execute(sql)
conector.commit()
print('Os três campos foram inseridos e inicializados com zero')
cursor.close()
conector.close()