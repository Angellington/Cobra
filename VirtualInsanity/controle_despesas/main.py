from config import criar_despesa
from despesas import adicionar_no_arquivo
from config import DESPESA_ROUTE

def main() -> None:
    print("Você irá adicionar despesa")
    
    despesa = criar_despesa(DESPESA_ROUTE)
    adicionar_no_arquivo(despesa=despesa, path=DESPESA_ROUTE)


if __name__ == "__main__":
    main()