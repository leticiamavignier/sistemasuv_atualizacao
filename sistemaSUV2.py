from tkinter import ttk
from tkinter import messagebox
from tkinter import *
import sys
import DataBase
import os
sys.path.insert(
    0, r"C:\\Users\seuip\AppData\Local\Programs\Python\Python39\Prática Profissional - Uninassau\SistemaSUV")


sistemasuv = Tk()
# Propriedades tela do sistema
sistemasuv.title("Sistema SUV - Salve Uma Vida")
sistemasuv.geometry("600x300")
sistemasuv.configure(background="gray98", relief="raise")
sistemasuv.resizable(width=False, height=False)
# Transparencia da tela
sistemasuv.attributes("-alpha", 0.9)
sistemasuv.iconbitmap(default="ICONE\Icone.ico")


# Detalhes da tela esquerda
LeftFrame = Frame(sistemasuv, width=200, height=300,
                  background="sienna1", relief="raise")
LeftFrame.pack(side="left")

logo = PhotoImage(file="amor.png")
LogoLabel = Label(LeftFrame, image=logo, background="gray98")
LogoLabel.place(x=50, y=100)

# Detalhes da tela direita
RightFrame = Frame(sistemasuv, width=395, height=300,
                   background="navy", relief="raise")
RightFrame.pack(side="right")

# Textos lado esquerdo
textocadastro = Label(sistemasuv, text="Faça o seu cadastro", font=(
    "Century Gothic bold", 11),
    background="sienna1", foreground="#000")
textocadastro.place(x=10, y=10, width=160, height=20)

obs = Label(sistemasuv, text="Use o sistema para o bem", font=(
    "Century Gothic bold", 9),
    background="sienna1", foreground="#000")
obs.place(x=10, y=35, width=160, height=20)

# Informações da tela direita
# Acesso ao sistema SUV
# Eixo Y é ALTURA
usuarioLabel = Label(RightFrame, text="Usuário: ", font=(
    "Century Gothic", 18), background="navy", foreground="white")
usuarioLabel.place(x=15, y=100)

usuarioEntry = ttk.Entry(RightFrame, width=30)
usuarioEntry.place(x=150, y=110)

senhaLabel = Label(RightFrame, text="Senha:", font=(
    "Century Gothic", 18), background="navy", foreground="white")
senhaLabel.place(x=15, y=150)

senhaEntry = ttk.Entry(RightFrame, width=30, show="*")
senhaEntry.place(x=150, y=160)


def acesso():
    Usuario = usuarioEntry.get()
    Senha = senhaEntry.get()

    DataBase.cursor.execute("""
    SELECT * FROM usuarios
    WHERE (User =? and Senha=?)
    """), (Usuario, Senha))
        print("Acesso concedido!")

        # Botões da tela direita
# Botão de registro do usuário
acessoButton=ttk.Button(
    RightFrame, text = "Acesso ao Sistema", width = 30, command = acesso)
acessoButton.place(x = 100, y = 225)


def Registro():
    # Escondendo botão de login
    acessoButton.place(x = 5000)
    registroButton.place(x = 5000)

    # Inserindo botões de cadastro
    NomeLabel=Label(RightFrame, text = "Nome:", font = (
        "Century Gothic", 18), bg = "navy", fg = "white")
    NomeLabel.place(x = 5, y = 5)

    NomeEntry=ttk.Entry(RightFrame, width = 38)
    NomeEntry.place(x = 100, y = 16)

    EmailLabel=Label(RightFrame, text = "Email:", font = (
        "Century Gothic", 18), bg = "navy", fg = "white")
    EmailLabel.place(x = 5, y = 55)

    EmailEntry=ttk.Entry(RightFrame, width = 38)
    EmailEntry.place(x = 100, y = 65)

    def registrobanco():
        Nome=NomeEntry.get()
        email=EmailEntry.get()
        usuario=usuarioEntry.get()
        senha=senhaEntry.get()
        if (Nome == "" and email == "" and usuario == "" and senha == ""):
            messagebox.showerror(title = "Registro com erro",
                                 message = "Preencha todos os campos")
        else:

            DataBase.cursor.execute("""
            INSERT INTO usuarios (Nome, email, usuario, senha) VALUES(?, ?, ?, ?)
            """, (Nome, email, usuario, senha))
            DataBase.conn.commit()
            messagebox.showinfo(
                title="Registro", message="Cadastrado com sucesso!")

    Registro = ttk.Button(RightFrame, text="Registro",
                          width=30, command=registrobanco)
    Registro.place(x=100, y=225)

    def voltarlogin():
        # Escondendo botões
        NomeLabel.place(x=5000)
        NomeEntry.place(x=5000)
        EmailLabel.place(x=5000)
        EmailEntry.place(x=5000)
        Registro.place(x=5000)
        voltar.place(x=5000)
        # Mostrando Botões
        acessoButton.place(x=100)
        registroButton.place(x=125)

    voltar = ttk.Button(RightFrame, text="Voltar",
                        width=20, command=voltarlogin)
    voltar.place(x=125, y=260)


registroButton = ttk.Button(
    RightFrame, text="Registre-se", width=20, command=Registro)
registroButton.place(x=125, y=260)


# Executa o programa
sistemasuv.mainloop()
