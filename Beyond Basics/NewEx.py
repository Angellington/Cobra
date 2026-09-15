def criar_livro(titulo, ano, autor, paginas):
    if not titulo:
        return None
    titulo = titulo.strip()

    if ano <= 0 or ano is str:
        return None

    autor = autor.strip()
    