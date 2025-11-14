from funcoes import (
    carregar_chamados,
    criar_chamado,
    listar_chamados,
    cancelar_chamado
)

# Menu principal do sistema
def menu():
    chamados = carregar_chamados()  # Carrega chamados do arquivo

    while True:
        print("=== Help Tecx ===")
        print("1 - Criar chamado")
        print("2 - Listar chamados")
        print("3 - Cancelar chamado")
        print("4 - Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            criar_chamado(chamados)

        elif opcao == "2":
            listar_chamados(chamados)

        elif opcao == "3":
            cancelar_chamado(chamados)

        elif opcao == "4":
            print("Encerrando o sistema.")
            break

        else:
            print("Opção inválida. Tente novamente.\n")


# Ponto de entrada do programa
if __name__ == "__main__":
    menu()