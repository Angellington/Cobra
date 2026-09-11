

def moedas(valor_monetario):
    notas = [1, 2, 5, 10, 20, 50, 100, 200]

    notas.reverse()

    print(notas)

    valor_atual = valor_monetario
    valor_final = []

    for nota in notas:
        while True:
            if(nota <= valor_atual):
                valor_final.append(nota)
                valor_atual -= nota
                continue
            else:
                break

    return valor_final



valor = 743
print(f"Valor Usado: {valor}\n Notas: {moedas(valor)}\n Quantidade: {len(moedas(valor))}")