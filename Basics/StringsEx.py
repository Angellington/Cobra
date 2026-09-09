titulo = input("Qual nome do livro?: ")
titulo = " ".join(titulo.split())

if not titulo.strip():
    print("Título rejeitado!")
else:
    print(titulo)
    print(titulo.upper())
    print(titulo[0])
    print(titulo[-1])
    print(titulo[:5])