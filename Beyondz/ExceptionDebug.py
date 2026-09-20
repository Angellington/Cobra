# Traceback
# Diferenciar ValueError, KeyError, TypeError
# try except
# else finally
# raise
# breakpoint()

# numero = int("abc")
# O traceback informa como o erro aconteceu

# Principais Exceções
# ValueError
# idade = int("vinte")

# KeyError
# livro = {"titulo": "1984"}
# print(livro["paginas"])

# TypeError
# resultado = "10" + 5

# IndexError
# livros = ["1984"]
# print(livros[3])



try:
    paginas = int(input("Digite a quantidade de páginas: "))
except ValueError:
    print("Digite um número inteiro válido")

# Evitar
try:
    paginas = int(input("Páginas: "))
except:
    print("Algo deu errado")

# 4 else e finally
try:
    paginas = int("320")
except ValueError:
    print("Valor inválido.")
else:
    print(f"Páginas registradas: {paginas}")
finally:
    print("Processamento encerrado")

def validar_paginas(paginas):
    if paginas <= 0:
        raise ValueError("A quantidade de páginas deve ser maior que zero.")
    return paginas

try:
    paginas = validar_paginas(0)
except ValueError as erro:
    print(f"Erro: {erro}")

def criar_livro(titulo, paginas):
    if not titulo.strip():
        raise ValueError("O título não pode estar vazio.")

    if paginas <= 0:
        raise ValueError("As páginas devem ser maiores que zero.")

    return {
        "titulo": titulo.strip(),
        "paginas": paginas
    }

try:
    livro = criar_livro("1984", 328)
except ValueError as erro:
    print(f"Não foi possível criar o livro: {erro}")
else:
    print("Livro criado: ", livro)
finally:
    print("Operação finalizada.")


def mostrar_paginas(livro):
    try:
        return livro["paginas"]
    except KeyError:
        return "Livro sem informação de páginas"

# EVITAR
# try:
#     return livro["paginas"] / 0
# except:
#     return None


livro =    {
        "id": 2,
        "titulo": "Lunis e as Cinco Estações",
        "autor": "Helena Duarte",
        "genero": "Fantasia",
        "ano": 2023,
        "idioma": "Português",
        "paginas": 487,
        "lidas": 312,
        "status": "Lendo",
        "avaliacao": 5.0,
    },

def calcular_progresso(livro):
    breakpoint()

    return livro["lidas"] / livro["paginas"] / 100

calcular_progresso(livro)

