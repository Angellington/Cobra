def criar_resumo(titulo, paginas, autor="Desconhecido"):
    if not titulo.strip():
        return None
    if paginas <= 0:
        return None

    resumo = {
        "titulo": titulo.strip(),
        "paginas": paginas,
        "autor": autor.strip()
    }

    return resumo


print(criar_resumo(paginas=328, titulo="1984", autor="George Owel"))




def calcular_desconto(preco, percentual=10):
    if preco <= 0 or not preco:
        return None

    desconto = preco * (percentual / 100)

    return preco - desconto

print(calcular_desconto(preco=100), "R$")
print(calcular_desconto(preco=100, percentual=20))


def adicionar_genero(genero, generos=None):
    if generos is None:
       generos = []

    if not genero:
        return generos

    generos.append(genero.strip())
    return genero

print(adicionar_genero("Drama"))
print(adicionar_genero("Fantasia"))


def criar_livro(titulo, paginas, generos=None, catalogo=None):
    if generos is None:
        generos = []

    if catalogo is None:
        catalogo = []

    if not titulo:
        return None

    if paginas <= 0:
        return None

    livro = {
        "titulo": titulo.strip(),
        "paginas": paginas,
        "generos": generos,
    }

    catalogo.append(livro)

    return catalogo

print("criar: ", criar_livro("Lunis", 223, ["Ação, Aventura"]))