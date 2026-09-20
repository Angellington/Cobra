from catalogo_operacoes import (
    catalogo_validation, buscar_por_id, filtrar_por_status, listar_livros
)

catalogo = [
    {
        "id": 1,
        "titulo": "LUNIS",
        "autor": "A. M. Silva",
        "ano": 2021,
        "genero": "Fantasia",
        "status": "disponivel",
        "nota": 4.5,
        "emprestado_para": None,
        "vezes_emprestado": 12,
        "localizacao": "Estante A - Prateleira 2"
    },
    {
        "id": 2,
        "titulo": "TLM",
        "autor": "R. Costa",
        "ano": 2019,
        "genero": "Ficção Científica",
        "status": "emprestado",
        "nota": 4.8,
        "emprestado_para": "Maria",
        "vezes_emprestado": 27,
        "localizacao": "Estante B - Prateleira 1"
    },
    {
        "id": 3,
        "titulo": "Flor do Luar",
        "autor": "C. Andrade",
        "ano": 2023,
        "genero": "Romance",
        "status": "reservado",
        "nota": 4.2,
        "emprestado_para": "João",
        "vezes_emprestado": 5,
        "localizacao": "Estante C - Prateleira 3"
    },
    {
        "id": 4,
        "titulo": "O Último Verão",
        "autor": "D. Martins",
        "ano": 2020,
        "genero": "Drama",
        "status": "em manutenção",
        "nota": 3.9,
        "emprestado_para": None,
        "vezes_emprestado": 8,
        "localizacao": "Estante A - Prateleira 4"
    },
    {
        "id": 5,
        "titulo": "Código Abissal",
        "autor": "E. Ferraz",
        "ano": 2022,
        "genero": "Suspense",
        "status": "disponivel",
        "nota": 4.0,
        "emprestado_para": None,
        "vezes_emprestado": 15,
        "localizacao": "Desconhecida"
    }
]

livro_existente = buscar_por_id(catalogo, 10)
print("livro existente", livro_existente)

todos_livros = listar_livros(catalogo)
print("Todos os Livros", todos_livros)

status_livro = filtrar_por_status(catalogo=catalogo, status="disponivel")
print("Status Livro", status_livro)