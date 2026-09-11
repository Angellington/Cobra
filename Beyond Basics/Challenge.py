catalogo = [
    {
        "titulo": "The Last Melancholy",
        "paginas": 300,
        "terminado": True,
    },
    {
        "titulo": "Lunis e as Cinco Estações",
        "paginas": 210,
        "terminado": False,
    },
    {
        "titulo": "Flor do Luar",
        "paginas": 32,
        "terminado": True,
    }
]

for numero, livro in enumerate(catalogo, start=1):
    if livro['terminado']:
        status = "Concluído"
    else:
        status = "Em andamento"

    print(f"{numero}: {livro['titulo']}\n status: {status} e paginas: {livro['paginas']} ")

terminados = 0
for livro in catalogo:
    if(livro['terminado']):
        terminados += 1
print(f"Quantidade de Livros terminados: {terminados}")

total_paginas = 0
for livro in catalogo:
    total_paginas += livro['paginas']
print(f"Total de Páginas: {total_paginas}")

catalogo_copia = catalogo.copy()

catalogo_copia.append({
    "titulo": "Um Livro para a Garota B",
    "paginas": 500,
    "terminado": False
})

total_livros_copia = 0
total_livros_original = 0
for livros in catalogo:
    total_livros_original += 1

for livro in catalogo_copia:
    total_livros_copia += 1

print("Total da Cópia", total_livros_copia)
print("Total Original", total_livros_original)

# Forma mais simples
print("Total de Cópia Simples: ", len(catalogo_copia))
print("Total de Simples: ", len(catalogo))