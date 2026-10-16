# class SteamGame:
#     pass

# hades = SteamGame()
# stardew_valley = SteamGame()



class SteamGame:
    def __init__(self, nome: str) -> None:
        if not nome.strip():
            raise ValueError("O nome do jogo não pode ficar vazio")
        
        self.nome = nome
        self.horas_jogadas = 0.0

    def registrar_sessao(self, horas: float) -> None:
        if horas <= 0:
            raise ValueError("A duração da sessão deve ser positiva")
        self.horas_jogadas += horas

    def resumo(self) -> str:
        return f"{self.nome}: {self.horas_jogadas} horas jogadas"

hades = SteamGame("Hades")
stardew_valley = SteamGame("Stardew Valley")

class Manga:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.paginas_lidas = 0


vagabond = Manga("Vagabond")
hades.registrar_sessao(2.5)

print("hades", hades.horas_jogadas)
texto = hades.resumo()
print("texto", texto)


stardew_valley.registrar_sessao(1.5)

print(hades.horas_jogadas)
print(stardew_valley.horas_jogadas)

try:
    hades.registrar_sessao(0)
except ValueError as erro:
    print(erro)

try:
    stardew_valley.registrar_sessao(-1)
except ValueError as erro:
    print(erro)


try:
    novo_jogo = SteamGame(" ")
except ValueError as erro:
    print("Erro: ", erro)