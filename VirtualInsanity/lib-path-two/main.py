from pathlib import Path

PASTA_PROJETO = Path(__file__).parent
PASTA_DADOS = PASTA_PROJETO / "data"
ARQUIVO_TITULOS = PASTA_DADOS / "titulos.txt"

print(f"Pasta do projeto: {PASTA_PROJETO}")
print(f"Pasta de dados: {PASTA_DADOS}")
print(f"Arquivo de títulos: {ARQUIVO_TITULOS}")

print(PASTA_DADOS.exists())

PASTA_DADOS.mkdir(exist_ok=True)

print(PASTA_DADOS.exists())

print(f"A pasta existe? {PASTA_DADOS.exists()}")
PASTA_DADOS.mkdir(exist_ok=True)
print(f"A pasta existe agora? {PASTA_DADOS.exists()}")

with ARQUIVO_TITULOS.open("w", encoding="utf-8") as arquivo:
    arquivo.write("Lunis\n")
    arquivo.write("The Last Melancholy\n")
print(f"O arquivo existe? {ARQUIVO_TITULOS.exists()}")

with ARQUIVO_TITULOS.open("r", encoding="utf-8") as arquivo:
    conteudo = arquivo.read()

print("Conteudo", conteudo)

with ARQUIVO_TITULOS.open("r", encoding="utf-8") as arquivo:
    titulos = [
        linha.strip()
        for linha in arquivo
        if linha.strip()
    ]

print("Linhas", titulos)

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

def adicionar_titulo(titulo):
    titulo = titulo.strip()

    if not titulo:
        return False
    titulos = ler_titulos()

    if titulo.casefold() in {item.casefold() for item in titulos}:
        return False

    titulos.append(titulo)
    salvar_titulos(titulos)
    return True


titulos = ["Lunis", "The Last Melancholy"]

salvar_titulos(titulos)

titulos_lidos = ler_titulos()

print(titulos_lidos)

def excluir_titulo(titulo):
    titulo_buscado = titulo.strip().casefold()
    titulos = ler_titulos()

    titulos_atualizados = [
        item
        for item in titulos 
        if item.casefold() != titulo_buscado
    ]

    if len(titulos_atualizados) == len(titulos):
        return False

    salvar_titulos(titulos_atualizados)
    return True

print(excluir_titulo("LUNIS"))
print(ler_titulos())

print(excluir_titulo("Título inexistente"))
print(ler_titulos())