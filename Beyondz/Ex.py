
def apresentar_livro(titulo, paginas):
    return f"O livro {titulo} possui {paginas} páginas."

print(apresentar_livro("Lunis", 200))

def dobrar(numero):
    return numero * 2

valor = dobrar(7)
print(valor)
# O retorno no print seria None, pois é como estar colocando print por print, o print já é uma função, é como retornar uma função que retorna uma coisa, que retorna outra.


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
# Ex 3
def calcular_media_paginas(catalogo):

    if not catalogo:
        return None
    
    paginas = 0
    for livro in catalogo:
        paginas += livro["paginas"]

    return paginas / len(catalogo)



print(f"A média de páginas é {calcular_media_paginas(catalogo)}")

# Ex 4 - Buscar por gênero

catalogo = [
    {
        "titulo": "The Last Melancholy",
        "paginas": 1200,
        "genero": ["Fantasia", "Aventura", "Ação"]
    },{
        "titulo": "Flor Do Luar",
        "paginas": 32,
        "genero": ["Romance", "Cotidiano", "Drama"]
    },{
        "titulo": "Um Livro para a Garota B",
        "paginas": 512,
        "genero": ["Drama", "Mistério", "Cotidiano"]
    },{
        "titulo": "Lunis e as cinco estações",
        "paginas": 120,
        "genero": ["Mistério", "Drama", "Fantasia"]
    }
]

def buscar_por_genero(catalogo, genero):
    livros_genero = []
    genero_escolhido = genero.upper().strip()

    for livro in catalogo:
        for gen in livro["genero"]:
            gen_format = gen.upper().strip()

            if(gen_format == genero_escolhido):
                livros_genero.append(livro["titulo"])
                break

    if not livros_genero:
        return f"Nenhum livro possui o gênero {genero}."
    
    return f'Os livros que têm o gênero {genero} saõ {", ".join(livros_genero)}'

print(buscar_por_genero(catalogo, "Drama"))


# Ex 5

livro = {
    "titulo": "1984",
    "paginas": 328,
    "lidas": 100
}

progresso = livro["lidas"] / livro["paginas"] * 100

def calcular_progresso(livro):
    if livro["paginas"] <= 0:
        return None
    return livro["lidas"] / livro["paginas"] * 100

def mostrar_progresso(livro):
    progresso = calcular_progresso(livro)
    if progresso is None:
        return "Quantidade de páginas inválida"

    return f"{livro['titulo']}: {progresso:.2f}%"

print(mostrar_progresso(livro))

print(calcular_progresso({
    "titulo": "Teste",
    "paginas": 0,
    "lidas": 0
}))

print(buscar_por_genero(catalogo, "Terror"))