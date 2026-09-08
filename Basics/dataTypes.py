nome = "Wellington"
idade = 21
altura = 1.75
estudando = True

valores = [nome, idade, altura, estudando]

for valore in valores:
    print(type(valore))

livro = "The Last Melancholy"
paginas = 534
preco = 29.90
terminou = True

tlm = {
    "Livro": livro,
    "Páginas": paginas,
    "Preço": preco,
    "Terminou": terminou
}

for key, tlm_value in tlm.items():
    print(f"{key}: {tlm_value} - Tipo: {type(tlm_value)}")

print(tlm["Páginas"]) ## Acessando valor de um dicionário