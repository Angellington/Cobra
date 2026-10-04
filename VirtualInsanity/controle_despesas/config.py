from genericpath import exists
from pathlib import Path
from datetime import date
from despesas import abrir_arquivo

PASTA_PROJETO = Path(__file__).parent
DATA_ROUTE = PASTA_PROJETO / "dados"
DESPESA_ROUTE = DATA_ROUTE / "despesas.json"


def criar_despesa(path: str):
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

def identificar_ultimo_id(path: str):
    if not path.exists():
        return None
    
    despesas = abrir_arquivo(path=path)
    if not despesas:
        return 1
    return max(despesa["id"] for despesa in despesas) + 1
