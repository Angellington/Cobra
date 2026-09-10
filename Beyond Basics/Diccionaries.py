livro = {
    "titulo": "The Last Melancholy",
    "autor": "Anjo Fundador",
    "paginas": 300,
    "terminou": False
}

print(livro["autor"])
print(livro["paginas"])
print(livro["titulo"])

livro["paginas"] = 534
livro["genero"] = "Fantasia"

print("livro", livro)

del livro["genero"]

print("livro", livro)


# Consultar key sem ocorrer um keyError

print(livro.get("isbn", "ISBN Não encontrado"))
# O segundo argumento é para caso a chave não exista

if "autor" in livro:
    print("O autor está cadastrado")

for key, value in livro.items():
    print(f"{key}: {value}")