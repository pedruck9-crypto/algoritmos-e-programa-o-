titulo = ""
tipo = ""
genero = ""
ano = ""
sinopse = ""
cadastrada = False

while True:
    print("\n=== CRUD de Filmes e Séries — Ciclo 1 ===")
    print("1 - Cadastrar mídia")
    print("2 - Consultar mídia")
    print("3 - Atualizar mídia")
    print("4 - Excluir mídia")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        if cadastrada:
            print("Já existe uma mídia cadastrada. Exclua-a antes de cadastrar outra.")
        else:
            novo_titulo = input("Título: ").strip()
            if novo_titulo == "":
                print("O título não pode ficar vazio.")
            else:
                titulo = novo_titulo
                tipo = input("Tipo (filme/série): ").strip()
                genero = input("Gênero: ").strip()
                ano = input("Ano: ").strip()
                sinopse = input("Sinopse: ").strip()
                cadastrada = True
                print("Mídia cadastrada com identificador 1.")
    elif opcao == "2":
        if cadastrada:
            print("\nIdentificador: 1")
            print("Título:", titulo)
            print("Tipo:", tipo)
            print("Gênero:", genero)
            print("Ano:", ano)
            print("Sinopse:", sinopse)
        else:
            print("Nenhuma mídia cadastrada.")
    elif opcao == "3":
        if cadastrada:
            identificador = input("Identificador da mídia (1): ").strip()
            if identificador == "1":
                novo_titulo = input("Novo título (Enter mantém o atual): ").strip()
                novo_tipo = input("Novo tipo (Enter mantém o atual): ").strip()
                novo_genero = input("Novo gênero (Enter mantém o atual): ").strip()
                novo_ano = input("Novo ano (Enter mantém o atual): ").strip()
                nova_sinopse = input("Nova sinopse (Enter mantém a atual): ").strip()
                if novo_titulo != "":
                    titulo = novo_titulo
                if novo_tipo != "":
                    tipo = novo_tipo
                if novo_genero != "":
                    genero = novo_genero
                if novo_ano != "":
                    ano = novo_ano
                if nova_sinopse != "":
                    sinopse = nova_sinopse
                print("Mídia atualizada.")
            else:
                print("Identificador não encontrado.")
        else:
            print("Nenhuma mídia cadastrada.")
    elif opcao == "4":
        if cadastrada:
            identificador = input("Identificador da mídia (1): ").strip()
            if identificador == "1":
                cadastrada = False
                titulo = ""
                tipo = ""
                genero = ""
                ano = ""
                sinopse = ""
                print("Mídia excluída.")
            else:
                print("Identificador não encontrado.")
        else:
            print("Nenhuma mídia cadastrada.")
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
