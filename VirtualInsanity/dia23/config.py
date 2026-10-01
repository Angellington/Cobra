from pathlib import Path


PASTA_PROJETO = Path(__file__).parent
PASTA_DADOS = PASTA_PROJETO / "dados"
ARQUIVO_CATALOGO = PASTA_DADOS / "catalogo.json"
ARQUIVO_NOVO_CATALOGO = PASTA_DADOS / "catalogo_novo.json"

PASTA_DADOS.mkdir(parents=True, exist_ok=True)