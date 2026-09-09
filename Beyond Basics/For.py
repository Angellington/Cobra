livros = ["Lunis", "The Last Melancholy", "Flor do Luar"]

for livro in livros:
    print(livro)

for livro in livros:
    print("Livro: ", livro)

print(f"Temos {len(livros)} cadastrados.")

contador = 1

for livro in livros:
    print(f"{contador} - {livro}")
    contador += 1



livros = [
    "Espíritos",
    "Matheus",
    "Lucas",
    "Blueberry",
    "Romagnolia Ragnarokia",
    "Corte Carmesim",
    "Combinando com a Cor de Deus",
    "Quarta Guerra Mundial",
    "Além de Cor Leonis",
    "Delightful Doomsday",
]

contador = 1;
for livro in livros:
    print(f"Livro {contador} - {livro}")
    contador += 1

print(f"Total de Livros de The Last Melancholy são {len(livros)}")