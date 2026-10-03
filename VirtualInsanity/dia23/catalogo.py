import json
from multiprocessing.sharedctypes import Value
from pathlib import Path


from config import ARQUIVO_NOVO_CATALOGO, PASTA_DADOS, ARQUIVO_CATALOGO

catalogo = [
    {
        "id": 1,
        "titulo": "The Last Melancholy",
        "autor": "Wellington Ferreira",
        "paginas": 302,
        "avaliacao": 4.5
    },
    {
        "id": 2,
        "titulo": "Lunis e as Cinco Estações",
        "autor": "Wellington Ferreira",
        "paginas": 487,
        "avaliacao": 5.0
    }
]

with ARQUIVO_CATALOGO.open("w", encoding="utf-8") as arquivo:
    json.dump(catalogo, arquivo, indent=4, ensure_ascii=False)

with ARQUIVO_CATALOGO.open("r", encoding="utf-8") as arquivo:
    catalogo_lido = json.load(arquivo)

print(catalogo_lido)
print(catalogo_lido[0]["titulo"])
print(catalogo_lido[1]["paginas"])

def salvar_catalogo(catalogo, pasta_dados=ARQUIVO_CATALOGO):
    PASTA_DADOS.mkdir(parents=True, exist_ok=True)

    with pasta_dados.open("w", encoding="utf-8") as arquivo:
        json.dump(catalogo, arquivo, indent=4, ensure_ascii=False)


def ler_catalogo(catalogo):
    if not ARQUIVO_CATALOGO.exists():
        return []

    try:
        with ARQUIVO_CATALOGO.open("r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        raise ValueError("O arquivo possui JSON inválido") from Erro

    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")
    return catalogo

def todos_os_livros(pasta_dados=ARQUIVO_NOVO_CATALOGO):
    if not pasta_dados.exists():
        return []

    try:
        with pasta_dados.open("r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        raise ValueError("O arquivo possui JSON inválido") from Erro
    
    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")

    return [livro["titulo"] for livro in catalogo]

def quantidade_livros(pasta_dados=ARQUIVO_NOVO_CATALOGO):
    if not pasta_dados.exists():
        return 0

    try:
        with pasta_dados.open("r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        raise ValueError("O arquivo possui JSON inválido") from Erro

    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")
    return len(catalogo)

def catalogo_validation(pasta_dados):
    if not pasta_dados.exists():
        return False

    try:
        with pasta_dados.open("r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        raise ValueError("O arquivo possui JSON inválido") from Erro

    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")
    return True

def ler_json(pasta_dados):
    if not pasta_dados.exists():
        return []

    try:
        with pasta_dados.open("r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        raise ValueError("O arquivo possui JSON inválido") from Erro

    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")
    return catalogo

def maior_avaliacao(pasta_dados=ARQUIVO_NOVO_CATALOGO):
    if not pasta_dados.exists():
        return None

    try:
        with pasta_dados.open("r", encoding="utf-8") as arquivo:
            catalogo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        raise ValueError("O arquivo possui JSON inválido") from Erro

    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")

    return max(
        (f"{livro["titulo"]} - {livro["avaliacao"]} estrelas!" for livro in catalogo if livro["avaliacao"] is not None),
        default=None
    )

def adicionar_livro(livro, pasta_dados=ARQUIVO_NOVO_CATALOGO):
    catalogo_validation(pasta_dados)
    catalogo = ler_json(pasta_dados)
    catalogo.append(livro)
    salvar_catalogo(catalogo, pasta_dados)

def calcular_total_paginas(catalogo: list[dict]) -> int:
    return sum(livro["paginas"] for livro in catalogo);

def busca_por_id(
        catalogo: list[dict],
        id_livro: int
) -> dict | None:
    for livro in catalogo:
        if livro["id"] == id_livro:
            return livro


def catalogo_validation_pure(catalogo: list[dict]) -> list[dict]:
    if not catalogo:
        raise ValueError("Não é um catalogo válido")
    if not isinstance(catalogo, list):
        raise ValueError("O catalogo precisa ser uma lista")
    if len(catalogo) <= 0:
        raise ValueError("O catalogo não possui valor?")
    return catalogo

def listar_titulos(catalogo: list[dict]) -> list[str]:
    catalogo_validation_pure(catalogo)

    

    return [
        livro["titulo"] for livro in catalogo
    ]



def calcular_media_avaliacao(catalogo: list[dict]) -> float:
    catalogo_validation_pure(catalogo=catalogo)

    avaliacoes = [
        livro["avaliacao"]
        for livro in catalogo
        if livro["avaliacao"] is not None
    ]

    if not catalogo:
        return 0.0

    return sum(avaliacoes) / len(avaliacoes)    


def buscar_por_titulo(
        catalogo: list[dict],
        termo: str
) -> list[dict]:
    catalogo_validation_pure(catalogo=catalogo)
    termo = termo.strip()
    if not catalogo:
        raise ValueError("Coloque um catálogo de verdade")
    if not termo:
        raise ValueError("Insira um termo correto")
    termo_normalizado = termo.casefold()

    return [
        livro for livro in catalogo
        if termo_normalizado in livro["titulo"].casefold()
    ]