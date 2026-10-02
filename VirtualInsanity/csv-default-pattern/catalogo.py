from pathlib import Path
from datetime import date
import csv

catalogo = [
    {
        "id": 1,
        "titulo": "Avatar: A Ascensão de Kyoshi",
        "autor": "F. C. Yee",
        "paginas": 448,
        "avaliacao": 4.8,
        "data_publicacao": "2020-07-21"
    },
    {
        "id": 2,
        "titulo": "Avatar: O Despertar de Roku",
        "autor": "Randy Ribay",
        "paginas": 368,
        "avaliacao": 4.7,
        "data_publicacao": "2023-08-21"
    }
]

data_exportacao = date.today().isoformat()
for livro in catalogo:
    livro["data_exportacao"] = data_exportacao

campos = ["id", "titulo", "autor", "paginas", "avaliacao", "data_publicacao", "data_exportacao"]

PASTA_PROJETO = Path(__file__).parent
PASTA_DADOS = PASTA_PROJETO / "dados"
ARQUIVO_CATALOGO = PASTA_DADOS / "catalogo.csv"

PASTA_DADOS.mkdir(exist_ok=True, parents=True)



with ARQUIVO_CATALOGO.open("w", encoding="utf-8", newline="") as arquivo:
    escritor = csv.DictWriter(arquivo, fieldnames=campos)
    escritor.writeheader()
    escritor.writerows(catalogo)

with ARQUIVO_CATALOGO.open("r", encoding="utf-8", newline="") as arquivo:
    leitor = csv.DictReader(arquivo)
    catalogo_lido = list(leitor)

for livro in catalogo_lido:
    livro["id"] = int(livro["id"])
    livro["paginas"] = int(livro["paginas"])
    livro["avaliacao"] = float(livro["avaliacao"])

print(catalogo_lido)
print(type(catalogo_lido[0]["id"]))
print(type(catalogo_lido[0]["paginas"]))
print(type(catalogo_lido[0]["avaliacao"]))

total_paginas = sum(
    livro["paginas"]
    for livro in catalogo_lido
)

print(total_paginas)