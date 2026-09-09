livros = [
    "The Last Melancholy",
    "Flor do Luar",
    "Um Livro para a Garota B",
    "Lunis e as Cinco Estações"
]

livro_removido = livros.pop(1)
print("removido", livro_removido)

print("Livros: ", ", ".join(livros))
titulo_remover = input("Remover título: ").strip()
titulo_remover = " ".join(titulo_remover.split())

if not titulo_remover:
    print("Título vazio")
elif titulo_remover  in livros:
    livros.remove(titulo_remover)
else:
    print("Título não encontrado")

ultimo_livro = livros.pop()
print("ultimo livro", ultimo_livro)
print("Livros", livros)

