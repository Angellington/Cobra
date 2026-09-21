from pathlib import Path

PAST_PROJETO = Path(__file__).parent
PASTA_DADOS = PAST_PROJETO / "data"
ARQUIVO_LIVROS = PASTA_DADOS / "livros.txt"


PASTA_DADOS.mkdir(exist_ok=True)

print("Arquivo: ", ARQUIVO_LIVROS)
