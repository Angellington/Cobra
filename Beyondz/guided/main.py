from operacoes import (
    buscar_por_id,
    listar_titulos,
    contar_livros
)

catalogo = [
    {
        "id": 1,
        "titulo": "1984",
        "paginas": 328
    },
    {
        "id": 2,
        "titulo": "Lunis",
        "paginas": 120
    }
]



livro = buscar_por_id(catalogo, 1)

print(f"Livro encontrado {livro}")
print(f"Títulos: ", listar_titulos(catalogo))
print(f"Quantidade: {contar_livros(catalogo)}")

# caso de borda
print(f"Buscando vazio: ", buscar_por_id([], 1))
print(f"Buscando vazio: ", buscar_por_id(catalogo=catalogo, id_livro=999))

