import json
from pathlib import Path
PASTA = Path(__file__).parent
ARQUIVO_ROUTE = PASTA / "livro.json"

def ler_json(ARQUIVO_ROUTE):
    if not ARQUIVO_ROUTE.exists():
        raise ValueError("Caminho inválido")

    try:
        with ARQUIVO_ROUTE.open("r", encoding="utf-8") as arquivo:
            return json.load(arquivo)
    except json.JSONDecodeError:
        raise ValueError("O arquivo possui JSON inválido")
    except OSError:
        raise ValueError("Não foi possível acessar o arquivo")

def main():

    livro = {
        "titulo": "1984",
        "autor": "George Orwell",
        "paginas": 328,
    }



    with ARQUIVO_ROUTE.open("w", encoding="utf-8") as arquivo:
        json.dump(livro, arquivo, indent=4)

    # Ler json
    livro_lido = ler_json(ARQUIVO_ROUTE)
    livro_lido.pop("ano", None)

    with ARQUIVO_ROUTE.open("w", encoding="utf-8") as arquivo:
        json.dump(livro_lido, arquivo, indent=4)
    print(livro_lido)

    

if __name__ == "__main__":
    main()
