from codecs import ascii_decode
from genericpath import exists
import json
from pathlib import Path

# def validar_despesa(despesa: list[dict]):
def abrir_arquivo(path: str):
    if not path:
        ValueError("Insira um caminho válido!")

    try:
        with path.open("r", encoding="utf-8") as arquivo:
            arquivo = json.load(arquivo)

    except json.JSONDecodeError as Erro:
        return ValueError("Insira um arquiov json válido")
    if not isinstance(arquivo, list):
        ValueError("O valor não é uma lista")

    return arquivo

def adicionar_no_arquivo(despesa: dict, path: Path) -> None:
    if not path:
        raise ValueError("Insira um caminho válido")

    if path.exists() and path.stat().st_size > 0:
        with path.open("r", encoding="utf-8") as arquivo:
            despesas = json.load(arquivo)
    else:
        despesas = []

    despesas.append(despesa)

    with path.open("w", encoding="utf-8") as arquivo:
        json.dump(despesas, arquivo, ensure_ascii=False, indent=4)