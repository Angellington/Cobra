
def buscar_por_id(catalogo, id_livro):
    for livro in catalogo:
        if livro["id"] == id_livro:
            return livro

    return None

def listar_titulos(catalogo):
    return [
        livro["titulo"]
        for livro in catalogo
    ]

def contar_livros(catalogo):
    return len(catalogo)

if __name__ == "__name__":
    print("O modelo operacoes foi executado diretamente.")