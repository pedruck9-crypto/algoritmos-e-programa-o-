midias = []
proximo_id = 1

while True:
    print("\n=== CRUD de Filmes e Séries — Ciclo 2 ===")
    print("1 - Cadastrar mídia")
    print("2 - Listar mídias")
    print("3 - Buscar mídia por identificador")
    print("4 - Atualizar mídia")
    print("5 - Excluir mídia")
    print("0 - Sair")
    opcao = input("Escolha uma opção: ").strip()

    if opcao == "1":
        titulo = input("Título: ").strip()
        if titulo == "":
            print("O título não pode ficar vazio.")
        else:
            tipo = input("Tipo (filme/série): ").strip()
            genero = input("Gênero: ").strip()
            ano = input("Ano: ").strip()
            sinopse = input("Sinopse: ").strip()
            midia = {
                "id": proximo_id,
                "titulo": titulo,
                "tipo": tipo,
                "genero": genero,
                "ano": ano,
                "sinopse": sinopse,
            }
            midias.append(midia)
            print("Mídia cadastrada com identificador", proximo_id)
            proximo_id = proximo_id + 1
    elif opcao == "2":
        if len(midias) == 0:
            print("Nenhuma mídia cadastrada.")
        else:
            for midia in midias:
                print("\nID:", midia["id"])
                print("Título:", midia["titulo"])
                print("Tipo:", midia["tipo"])
                print("Gênero:", midia["genero"])
                print("Ano:", midia["ano"])
                print("Sinopse:", midia["sinopse"])
    elif opcao == "3":
        identificador = input("Identificador: ").strip()
        encontrada = False
        for midia in midias:
            if str(midia["id"]) == identificador:
                print("Título:", midia["titulo"])
                print("Tipo:", midia["tipo"])
                print("Gênero:", midia["genero"])
                print("Ano:", midia["ano"])
                print("Sinopse:", midia["sinopse"])
                encontrada = True
        if not encontrada:
            print("Mídia não encontrada.")
    elif opcao == "4":
        identificador = input("Identificador da mídia: ").strip()
        encontrada = False
        for midia in midias:
            if str(midia["id"]) == identificador:
                novo_titulo = input("Novo título (Enter mantém o atual): ").strip()
                novo_tipo = input("Novo tipo (Enter mantém o atual): ").strip()
                novo_genero = input("Novo gênero (Enter mantém o atual): ").strip()
                novo_ano = input("Novo ano (Enter mantém o atual): ").strip()
                nova_sinopse = input("Nova sinopse (Enter mantém a atual): ").strip()
                if novo_titulo != "":
                    midia["titulo"] = novo_titulo
                if novo_tipo != "":
                    midia["tipo"] = novo_tipo
                if novo_genero != "":
                    midia["genero"] = novo_genero
                if novo_ano != "":
                    midia["ano"] = novo_ano
                if nova_sinopse != "":
                    midia["sinopse"] = nova_sinopse
                print("Mídia atualizada.")
                encontrada = True
        if not encontrada:
            print("Mídia não encontrada.")
    elif opcao == "5":
        identificador = input("Identificador da mídia: ").strip()
        indice_encontrado = -1
        indice = 0
        while indice < len(midias):
            if str(midias[indice]["id"]) == identificador:
                indice_encontrado = indice
            indice = indice + 1
        if indice_encontrado == -1:
            print("Mídia não encontrada.")
        else:
            midias.pop(indice_encontrado)
            print("Mídia excluída.")
    elif opcao == "0":
        print("Programa encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
