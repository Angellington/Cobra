from catalogo import salvar_catalogo, ler_catalogo, todos_os_livros, maior_avaliacao
from config import ARQUIVO_NOVO_CATALOGO, PASTA_DADOS, ARQUIVO_CATALOGO

def main():
    catalogo_avatar = [
    {
        "id": 1,
        "titulo": "Avatar: A Ascensão de Kyoshi",
        "autor": "F. C. Yee",
        "paginas": 448,
        "avaliacao": None
    },
    {
        "id": 2,
        "titulo": "Avatar: A Sombra de Kyoshi",
        "autor": "F. C. Yee",
        "paginas": 352,
        "avaliacao": None
    },
    {
        "id": 3,
        "titulo": "Avatar: A Alvorada de Yangchen",
        "autor": "F. C. Yee",
        "paginas": 336,
        "avaliacao": None
    },
    {
        "id": 4,
        "titulo": "Avatar: O Legado de Yangchen",
        "autor": "F. C. Yee",
        "paginas": 368,
        "avaliacao": None
    },
    {
        "id": 5,
        "titulo": "Avatar: O Despertar de Roku",
        "autor": "Randy Ribay",
        "paginas": 368,
        "avaliacao": None
    }
    ]   

    catalogo_algo = [
    {
    "id": 1,
    "titulo": "Avatar: A Ascensão de Kyoshi",
    "autor": "F. C. Yee",
    "genero": [
        "Fantasia", "Aventura", "Drama"
    ],
    "paginas": 448,
    "avaliacao": None },
    {
        "id": 2,
        "titulo": "Algoritmos: Estruturas de Dados e Análise",
        "autor": "Mark Allen Weiss",
        "paginas": 832,
        "avaliacao": 4.0
    }
    ]

    salvar_catalogo(catalogo=catalogo_avatar)
    catalogo_recuperado = ler_catalogo(ARQUIVO_CATALOGO)
    for livro in catalogo_recuperado:
        print(livro["titulo"])
    salvar_catalogo(catalogo=catalogo_algo, pasta_dados=ARQUIVO_NOVO_CATALOGO)

    novo_catalogo_ler = ler_catalogo(ARQUIVO_NOVO_CATALOGO)

    print(todos_os_livros(pasta_dados=ARQUIVO_NOVO_CATALOGO))

    print(maior_avaliacao(pasta_dados=ARQUIVO_NOVO_CATALOGO))

if __name__ == "__main__":
    main()