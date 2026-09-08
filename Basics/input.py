livro = input("Digite o nome do livro: ")
print(f"O livro digitado foi: {livro}")

paginas = int(input("Quantas paginas o livro tem?: "))
print(type(paginas))

print(f"Ainda faltam ler 20 páginas, faltarão  {paginas - 20}")

livro = input("Qual foi o último livro que você leu?: ")
paginas = int(input("Quantas páginas o livro tem?: "))
lidas = int(input("Quantas páginas você já leu?: "))
print(f"Você leu {lidas} páginas do livro {livro}, ainda faltam {paginas - lidas} páginas para terminar o livro.")

0