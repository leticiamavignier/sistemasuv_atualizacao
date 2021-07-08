import sqlite3
from sqlite3 import Error

# Criando conexão


def ConexaoBanco():
    caminho = r"C:/Users/seuip/AppData/Local/Programs/Python/Python39/Prática Profissional - Uninassau/SistemaSUV/bancoConexão.db"
    conn = None
    try:
        conn = sqlite3.connect(caminho)
    except Error as e:
        print(e)
    return conn


vcon = ConexaoBanco()

# Criando tabela
vsql = """CREATE TABLE usuarios(
            Nome VARCHAR (30),
            email VARCHAR (14),
            usuario VARCHAR (30)
        );"""


def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        print("Tabela Criada - CREATE OK")
    except Error as ex:
        print(ex)


criarTabela(vcon, vsql)

vcon.close()
