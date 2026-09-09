for dia in range(1, 6):
    print(f"Dia {dia} de estudo")

for numero in range(2, 11, 2):
    print(numero)

for dia in range(1, 8):
    print(f"Dia {dia}: estudar Python")
print("Semana concluída!")

paginas_lidas = [20, 35, 0, 30, 15, 0, 30]
total = 0
dias_leitura = 0

for numero, pagina in enumerate(paginas_lidas, start=1):
    if pagina == 0:
        print(f"Dia {numero}: nenhuma leitura")
    else:
        total += pagina
        dias_leitura += 1
        print(f"Dia {numero}: {pagina} páginas")

print(f"Total de paginas lidas foram {total}")
print(f"Dias de leitura {dias_leitura}")
