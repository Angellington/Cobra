def adicionar_livro(titulo, catalogo=None):
    if catalogo is None:
        catalogo = []

    catalogo.append(titulo)
    return catalogo

def criar_mensagem():
    mensagem = "Olá"
    print(mensagem)

criar_mensagem()
# print(mensagem)

catalogo = []

def mostrar_catalogo():
    print(catalogo)

mostrar_catalogo()

catalogo = [{ "titulo": "1984", "paginas": 328}]

# Evite
def buscar_livro(termo):
    for livro in catalogo:
        if termo.casefold() in livro["titulo"].casefold():
            print("livro", livro)


# Use mais assim, passe o objeto direto para analisart dentro do escopo do objeto
def buscar_livro(catalogo, termo):
    encontrados = []

    termo = termo.strip().casefold()

    for livro in catalogo:
        titulo = livro["titulo"].casefold()

        if termo in titulo:
            encontrados.append(livro)

    return encontrados


catalogo_a = [{"titulo": "1984", "paginas": 328}]
catalogo_b = [{"titulo": "Lunis", "paginas": 120}]

print(buscar_livro(catalogo_a, "1984"))
print(buscar_livro(catalogo_b, "Lunis"))


contador = 0

def incrementar():
    global contador
    contador += 1

def incrementar(contador):
    return contador + 1

contador = 0
contador = incrementar(contador)
contador = incrementar(contador)


def validar_paginas(paginas):
    return paginas > 0

def criar_livro(titulo, paginas, generos=None):
    if generos is None:
        generos = []
    return {
        "titulo": titulo.strip(),
        "paginas": paginas,
        "generos": generos
    }

def adicionar_livro(catalogo, livro):
    catalogo.append(livro)
    return catalogo


catalogo = []
if validar_paginas(327):
    livro = criar_livro("1984", 328, ["Distopia"])
    adicionar_livro(catalogo, livro)

print(catalogo)


def calcular_progresso(livro):
    """Retorna o percentual de páginas lidas do livro"""

    if livro["paignas"] <= 0:
        return None

    return livro["lidas"] / livro["paginas"] * 100

print(calcular_progresso.__doc__)

def buscar_livro(catalogo, termo):
    """
    Busca livros pelo título.

    Retorna uma lista vazia quando nenhum livro é encontrado
    """

def buscar_livro(catalogo, termo):
    """
    Recebe o CATALOGO, e o termo que vai ser buscado entre o catáogo
    
    Recebe 
    """
    encontrados = []

    termo = termo.strip().casefold()

    if not termo:
        return encontrados

    for livro in catalogo:
        if termo in livro["titulo"].casefold():
            encontrados.append(livro)

    return encontrados



def listar_livros(catalogo):
    if not catalogo:
        return "Catálogo vazio."

    linhas = []

    for numero, livro in enumerate(catalogo, start=1):
        linhas.append(
            f"{numero}. {livro["titulo"]} - "
            f"{livro["paginas"]} páginas"
        )
    return "\n".join(linhas)

catalogo = [
    {"titulo": "1984", "paginas": 328},
    {"titulo": "Lunis", "paginas": 120}
]

print(listar_livros(catalogo))

resultado = buscar_livro(catalogo, "lun")
print(resultado)


catalogo = []

def cadastrar():
    titulo = input("Título: ")
    catalogo.append(titulo)

def cadastrar(catalogo, titulo):
    catalogo.append(titulo)
    return catalogo



catalogo = []

def adicionar(catalogo, titulo):
    catalogo.append(titulo)
    return catalogo

def contar_livros(catalogo):
    """
    Ela deve retornar a quantidade de livros
    """
    return len(catalogo)


