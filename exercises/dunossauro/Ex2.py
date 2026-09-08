# Faça um programa que peça 2 números inteiros e um número real. Calcule e mostre:

a = int(input("Digite o primeiro número inteiro: "))
b = int(input("Digite o segundo número inteiro: "))
c = float(input("Digite um número real: "))

teste1 = (a * 2) * (b / 2)
teste2 = (a * 3) + c
teste3 = c ** 3

print(f"O produto do dobro do primeiro com metade do segundo é: {teste1}")
print(f"A soma do triplo do primeiro com o terceiro é: {teste2}")
print(f"O terceiro elevado ao cubo é: {teste3}")