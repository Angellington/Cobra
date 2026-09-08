# Faça um programa que mostre a mensagem "Alo mundo" na tela:
print("Alo mundo")

# Faça um programa que peça um número e então mostre a mensagem "O número informado foi [número]":

numero = input("Digite um numero: ")
print(f"O núnero informado foi {numero}")

# Faça um programa que peça dois números e imprima a soma:

n1 = input("Digite o primeiro número: ")
n2 = input("DIgite o segundo número: ")
soma = int(n1) + int(n2)
print(f"A soma dos números é: {soma} ")

# Faça um programa que peça as 4 notas bimestrais e mostre a média.

n1 = float(input("Digite a primeira nota: "))
n2 = float(input("Digite a segunda nota: "))
n3 = float(input("Digite a terceira ntoa: "))
n4 = float(input("Digite a quarta nota: "))

map = [n1, n2, n3, n4]

media = sum(map) / len(map)
print(f"A média das notas é: {media}")

# Faça um programa que converta metros para centímetros:

metros = float(input("Digite o valor em metros: "))
centimetros = metros * 100
print(f"{metros} metros é igual a {centimetros} centímetros")

# Faça um programa que peça o raio de um círculo, calcule e mostre sua área:

import math

raio = float(input("Digite o raio do círculo: "))
formula = math.pi * (raio ** 2)
print(f"A área do círculo com raio {raio} é: {formula}")

# Faça um programa que calcule a área de um quadrado, em seguida mostre o dobro desta área para o usuário.

lado = float(input("Digite o valor do lado do quadrado: "))
formula = lado ** 2
dobro = formula * 2
print(f"A área do quadrado é: {formula} e o dobro da área é: {dobro}")

# Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.

ganho = float(input("Digite o quanto você ganha por hora: "))
horas = float(input("Digite o número de horas trabalhadas no mês:"))
salario = ganho * horas
print(f"O total do seu salário no mês é: R${salario:.2f}")

# Faça um programa que peça a temperatura em graus Fahrenheit, transforme e mostre a temperatura em graus Celsius.

fahrenheit = float(input("Digite a temperatura em graus Fahrenheit: "))

c = 5 * ((fahrenheit - 32) / 9)
print(f"A temperatura em graus Celsius é: {c:.2f}°C")

# Faça um programa que peça a temperatura em graus Celsius, transforme e mostre em graus Fahrenheit.

celsius = float(input("Digite a temperatura em graus Celsius: "))
F = (celsius * 9/5) + 32
print("A temperatura em graus Fahrenheit é: {:.2f}°F".format(F))