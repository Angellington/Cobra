def calcular_progresso(livro):
    if livro["paginas"] <= 0:
        return None
    return livro["lidas"] / livro["paginas"] * 100
