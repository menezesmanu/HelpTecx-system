import os

# Lista de produtos aceitos no sistema (tupla para manter imutável)
PRODUTOS_DISPONIVEIS = ("Celular", "Notebook", "Tablet")

# Nome do arquivo onde os chamados serão gravados
ARQUIVO_CHAMADOS = "chamados.txt"


# ----------------------------------------------------------------------
# Função que lê o arquivo e transforma cada linha em um dicionário
# ----------------------------------------------------------------------
def carregar_chamados():
    chamados = []

    # Se o arquivo não existe ainda, retorna uma lista vazia
    if not os.path.exists(ARQUIVO_CHAMADOS):
        return chamados

    # Abre o arquivo linha por linha
    with open(ARQUIVO_CHAMADOS, "r", encoding="utf-8") as arquivo:
        for linha in arquivo:
            dados = linha.strip().split("|")

            # Garante que a linha tem todos os campos necessários
            if len(dados) == 5:
                numero, cliente, produto, defeito, status = dados

                chamados.append({
                    "numero": int(numero),
                    "cliente": cliente,
                    "produto": produto,
                    "defeito": defeito,
                    "status": status
                })

    return chamados


# ----------------------------------------------------------------------
# Função que salva todos os chamados no arquivo .txt
# ----------------------------------------------------------------------
def salvar_chamados(chamados):
    with open(ARQUIVO_CHAMADOS, "w", encoding="utf-8") as arquivo:
        for c in chamados:
            linha = f"{c['numero']}|{c['cliente']}|{c['produto']}|{c['defeito']}|{c['status']}\n"
            arquivo.write(linha)


# ----------------------------------------------------------------------
# Gera o número sequencial do chamado
# ----------------------------------------------------------------------
def gerar_numero_chamado(chamados):
    if not chamados:
        return 1
    return max(c["numero"] for c in chamados) + 1


# ----------------------------------------------------------------------
# Garante que o usuário digite apenas texto (nada de números)
# ----------------------------------------------------------------------
def validar_string(msg):
    while True:
        dado = input(msg).strip()

        # remove espaços para validar
        if dado.replace(" ", "").isalpha():
            return dado

        print("Entrada inválida. Digite apenas letras.")


# ----------------------------------------------------------------------
# Garante que o produto digitado existe no sistema
# ----------------------------------------------------------------------
def validar_produto():
    while True:
        produto = input("Produto (Celular / Notebook / Tablet): ").strip().title()

        if produto in PRODUTOS_DISPONIVEIS:
            return produto

        print("Produto não encontrado no sistema.")


# ----------------------------------------------------------------------
# Garante que o usuário digite apenas números
# ----------------------------------------------------------------------
def validar_numero(msg):
    while True:
        valor = input(msg).strip()

        if valor.isdigit():
            return int(valor)

        print("Entrada inválida. Digite apenas números.")


# ----------------------------------------------------------------------
# Cria um novo chamado e adiciona à lista
# ----------------------------------------------------------------------
def criar_chamado(chamados):
    print("\n--- Criar Chamado ---")

    cliente = validar_string("Nome do cliente: ")
    produto = validar_produto()
    defeito = input("Descrição do defeito: ").strip()

    # Gera número único
    numero_chamado = gerar_numero_chamado(chamados)

    # Cria o dicionário do chamado
    chamado = {
        "numero": numero_chamado,
        "cliente": cliente,
        "produto": produto,
        "defeito": defeito,
        "status": "Aberto"
    }

    chamados.append(chamado)
    salvar_chamados(chamados)

    print(f"Chamado criado. Número do chamado: {numero_chamado}\n")


# ----------------------------------------------------------------------
# Exibe todos os chamados na tela
# ----------------------------------------------------------------------
def listar_chamados(chamados):
    print("\n--- Lista de Chamados ---")

    if not chamados:
        print("Nenhum chamado encontrado.\n")
        return

    for c in chamados:
        print(f"Número do chamado: {c['numero']}")
        print(f"Cliente: {c['cliente']}")
        print(f"Produto: {c['produto']}")
        print(f"Defeito: {c['defeito']}")
        print(f"Status: {c['status']}")
        print("-" * 30)

    print()


# ----------------------------------------------------------------------
# Cancela um chamado existente
# ----------------------------------------------------------------------
def cancelar_chamado(chamados):
    print("\n--- Cancelar Chamado ---")

    if not chamados:
        print("Não há chamados para cancelar.\n")
        return

    numero = validar_numero("Informe o número do chamado: ")

    for c in chamados:
        if c["numero"] == numero:
            c["status"] = "Cancelado"
            salvar_chamados(chamados)
            print("Chamado cancelado.\n")
            return

    print("Chamado não encontrado.\n")