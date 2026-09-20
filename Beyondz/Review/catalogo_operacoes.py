from typing import Type


def id_livro_validation(id_livro):
    try:
        id_livro = int(id_livro)
    except (ValueError, TypeError):
        raise ValueError("Insira um número.")
    if not id_livro:
        raise ValueError("Insira um valor válido para o id")
    if id_livro <= 0:
        raise ValueError("Insira um id positivo")
    return id_livro

def titulo_validation(titulo):
    titulo = titulo.strip()

    if not titulo:
        raise ValueError("Insira um título válido")
    else:
        return titulo

def paginas_validation(paginas):
    try:
        paginas = int(paginas)
    except (TypeError, ValueError):
        raise ValueError("Coloque um valor válido para as págians")
    if paginas <= 0 or not paginas:
        raise ValueError("Coloque um valor válido para as páginas")
    return paginas

def catalogo_validation(catalogo):
    if not isinstance(catalogo, list):
        raise ValueError("O catalogo deve ser uma lista")
    return catalogo

def status_validation(status):
    status = status.strip().casefold()
    if not status:
        raise ValueError("Insira um valor de status válido")
    return status

def calcular_quantidade_paginas_totais(catalogo):
    catalogo = catalogo_validation(catalogo=catalogo)
    total_paginas = 0

    for livro in catalogo:
        total_paginas += livro["paginas"]
    return total_paginas


def criar_livro(id_livro, titulo, paginas):
    return {
        "id_livro": id_livro_validation(id_livro=id_livro),
        "titulo": titulo_validation(titulo=titulo),
        "paginas": paginas_validation(paginas=paginas),
        "status": "Não iniciado"
    }



def buscar_por_id(catalogo, id_livro):
    id_livro = id_livro_validation(id_livro=id_livro)
    catalogo = catalogo_validation(catalogo=catalogo)

    for livro in catalogo:
        if livro["id_livro"] == id_livro:
            return livro

    return None

def adicionar_livro(catalogo, livro):
    if buscar_por_id(catalogo, livro["id_livro"]) is not None:
        raise ValueError("Já existe um livro com esse ID.")

    catalogo.append(livro)
    return livro


def filtrar_por_status(catalogo, status):
    catalogo_validation(catalogo)
    status = status_validation(status)

    return [
        livro
        for livro in catalogo
        if livro["status"].strip().casefold() == status
    ]

def calcalar_media(catalogo):
    catalogo_validation(catalogo=catalogo)
    if not catalogo:
        raise ValueError("Não é possível calcular a média de um catálogo vazio")

    return calcular_quantidade_paginas_totais(catalogo) / len(catalogo)