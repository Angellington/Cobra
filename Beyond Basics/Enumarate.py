from prompt_toolkit import print_formatted_text


livros = ["The Last Melancholy", "Flor do Luar", "Um Livro para a garota B", "Lunis e as Cinco Estações"]

for numero, livro in enumerate(livros, start=1):
    print(f"Livro {numero} - {livro}")

livros_avatar = ["Ascensão de Kyoshi", "Escuridão de Kyoshi", "Aurora de Yangchen", "Legado de Yangchen", "O Julgamento de Roku", "O Despertar de Roku"]

for numero, livro in enumerate(livros_avatar, start=1):
    print(f"Crônicas do Avatar {numero} - {livro}")


paginas = [200, 150, 300]
total = 0

for quantidade in paginas:
    total += quantidade

print(f"Total: {total} páginas")

total = 0
paginas_lidas = [20, 35, 0, 40, 15]

for quantidade in paginas_lidas:
    total += quantidade

print(f"Total: {total}")

print("Usando a função sum: ",sum(paginas_lidas))

total = 0
dias_com_leitura = 0

for quantidade in paginas_lidas:
    total += quantidade

    if quantidade > 0:
        dias_com_leitura += 1

print(f"Total: {total} páginas")
print(f"Dias com leitura: {dias_com_leitura}")