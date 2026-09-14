catalogo = [
    {
        "titulo": "1984",
        "paginas": 328,
        "lidas": 100
    },
    {
        "titulo": "The Last Melancholy",
        "paginas": 420,
        "lidas": 210
    }
]

def calcular_progresso(livro):
    if livro["paginas"] <= 0:
        return None 

    return livro["lidas"] / livro["paginas"] * 100

def apresentar_livro(titulo, paginas):
    return f"{titulo} possui {paginas} páginas."

print(apresentar_livro("Lunis", 320))




print(apresentar_livro(paginas=328, titulo="Flor do Luar"))

def criar_livro(titulo, paginas, genero):
    return {
        "titulo": titulo,
        "paginas": paginas,
        "genero": genero
    }

livro = criar_livro(
    "Lunis",
    paginas=120,
    genero=["Mistério", "Aventura"]
)

def saudar(nome, saudacao="Olá"):
    return f"{saudacao}, {nome}"

print(saudar("Letícia"))
print(saudar("Wellington", "Bom dia"))

def apresentar_livro(titulo, paginas, idioma="Português"):
    return f"{titulo} - {paginas} páginas - {idioma}"

print(apresentar_livro("1984", 328))
print(apresentar_livro("1984", 328, "Inglês"))

# Parâmetros obrigatórios devem vir antes dos parâmetros com valor padrão

# Correto
def exemplo(nome, idade=0):
    pass
# def exemplo(idade=0, nome):
    pass
# Incorreto / O próprio VS CODE alerta


def adicionar_livro(titulo, catalogo=[]):
    catalogo.append(titulo)
    return catalogo

print(adicionar_livro("1984"))
print(adicionar_livro("Luinis"))

def adicionar_livro(titulo, catalogo=None):
    if catalogo is None:
        catalogo = []

    catalogo.append(titulo)
    return catalogo

print(adicionar_livro("1984"))
print(adicionar_livro("Lunis"))

meus_livros = ["Kineorama", " Base Secreta"]
adicionar_livro("Hopes and Dreams", meus_livros)
adicionar_livro("Vlad Tapes", meus_livros)

print(meus_livros)