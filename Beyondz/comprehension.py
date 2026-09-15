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

touhou = {
    "Embodiment of Scarlet Devil": 6,
    "Perfect Cherry Blossom": 7,
    "Imperishable Night": 8,
}


touhou_multiplica = {
    titulo: numero
    for titulo, numero in touhou.items()
    if numero * 2
}



livros_ordenados = sorted(catalogo, reverse=True)

print(f"Livro Ordenados: {livros_ordenados}")

por_paginas = sorted(
    catalogo,
    key=lambda livro: livro["paginas"]
)
catalogo_ordenado = sorted(
    catalogo,
    key=lambda livro: livro["paginas"],
    reverse=True
)
print(f"catalogo ordenado {catalogo_ordenado}")

por_titulo = sorted(catalogo, key=lambda livro: livro["titulo"].casefold())
print(f"Por título: {por_titulo}")

total = sum(livro["paginas"] for livro in catalogo)
menor = min(catalogo, key=lambda livro: livro["paginas"])
maior = max(catalogo, key=lambda livro: livro["paginas"])

print(total)
print(menor)
print(maior)

if catalogo:
    maior = max(catalogo, key=lambda livro: livro["paginas"])
else:
    maior = None

existe_livro_longo = any(
    livro["paginas"] > 500
    for livro in catalogo
)

todos_validos = all(
    livro["paginas"] > 0
            for livro in catalogo
    )

