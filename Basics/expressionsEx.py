titulo = input("Qual o título do livro: ")
paginas_totais = int(input("Quantas páginas o livro tem: "))
paginas_lidas = int(input("Páginas lidas: "))
porcentagem = paginas_lidas / paginas_totais * 100

if paginas_lidas == 0:
    print("Livro ainda não iniciado")
elif (paginas_lidas <= 0) or (paginas_totais < 0):
    print("Páginas inválidas")
elif(paginas_lidas > paginas_totais):
    print("Você leu mais que as páginas totais do livro")
elif(paginas_totais > paginas_lidas):
    print(f"Livro ainda em andamento com {porcentagem:.2f}% lidas")
else:
    print(f"Livro concluído {titulo}")