livros = [
    "The Last Melancholy",
    "Um Livro para a Garota B",
    "Lunis e as Cinco Estações",
    "Flor do Luar"
]

print(livros)

print(livros[0])
print(livros[1])
print(livros[-1])
print(len(livros))

print(livros[:2])
livros[1] = "Flor do Luar 2"
print(livros)

livros = [
    "Crônicas do Avatar: A Ascensão de Kyoshi",
    "Crônicas do Avatar: A Escuridão de Kyoshi",
    "Crônicas do Avatar: A Aurora de Yangchen",
    "Crônicas do Avatar: O Legado de Yangchen",
    "Crônicas do Avatar: O Julgamento de Roku",
    "Crônicas do Avatar: O Despertar de Roku",
    "Crônicas do Avatar: A Calmaria de Kuruk",
    "Crônicas do Avatar: A Ferida de Kuruk",
    "Crônicas do Avatar: A Balança de Scezeto",
    "Crônicas do Avatar: A misticidade de Luyu",
    "Crônicas do Avatar: A Tenuocidade de Luna"
]

primeiro = livros[0]
print("primeiro", primeiro)
ultimo = livros[-1]
print("ultimo", ultimo)
quantos_livros = len(livros)
print("quantos livros", quantos_livros)
livros[1] = "KYOSHI"
print("Livros", livros)
print(livros[:2])

# Adicionar
livros = ["Lunis", "The Last Melancholy"]
livros.append("Flor do Luar")
print("livros", livros)



novo_titulo = input("Novo título para adicionar").strip()
novo_titulo = " ".join(novo_titulo.split())

if not novo_titulo:
    print("Título inválido")
else:
    livros.append(novo_titulo)

    print("Livros:", livros)
    print("Quantidade:", len(livros))
    print("Último título:", livros[-1])

    if "Lunis" in livros:
        livros.remove("Lunis")
    else:
        print("Livro não encontrado")