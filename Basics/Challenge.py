leitor = input("Nome do leitor: ").strip()
leitor = " ".join(leitor.split())

livro = input("Título do livro: ").strip()
livro = " ".join(livro.split())

total_paginas = int(input("Total de páginas: "))
paginas_lidas = int(input("Total de páginas lidas: "))
meta = int(input("Meta de páginas por dia: "))

if not leitor or not livro:
    print("Nome do Leitor ou título inválido")

elif total_paginas <= 0 or meta <= 0:
    print("O total de páginas e a meta diária deve ser maior que zero")

elif paginas_lidas < 0 or paginas_lidas > total_paginas:
    print("Páginas lidas não pode ser negativa e nem maior que o total de páginas")
else:
    if paginas_lidas == 0:
        status = "Não Iniciado"
    elif paginas_lidas > 0:
        status = "Em andamento"
    else:
        status = "Concluído"

    restantes = total_paginas - paginas_lidas
    porcentagem = paginas_lidas / total_paginas * 100
    blocos = restantes // meta
    sobra = restantes % meta

    print(f"Leitor: {leitor}")
    print(f"Livro: {livro}")
    print(f"Situação: {status}")
    print(f"Progresso: {porcentagem:.2f}%")
    print(f"Páginas restantes: {restantes}")
    print(f"Blocos completos de {meta} páginas: {blocos}")
    print(f"Páginas restantes após esses blocos: {sobra}")
