import time
import getpass
from utils import limpar_terminal
from db import criar_usuario, verificar_usuario

def cadastrar():
    while True:
        usuario = input("Nome: ")
        email = input("Email: ")
        senha = getpass.getpass("Senha: ")
        confirma_senha = getpass.getpass("Confirma senha: ")

        if senha != confirma_senha:
            print("As senhas não coincidem!")
        else:
            if criar_usuario(email, usuario, senha):
                print("Usuário criado com sucesso!")
                time.sleep(2)
                limpar_terminal()
                return
            else:
                print("Email já cadastrado!")

def login():
    while True:
        email = input("Email: ")
        senha = getpass.getpass("Senha: ")
        usuario = verificar_usuario(email, senha)

        if usuario:
            print(f"Logado com sucesso, bem vindo, {usuario}!")
            return usuario
        else:
            print("Email ou senha incorretos.")
