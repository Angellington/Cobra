catalogo = [
    {
        "titulo": "1984",
        "paginas": 328,
        "lidas": 100
    },
    {
        "titulo": "The Last Melancholy",
        "paginas": 420,
        "lidas": 210
    }
]

paginas = []

for livro in catalogo:
    paginas.append(livro["paginas"])

paginas = [livro["paginas"] for livro in catalogo]

# Estrutura 
# [expressao for item in colecao]


concluidos = [ 
    livro
    for livro in catalogo
    if livro["lidas"] == livro["paginas"]
]

catalogo = {
    "1984": 328,
    "Lunis": 120,
    "The Last Melancholy": 420
}

dobradas = {
    titulo: paginas * 2
    for titulo, paginas in catalogo.items()
}

print(dobradas)

livros_longos = {
    titulo: paginas
    for titulo, paginas in catalogo.items()
    if paginas >= 300
}

print(f"Livros Longos {livros_longos}")