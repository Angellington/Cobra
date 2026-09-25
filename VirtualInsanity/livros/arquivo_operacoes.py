from pathlib import Path

from VirtualInsanity.livros.pathlibtrain import ARQUIVO_LIVROS
from VirtualInsanity.catalogo_operacoes import listar_livros

PASTA_PROJETO = Path(__file__).parent
PASTA_DADOS = PASTA_PROJETO / "data"
ARQUIVOS_LIVROS = PASTA_DADOS / "livros.txt"

def adicionar_titulo(titulo):
    titulo = titulo.strip()

    if not titulo:
        raise ValueError("O título não pde ser vazio.")
    PASTA_DADOS.mkdir(exist_ok=True)

    with ARQUIVO_LIVROS.open("a", encoding="utf-8") as arquivo:
        arquivo.write(f"{titulo}\n")

def quantidade_titulos():
    return len(listar_livros())

def arquivo_existe():
    return ARQUIVO_LIVROS.exists()

def apagar_titulos():
    if ARQUIVO_LIVROS.exists():
        ARQUIVO_LIVROS.unlink()
        return True
    return False
