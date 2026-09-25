from VirtualInsanity.livros.pathlibtrain import ARQUIVO_LIVROS
from VirtualInsanity.catalogo_operacoes import listar_livros

PASTA_PROJETO = Path(__file__).parent
PASTA_DADOS = PASTA_PROJETO / "data"
ARQUIVOS_LIVROS = PASTA_DADOS / "livros.txt"

def catalogo_validation(catalogo):
    length_catalogo = len(catalogo)
    if length_catalogo <= 0 or not catalogo:
        raise ValueError("Insira um catálogo válido")

def buscar_por_id(catalogo, id_livro):
    id_livro = int(id_livro)
    catalogo_validation(catalogo)

    try:
        id_livro = int(id_livro)
    except(TypeError, ValueError):
        raise ValueError("O ID precisa ser um número inteiro.")

    
    if not id_livro or id_livro <= 0:
        raise ValueError("Não foi informado o id do livro")
    for livro in catalogo:
        if livro["id"] == id_livro:
            return livro
    return None


def listar_livros(catalogo):
    catalogo_validation(catalogo)

    return [
        livro["titulo"]
        for livro in catalogo
    ]

def filtrar_por_status(catalogo, status):
    catalogo_validation(catalogo)
    status = status.strip()

    if not status or not status.strip():
        raise ValueError("Insira um status válido")
        
    status = status.strip().casefold()

    return [
        livro
        for livro in catalogo
        if(livro["status"].casefold() == status)
    ]        
from pathlib import Path



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

    

if __name__ == "__main__":
    print("Operações executado")