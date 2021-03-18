import sqlite3

conn = sqlite3.connect('DadosUsuarios.db')

cursor = conn.cursor()

cursor.execute(
	'''CREATE TABLE IF NOT EXISTS usuarios (
			  Id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
			  Nome TEXT NOT NULL,
			  Email TEXT NOT NULL,
			  Usuario TEXT NOT NULL,
			  Senha TEXT NOT NULL			  
	);'''
	)

print('Conectado ao banco de dados')