from pathlib import Path

<<<<<<< HEAD
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
=======
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
>>>>>>> 963464d87bd2a9209dc035be1392bb45338ecb2d
