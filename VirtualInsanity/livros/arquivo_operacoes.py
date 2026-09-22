from pathlib import Path

PASTA_DADOS = Path(__file__).parent / "data"
ARQUIVO_TITULOS = PASTA_DADOS / "titulos.txt"

def salvar_titulos(titulos):
    PASTA_DADOS.mkdir(exist_ok=True)

    with ARQUIVO_TITULOS.open("w", encoding="utf-8") as arquivo:
        for titulo in titulos:
            arquivo.write(f"{titulo}\n")

def ler_titulos():
    if not ARQUIVO_TITULOS.exists():
        return []

    with ARQUIVO_TITULOS.open("r", encoding="utf-8") as arquivo:
        return [
            linha.strip()
            for linha in arquivo
            if linha.strip()
        ]