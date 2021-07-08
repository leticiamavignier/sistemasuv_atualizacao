import sqlite3
# Gerando a conexão com o Banco de Dados
conn = sqlite3.connect('UsuarioData.db')

cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
    Nome TEXT,
    email TEXT,
    usuario TEXT,
    senha INTEGER
);
""")

#cursor.execute( "CREATE TABLE usuarios (nome text, email text, usuario text, senha integer)")

#cursor.execute( "INSERT INTO usuarios VALUES ('Ana', 'ana@gmail.com', 'ana2021', '1234')")

# conn.commit()

#cursor.execute("SELECT *FROM usuarios")
# print(cursor.fetchall())

print("Conectado ao Banco de Dados")
