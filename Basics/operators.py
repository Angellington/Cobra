print(107 / 20)
print(107 // 20)
print(107 % 20)


paginas_faltam = int(input("Quantas páginas faltam para terminar o livro?: "))
paginas_pretende = int(input("Quantas páginas você pretende ler por dia?:"))

print(f"Você terá {paginas_faltam // paginas_pretende} blocos completos de leitura.")

print(f"Depois desses blocos, sobrarão {paginas_faltam % paginas_pretende} páginas.")


preco = 29.90
print(f"O preço: R$ {preco:.2f}")

# Exercício
manga = 2990
comprei = 3

total = manga * comprei
print(f"O preço em reais inteiros é: R$ {total // 100}")
print(f"Os centavos restantes são: {total % 100} centavos")