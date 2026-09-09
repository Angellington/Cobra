nome = "   "
print(len(nome)) 

nome = "  Wellington "
print(nome.strip())


titulo = "  The Last Melancholy   "
print(titulo.strip())


nome = input("Nome do Leitor: ").strip()

if not nome:
    print("Nome inválido")
else:
    print(f"Olá, {nome}!")

# Maiscúla e Minúscula

titulo = "The Last Melancholy"
print(titulo.lower())
print(titulo.upper())
print(titulo.capitalize())

resposta = input("Você terminou o livro? ").strip().lower()

if resposta == "sim":
    print("Leitura concluída")

# Prática

titulo_pedido = input("Qual o título do livro?: ").strip()

if not titulo_pedido:
    print("Título inválido")
else:
    print(titulo_pedido.upper())
    print(titulo_pedido.lower())