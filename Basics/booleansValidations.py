idade = 21
tem_documento = True

print(idade >= 18 and tem_documento)


# AND

nota = 8
if nota >= 7 and nota <= 10:
    print("Nota válida e aluno aprovado")


status = "atrasado"
if status == "atrasado" or status == "perdido":
    print("É necessário verificar o livro")

nome = ""
print(not nome)
print(bool("False"))
livro_atual = None
if livro_atual is None:
    print("Nenhum livro foi informado")

nome = input("Nome do leitor: ")
idade = int(input("Idade: "))
paginas_lidas = int(input("Páginas lidas: "))

if len(nome) == 0:
    print("Nome inválido")
elif idade < 0:
    print("Idade inválida")
elif idade >= 18 and paginas_lidas >= 1:
    print("Lietor adulto identificado")
elif idade < 18 and paginas_lidas >= 1:
    print("Leitor de menor identifificadop")
elif paginas_lidas == 0:
    print("a leitira ainda não foi iniciada")