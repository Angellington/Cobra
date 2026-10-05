import os

try:
    from .config import Options, criar_despesa, DESPESA_ROUTE
    from .despesas import adicionar_no_arquivo, deletar_despesa, listar_despesas
except ImportError:
    from config import Options, criar_despesa, DESPESA_ROUTE
    from despesas import adicionar_no_arquivo, deletar_despesa, listar_despesas

def exibir_menu() -> None:
    # os.system("clear")
    print("1 - Deseja adicionar uma despesa?")
    print("2 - Deseja listar a despeas?")
    print("3 - Deseja deletar uma despesa? ")
    print("4 - Sair")

def main() -> None:
    print("Você irá adicionar despesa")
    while True:
        exibir_menu()
        try:
            decisao = Options(int(input(": ")))
        except ValueError:
            print("Digite o correto!")
            continue

        match decisao:
            case Options.ADICIONAR:
                despesa = criar_despesa(DESPESA_ROUTE)
                adicionar_no_arquivo(despesa=despesa, path=DESPESA_ROUTE)
            case Options.LISTAR:
                listar_despesas(DESPESA_ROUTE)
            case Options.DELETAR:
                deletar_despesa(DESPESA_ROUTE)
            case Options.SAIR:
                print("Saindo...")
                break

        # despesa = criar_despesa(DESPESA_ROUTE)
        # adicionar_no_arquivo(despesa=despesa, path=DESPESA_ROUTE)


if __name__ == "__main__":
    main()