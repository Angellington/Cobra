from pathlib import Path
from datetime import date
from typing import Literal
from enum import Enum

try:
    from .despesas import abrir_arquivo
except ImportError:
    from despesas import abrir_arquivo

PASTA_PROJETO = Path(__file__).parent
DATA_ROUTE = PASTA_PROJETO / "dados"
DESPESA_ROUTE = DATA_ROUTE / "despesas.json"

class Options(Enum):
    ADICIONAR = 1
    LISTAR = 2
    DELETAR = 3
    SAIR = 4

def criar_despesa(path: Path) -> dict[list]:
    while True:
        descricao = str(input("Insira uma descrição: ")).strip()
        if descricao:
            break
        print("Escreva uma descrição")
    while True:
        entrada = input("Insira um valor: ").strip().replace(",", ".")

        try:
            valor = float(entrada)
        except ValueError:
            print("Digite um valor válido")
            continue

        if valor <= 0:
            print("O valor deve ser maior que zero")
            continue

        break
    while True:
        categoria = str(input("Insira uma categoria: ")).strip()
        if categoria:
            break
        print("Escreva uma categoria")

    despesa = {
        "id": identificar_ultimo_id(path),
        "descricao": descricao,
        "valor": valor,
        "categoria": categoria,
        "data": date.today().strftime('%d/%m/%Y')
    }
    return despesa

def identificar_ultimo_id(path: Path) -> int | Literal[1] | None:
    if not path.exists():
        return None

    despesas = abrir_arquivo(path=path)
    if not despesas:
        return 1
    return max(despesa["id"] for despesa in despesas) + 1

def validar_id(path: Path, id_despesa: int) -> bool:
    if not path.exists():
        return False
    if not id_despesa or id_despesa < 0:
        raise ValueError("Insira um id válido!")
    
    despesas = abrir_arquivo(path=path)
    return any(d["id"] == id_despesa for d in despesas)