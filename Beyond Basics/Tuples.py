# tuplas são parecidas com listas, mas não podem ser alteradas depois de criadas


dimensoes = (1920, 1080)

print(dimensoes[0])
print(dimensoes[1])


generos = {"fantasia", "aventura", "fantasia", "misterio"}
print("generos", generos)

generos.add("ficção")
generos.remove("aventura")

print(generos)

if "fantasia" in generos:
    print("Gênero encontrado")


livro = ("THe Last Melancholy", 300, False)

titulo, paginas, terminado = livro

print(titulo)
print(paginas)
print(terminado)

primeiro, segundo, terceiro = ["A", "B", "C"]



livro = ("The Last Melancholy", 300, "Fantasia")

titulo, paginas, genero = livro
print(titulo)
print(paginas)
print(genero)

conjunto = { "Fantasia", "Aventura", "Fantasia", "Misterio"}

print("conjunto: ", conjunto)    
