def saudacao():
    print("Olá, Minerva!")

saudacao()
saudacao()

def nomem_da_funcao():
    # codigo da funcao
    pass

# 3 Parametros e Argumentos

def saudar_pessoa(nome):
    print(f"Olá, {nome}")

saudar_pessoa("Wellington")
saudar_pessoa("Letícia")

def mostrar_livro(titulo, paginas):
    print(f"{titulo} possui {paginas} paginas")

mostrar_livro("Flor do Luar", 32)


def somar_com_print(a, b):
    print(a + b)

resultado = somar_com_print(2, 3)

print(resultado)

# com return
def somar(a, b):
    return a + b

resultado = somar(2, 3)
print(resultado)
total = somar(10, 20)
dobro = somar(10, 20) * 2

print(total)
print(dobro)

def verificar_idade(idade):
    if idade < 0:
        return 'Idade inválida'

    return f"Idade informada: {idade}"

print(verificar_idade(21))
print(verificar_idade(-1))

def exemplo():
    return "Primeiro retorno"
    return "Segundo retorno"
print(exemplo())

# Responsabilidade única
# uma função deve fazer uma tarefa bem definida

# Evite:

def processar_livro():
    # lê dados
    # valida titulo
    # calcula progresso
    # busca livro
    # imprime menu
    # salva dados
    pass

# Prefira funções menores:

def calcular_progresso(paginas_lidas, paginas_totais):
    if paginas_lidas <= 0:
        return None

    if paginas_lidas < 0 or paginas_lidas > paginas_totais:
        return None

    return paginas_lidas / paginas_totais * 100

def buscar_livro(catalogo, termo):
    encontrados = []

    termo = termo.strip().casefold()

    if not termo:
        return encontrados

    for livro in catalogo:
        titulo = livro["titulo"].casefold()

        if termo in titulo:
            encontrados.append(livro)

    return encontrados


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

for livro in catalogo:
    progresso = calcular_progresso(
        livro["lidas"],
        livro["paginas"]
    )

    print(f"{livro['titulo']}: {progresso:.1f}%")

resultado = buscar_livro(catalogo, "1984")

for livro in resultado:
    print(livro["titulo"])

# Casos de Borda
print(calcular_progresso(0, 300))
print(calcular_progresso(300, 300))
print(calcular_progresso(50, 0))
print(calcular_progresso(-10, 300))
print(calcular_progresso(400, 300))

buscar_livro(catalogo, "")
# Deve funcioanr sem diferenciar maiúsculas:
buscar_livro(catalogo, "THE LAST")
buscar_livro(catalogo, "the last")
buscar_livro(catalogo, "The Last")