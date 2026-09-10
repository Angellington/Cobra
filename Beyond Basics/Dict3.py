livros = [
    {
        "titulo": "The Last Melancholy",
        "paginas": 300,
        "terminado": False
    },
    {
        "titulo": "Lunis e as Cinco Estações",
        "paginas": 250,
        "terminado": True
    }
]

concluidos = 0

for livro in livros:
    if livro["terminado"]:
        status = "Concluido"
        concluidos += 1
    else:
        status = "Em andamento"

    print(livro["titulo"])
    print(livro["paginas"])
    print(livro["terminado"])
    print(f"Status: {status}")

print("Livros concluidos", concluidos)
