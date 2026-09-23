titulos = ["1984", "O Hobbit"]
print(f"titulos: {titulos}")

from encodings import utf_8
from pathlib import Path


arquivo = Path("data") / "titulos.txt"
print(f"Arquivo: {arquivo}")

CAMINHO_NORMAL = Path(__file__).parent
print("caminho normal", CAMINHO_NORMAL)

PASTA_PROJETO = Path(__file__).parent
PASTA_DADOS = PASTA_PROJETO / "data"
ARQUIVO_TITULOS = PASTA_DADOS / "titulos.txt"

print("ARQUIVO TITULO", ARQUIVO_TITULOS)

# arquivo.open("r", encoding=utf_8)
# arquivo.open("W", encoding=utf_8)
# arquivo.open("a", encoding=utf_8)
arquivo = open("titulos.txt", "r", enconding="utf8")
conteudo = arquivo.read()
arquivo.close()

# Mas é mais seguro
with open("titulos.txt", "r", enconding="utf-8") as arquivo:
    conteudo = arquivo.read()
    