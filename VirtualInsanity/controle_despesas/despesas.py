import json
import os
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

def listar_despesas(path: str) -> None:
    if not path:
        ValueError("Insira um path válido")
    despesa = abrir_arquivo(path=path)
    print(despesa)
    while True:
        continuar = input("Digite para continuar: ")
        if continuar:
            break

def deletar_despesa(path: str) -> None:
    if not path:
        ValueError("Insira um path válido")

    try:
        from .config import validar_id
    except ImportError:
        from config import validar_id

    os.system("clear")
    print(abrir_arquivo(path=path))
    while True:
        try:
            id = int(input("Qual o id que deseja deletar: "))
        except ValueError:
            print("Insira um valor válido")
            continue
        if not validar_id(path, id):
            print("O valor não existe")
            continue
        break

        
