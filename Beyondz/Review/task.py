# 1. What's difference between return and print
## return is the function return, to return a value to scope of function. print cannot do it, cuz just print the value on computer, but not return a value.

# 2. WHat if  __name__ == "__main__" controll
## Eles controlam o escopo principal de um módulo, garantindo assim que a execução daquele módulo se restrinja a si mesmo, sem que o mesmo ou demais sejam executados ao serem importados.

## sorte(catalogo, ...) altera a ordem do catalogo original? Sim caso seja definido uma nova variável, não pois não altera a variavel do catalogo origiunal.

## 4. Se uma função recebe uma lista e executa append, a lista externa muda? SIM! MUDA! POis está sendo adicionado mais um

## 5. O método .strip()




from typing import Type

from catalogo_operacoes import buscar_por_id, calcular_quantidade_paginas_totais, criar_livro, filtrar_por_status, calcalar_media


catalogo = []

novo_livro = criar_livro(1, "Flor do Luar", 32 )
novo_livro_2 = criar_livro(2, "Lunis", 123 )
novo_livro_3 = criar_livro(3, "The Last Melancholy", 2300 )
novo_livro_4 = criar_livro(4, "Um Livro para a Garota B", 232 )
novo_livro_5 = criar_livro(5, "Flor do Luar 2", 64 )

print("Novo livro: ", novo_livro)
catalogo.append(novo_livro)
catalogo.append(novo_livro_2)
catalogo.append(novo_livro_3)
catalogo.append(novo_livro_4)
catalogo.append(novo_livro_5)

print("Catalogo", catalogo)


print(calcular_quantidade_paginas_totais(catalogo))  # 480
print(calcalar_media(catalogo))                     # 160.0
print(buscar_por_id([], 1))                         # None
print(filtrar_por_status([], "Lendo"))              # []
print(filtrar_por_status(catalogo, " concluído "))  # livro Lunis