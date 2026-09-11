catalogo_a = ["Lunis", "The Last Melancholy"]
catalogo_b = catalogo_a

catalogo_b.append("Flor do Luar")

print("A: ", catalogo_a)
print("B: ", catalogo_b)
print(catalogo_a is catalogo_b)

catalogo_b = catalogo_a.copy()
catalogo_b.append("Um Livro para a Garota B")

print("A: ", catalogo_a)
print("B: ", catalogo_b)