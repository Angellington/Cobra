import json
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