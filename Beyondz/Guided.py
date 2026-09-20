

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

def ler_paginas(valor):
    try:
        valor = int(valor)
    except ValueError:
        return 'Não foi possível converter para inteiro.'

    if valor <= 0:
        raise ValueError("O valor está menor que 0")
    return valor


print(ler_paginas("320"))
print(ler_paginas("abc"))
# print(ler_paginas("-10"))


def criar_livro(titulo, paginas):
    if not titulo or not titulo.strip():
        raise ValueError("Não tem título")
    if not paginas or paginas<= 0:
        raise ValueError("Página não possui valores válidos")
    return {
        "titulo": titulo,
        "paginas": paginas
    }

# Catalogo seguro
def buscar_paginas(livro):
    try:
        return livro["paginas"]
    except KeyError:
        return "Chave inválida, procure a página correta"

def calcular_media(catalogo):
    total = 0

    if not catalogo:
        raise ValueError("Você precisa ter alguma conteúdo para calcular a média")
    for livro in catalogo:
        total += livro["paginas"]

    return total / len(catalogo)


try:
    print(calcular_media([]))
except ValueError as erro:
    print(f"Erro: {erro}")