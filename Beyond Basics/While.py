for numero in range(1, 4):
    print(numero)

contador = 1

while contador <= 3:
    print(f"Contagem: {contador}")
    contador += 1

while True:
    resposta = input("Digite sair para encerrar: ").strip().lower()
    if resposta == "sair":
        break

    print("Você ainda está no programa")


numero = 0

while numero < 5:
    numero += 1

    if numero == 3:
        continue

    print(numero)





while True:
    total = 0
    dias = 0
    try:
        pagina = int(input("Paǵinas lidas: "))
    except ValueError:
        print("Digite apenas um número inteiro.")
        continue
    if(pagina < 0):
        print("Valor inválido")
        continue
    elif(pagina == 0):
        break


    total += pagina
    dias += 1

print(f"Total de Páginas: {total}")
print(f"Dias lidos {dias}")
if dias > 0:
    media = total / dias
    print(f"Média por dia: {media:.2f} páginas")
else:
    print("Nenhum dia de leitura foi registrado")


