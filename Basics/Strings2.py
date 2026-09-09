titulo = "The Last Melancholy"
novo_titulo = titulo.replace("Last", "First")
print(titulo)
print(novo_titulo)

titulo = "   The_Last_Melancholy   "
novo_titulo = titulo.strip().replace("_", " ")
print("novo titulo", novo_titulo)


titulo = "The      Last Melancholy"
palavras = titulo.split()

print(palavras)
print("-".join(palavras))

titulo = "       Um Livro Para a Garota B  "
titulo_limpo = " ".join(titulo.split())
print(f" [{titulo_limpo}]")

texto = "   Python    é   muito    legal   "
texto_separado = texto.split()

print("texto separado", texto_separado)
texto_juntinho = " ".join(texto_separado)
texto_juntinho_dois = "-".join(texto_separado)

print("texto juntinho", texto_juntinho)
print("texto juntinho dois", texto_juntinho_dois)

print("-".join("ABC"))
print("-".join(["ABC", "DEF"]))

# Fase de acesso

texto = "Python tal"
print(texto[0])
print(texto[1])


print(texto[1:4])

livro = "Lunis e as Cinco Estações"
print(livro[0])
print(livro[-1])
print(livro[:3])
print(livro[3:])
