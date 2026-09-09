paginas_lidas = 120
meta = 100

print(paginas_lidas > meta)
print(paginas_lidas < meta)
print(paginas_lidas == meta)

idade = 21
idade == 21
idade == 22



paginas_lidas = 120
paginas_totais = 300

if paginas_lidas == 0:
    print("Livro não iniciado")
elif paginas_lidas < paginas_totais:
    print("Livro em leitura")
else:
    print("Livro concluído")


titulo = input("Qual o título do livro?: ")
paginas_totais = int(input("Quantas páginas o livro tem?: "))
paginas_lidas = int(input("Quantas páginas você já leu?: "))

if paginas_lidas == 0:
    print(f"Você ainda não começou a ler o livro {titulo}.")
elif paginas_lidas > paginas_totais:
    print("A quantidade de páginas lidas não pode ser maior que o total.")
elif paginas_lidas < paginas_totais:
    print(f"Você está lendo o livro {titulo}.\n Ainda restam {paginas_totais - paginas_lidas} páginas para terminar.")
else:
    print(f"Parabéns! Você concluiu a leitura do livro {titulo}.")