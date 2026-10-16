# Exemplos de operações com listas (pão, queijo, presunto)
# Arquivo de demonstração: mostra uso de list comprehension, slicing, pop(i), index, count, sum, len, min, max,
# reverse, sorted, list.sort(), atribuição por fatia, e checagem "x in lista".

# lista inicial (contém duplicatas de "queijo" para demonstrar count/index)
ingredientes = ["pão", "queijo", "presunto", "alface", "tomate", "queijo"]

print("Lista inicial:", ingredientes)

# Acessar por índice
print("\ningredientes[0]:", ingredientes[0])  # primeiro item

# 'x in lista' verifica presença
print("\n'queijo' in ingredientes:", "queijo" in ingredientes)
print("'manteiga' in ingredientes:", "manteiga" in ingredientes)

# index(x) retorna o índice da primeira ocorrência (lança ValueError se não existir)
if "queijo" in ingredientes:
    print("\nPrimeiro índice de 'queijo':", ingredientes.index("queijo"))

# count(x) conta quantas vezes aparece
print("\nQuantidade de 'queijo':", ingredientes.count("queijo"))

# len() tamanho da lista
print("\nTamanho da lista:", len(ingredientes))

# Slicing: [inicio:fim:passo]
print("\nSlicing exemplos:")
print("ingredientes[1:4]  ->", ingredientes[1:4])   # índices 1,2,3
print("ingredientes[:3]   ->", ingredientes[:3])    # primeiros 3
print("ingredientes[3:]   ->", ingredientes[3:])    # a partir do índice 3
print("ingredientes[-2:]  ->", ingredientes[-2:])   # últimos 2
print("ingredientes[::-1] ->", ingredientes[::-1])  # invertida (cria nova lista)

# List comprehension: transformar / filtrar
print("\nList comprehension exemplos:")
maiusculas = [x.upper() for x in ingredientes]
print("Maiúsculas:", maiusculas)
sem_tomate = [x for x in ingredientes if x != "tomate"]
print("Sem tomate:", sem_tomate)

# Atribuição por fatia: mantém o mesmo objeto lista, mas substitui conteúdo
# útil quando outras referências dependem da mesma lista
print("\nAtribuição por fatia (remover todas as ocorrências de 'queijo'):")
antes = ingredientes[:]  # cópia para comparação
ingredientes[:] = [m for m in ingredientes if m != "queijo"]
print("antes:", antes)
print("depois:", ingredientes)

# Recria lista para demonstrar pop/index/remoção por índice
ingredientes = ["pão", "queijo", "presunto", "alface", "tomate", "queijo"]
print("\nReconstruída para demos:", ingredientes)

# Encontrar índice e usar pop(i) para remover por posição (retorna o elemento removido)
# exemplo: remover a primeira ocorrência de 'presunto' por índice
if "presunto" in ingredientes:
    idx_presunto = ingredientes.index("presunto")
    removido = ingredientes.pop(idx_presunto)  # pop por índice
    print("\npop(idx): removeu:", removido)
    print("Lista após pop:", ingredientes)
else:
    print("\n'presunto' não encontrado para pop.")

# pop() sem argumento remove e retorna o último item
ultimo = ingredientes.pop()
print("\npop() sem argumento removeu o último elemento:", ultimo)
print("Lista agora:", ingredientes)

# remove(x) remove a primeira ocorrência do valor x (já mostrado antes)
ingredientes.append("queijo")
print("\nAdicionado 'queijo' de volta:", ingredientes)
ingredientes.remove("queijo")
print("remove('queijo') removeu a primeira ocorrência:", ingredientes)

# Operações numéricas em listas numéricas: sum, min, max
numeros = [10, 3, 7, 1, 9]
print("\nLista numérica:", numeros)
print("sum(numeros):", sum(numeros))
print("min(numeros):", min(numeros))
print("max(numeros):", max(numeros))
print("len(numeros):", len(numeros))

# reverse() modifica a lista in-place (não retorna)
nums_copy = numeros[:]  # cópia
nums_copy.reverse()
print("\nreverse() in-place:", nums_copy, "(original permanece):", numeros)

# sorted(lista) retorna nova lista ordenada; list.sort() ordena in-place e retorna None
sorted_nova = sorted(numeros)
print("\nsorted(numeros) (nova lista ordenada):", sorted_nova)
print("numeros ainda:", numeros)

numeros.sort()
print("numeros.sort() (ordenado in-place):", numeros)

# Exemplos adicionais: usar enumerate para obter índice e valor simultaneamente
print("\nEnumerate exemplo (índice, valor):")
for i, v in enumerate(numeros):
    print(i, v)

# Filtrar com list comprehension e atribuição por fatia para manter referência
ingredientes = ["pão", "queijo", "presunto", "alface", "tomate"]
print("\nantes da filtragem por fatia:", ingredientes)
ingredientes[:] = [x for x in ingredientes if len(x) > 4]  # mantém apenas palavras com >4 letras
print("depois (mantém itens com len>4):", ingredientes)

# Observações finais impressas
print("\nObservações:")
print("- list comprehension é concisa e frequentemente mais rápida que loops explícitos.")
print("- slicing cria cópias (ex.: lista[::]) a menos que atribua por fatia lista[:]=...")
print("- pop(i) e remove(x) são úteis dependendo se você tem índice ou valor.")
print("- sorted() vs list.sort(): sorted cria nova lista; list.sort() modifica a original.")
