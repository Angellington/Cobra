from dataclasses import dataclass, field


# @dataclass
# class SteamGame:
#     nome: str
#     horas_jogadas: float = 0.0

# jogo_a = SteamGame("Stardew Valley", 0.7)
# jogo_b = SteamGame("Hades", 3.4)

# print(jogo_a.nome)
# print(jogo_b.horas_jogadas)

# jogo_c = SteamGame("Hades", 2.5)
# jogo_d = SteamGame("Hades", 2.5)

# print(jogo_c == jogo_d)
# print(jogo_c is jogo_d)

# jogo_c.horas_jogadas += 1



# print(jogo_c.horas_jogadas)
# print(jogo_d.horas_jogadas)



# print(jogo_c == jogo_d)

@dataclass
class SteamGame:
    nome: str
    horas_jogadas: float = 0.0


    def __post_init__(self) -> None:
        if not self.nome.strip():
            raise ValueError("O nome não pode ficar vazio.")

        if self.horas_jogadas < 0:
            raise ValueError("As horas não podem ser negativas")

    def registrar_sessao(self, horas: float) -> None:
        if horas <= 0:
            raise ValueError("A sessão deve ter duração positiva.")
        self.horas_jogadas += horas

    def resumo(self) -> str:
        return f"{self.nome} - {self.horas_jogadas:.1f} horas jogadas"

@dataclass
class BibliotecaSteam:
    jogos: list[SteamGame] = field(default_factory=list)

    def adicionar_jogo(self, jogo: SteamGame) -> None:
        self.jogos.append(jogo)

    def listar_jogos(self) -> list[str]:
        return [jogo.resumo() for jogo in self.jogos]

try:
    hades = SteamGame(" ")
except ValueError as Erro:
    print("Erro: ", Erro)

try:
    hades1 = SteamGame("Hades", 0)
except ValueError as Erro:
    print("Erro: ", Erro)

try:
    hades2 = SteamGame("Hades", -2)
except ValueError as Erro:
    print("Error: ", Erro)

try:
    hades3 = SteamGame(" ", 2)
except ValueError as Erro:
    print("Error: ", Erro)

hades1.registrar_sessao(1.4)
print(hades1.resumo())

biblioteca_a = BibliotecaSteam()
biblioteca_b = BibliotecaSteam()

biblioteca_a.adicionar_jogo(hades1)

print(biblioteca_a.listar_jogos())
print(biblioteca_b.listar_jogos())

hades1.registrar_sessao(1)
print(biblioteca_a.listar_jogos())

biblioteca_a.adicionar_jogo(SteamGame("Stardew Valley", 3))

print(biblioteca_a.listar_jogos())
print(biblioteca_b.listar_jogos())

try:
    hades1.registrar_sessao(0)
except ValueError as Erro:
    print(Erro)

print(hades1.horas_jogadas)