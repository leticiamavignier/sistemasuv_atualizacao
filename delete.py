import sqlite3
from sqlite3 import Error

# Criando conexão


def ConexaoBanco(caminho):
    caminho = r"C:\\Users\seuip\AppData\Local\Programs\Python\Python39\Prática Profissional - Uninassau\SistemaSUV\bancoConexão.db"
    con = None
    try:
        con = sqlite3.connect(caminho)
    except getopt.GetoptError as ex:
        print(ex)
    return con


# Deletar
vcon = ConexaoBanco()


def deletar(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()
    except getopt.GetoptError as ex:
        print(ex)
    finally:
        print("Registro deletado!")


deletar(vcon, vsql)
