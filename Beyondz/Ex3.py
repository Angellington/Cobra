catalogo = [
    {
        "id": 1,
        "titulo": "The Last Melancholy",
        "autor": "A. R. Whitmore",
        "genero": "Drama",
        "ano": 2021,
        "idioma": "Inglês",
        "paginas": 302,
        "lidas": 82,
        "status": "Lendo",
        "avaliacao": 4.5,
    },
    {
        "id": 2,
        "titulo": "Lunis e as Cinco Estações",
        "autor": "Helena Duarte",
        "genero": "Fantasia",
        "ano": 2023,
        "idioma": "Português",
        "paginas": 487,
        "lidas": 312,
        "status": "Lendo",
        "avaliacao": 5.0,
    },
    {
        "id": 3,
        "titulo": "Um Livro para a Garota B",
        "autor": "C. M. Vasconcelos",
        "genero": "Romance",
        "ano": 2019,
        "idioma": "Português",
        "paginas": 214,
        "lidas": 214,
        "status": "Concluído",
        "avaliacao": 4.0,
    },
    {
        "id": 4,
        "titulo": "Flor Do Luar",
        "autor": "Isabela Nogueira",
        "genero": "Fantasia Romântica",
        "ano": 2022,
        "idioma": "Português",
        "paginas": 368,
        "lidas": 45,
        "status": "Lendo",
        "avaliacao": 4.2,
    },
    {
        "id": 5,
        "titulo": "O Silêncio das Marés",
        "autor": "Rafael Monteiro",
        "genero": "Suspense",
        "ano": 2020,
        "idioma": "Português",
        "paginas": 156,
        "lidas": 0,
        "status": "Não iniciado",
        "avaliacao": None,
    },
    {
        "id": 6,
        "titulo": "Cartas ao Inverno",
        "autor": "Sofia Almeida",
        "genero": "Poesia",
        "ano": 2018,
        "idioma": "Português",
        "paginas": 98,
        "lidas": 98,
        "status": "Concluído",
        "avaliacao": 5.0,
    },
    {
        "id": 7,
        "titulo": "A Cidade dos Relógios Quebrados",
        "autor": "T. J. Ferraz",
        "genero": "Ficção Científica",
        "ano": 2024,
        "idioma": "Português",
        "paginas": 642,
        "lidas": 127,
        "status": "Lendo",
        "avaliacao": 4.7,
    },
    {
        "id": 8,
        "titulo": "Pequeno Tratado sobre Estrelas",
        "autor": "Marina Kobayashi",
        "genero": "Não-ficção",
        "ano": 2017,
        "idioma": "Português",
        "paginas": 45,
        "lidas": 45,
        "status": "Concluído",
        "avaliacao": 3.8,
    },
    {
        "id": 9,
        "titulo": "Onde os Pássaros Não Cantam",
        "autor": "L. F. Andrade",
        "genero": "Terror",
        "ano": 2023,
        "idioma": "Português",
        "paginas": 528,
        "lidas": 210,
        "status": "Pausado",
        "avaliacao": 4.1,
    },
    {
        "id": 10,
        "titulo": "Versos para um Verão Improvável",
        "autor": "Beatriz Salgado",
        "genero": "Romance",
        "ano": 2016,
        "idioma": "Português",
        "paginas": 132,
        "lidas": 132,
        "status": "Concluído",
        "avaliacao": 4.6,
    },
]

titulos = [livro["titulo"] for livro in catalogo]
print("titulos", titulos)


# Filtro
mais_vinte = [
    livro["titulo"]
    for livro in catalogo
    if livro["paginas"] > 300
]
print("maisvinte", mais_vinte)

# Dict

# new_dict = {
#     livro["titulo"]: livro["paginas"]
#     for livro in catalogo
# }
# print("new dict", new_dict)

ordenado = sorted(
    catalogo,
    key=lambda livro: livro["paginas"]
)
print("ordenado", ordenado)
ordenado = sorted(
    catalogo,
    key=lambda livro: livro["paginas"],
    reverse=True
)

ordenado = sorted(
    catalogo,
    key=lambda livro: livro["titulo"]
)

total_paginas = sum(
    livro["paginas"]
    for livro in catalogo
)

print("total pagians", total_paginas)

livro_menor_pagina = min(
    catalogo,
    key=lambda livro: livro["paginas"]
)

livro_maior_pagina = max(
    catalogo,
    key=lambda livro: livro["paginas"]
)

livros_longos = {
    livro["titulo"]: livro["paginas"]
    for livro in catalogo
    if livro.get("titulo")
    and isinstance(livro.get("paginas"), int)
    and livro["paginas"] >= 1000
}