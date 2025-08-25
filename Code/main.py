import time
from auth import login, cadastrar
from utils import limpar_terminal

def inicio():
    while True:
        print("---------------")
        print("# 1 - Login\n# 2 - Cadastrar\n# 3 - Sair")
        print("---------------")
        opcao = int(input("Opção: "))

        if opcao == 1:
            usuario = login()
            if usuario:
                break
        elif opcao == 2:
            cadastrar()
        elif opcao == 3:
            print("Saindo...")
            break
        else:
            print("Essa opção não existe, por favor selecione outra")
            limpar_terminal()

if __name__ == "__main__":
    inicio()
