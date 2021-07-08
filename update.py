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

# vsql = """INSERT INTO usuarios
#(Nome, email, usuario, senha)
# VALUES ('Andre','andre@gmail.com','andre2021')"""


def inserir(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
        print("Registro inserido com sucesso!")
    except Error as e:
        print(e)


#inserir(vcon, vsql)

# DELETAR
def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)
    finally:
        print("Registro Apagado")


vsql = "DELETE FROM tb_usuarios WHERE Nome"
deletar(vcon, vsql)


# Update
def atualizar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except Error as e:
        print(e)
    finally:
        print("Registro Atualizado")


vsql = "UPDATE FROM tb_usuarios SET Nome='Bruno' WHERE Nome"
atualizar(vcon, vsql)
