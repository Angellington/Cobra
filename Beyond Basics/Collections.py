livros = [
    {"título": "The Last Melancholy", "paginas": 300},
    {"título": "Lunis e as cinco estações", "páginas": 250}
]

for livro in livros:
    print(livro["título"])

catalogo_a = ["Livro A", "Livro B"]
catalogo_b = catalogo_a

print(catalogo_a)
print(catalogo_b)

catalogo_b.append("Livro C")


print(catalogo_a)
print(catalogo_b)

catalogo_b = catalogo_a.copy()

catalogo_b.append("Livro D")

print(catalogo_a)
print(catalogo_b)

a = [1, 2]
b = [1, 2]
c = a

# == compara conteúdo
# is verifica se é o mesmo objeto
print(a == b) # True
print(a is b) # False
print(a is c) # True