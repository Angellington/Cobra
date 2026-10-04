import unittest

from catalogo import buscar_por_titulo, listar_titulos

class TestCatalogo(unittest.TestCase):
    def test_buscar_por_titulo(self):
        catalogo = [
            {
                "id": 1,
                "titulo": "Avatar: A Ascensão de Kyoshi",
                "autor": "F. C. Yee"
            },
            {
                "id": 2,
                "titulo": "1984",
                "autor": "George Orwell"
            }
        ]

        resultado = buscar_por_titulo(
            catalogo=catalogo,
            termo="kyoshi"
        )

        esperado = [
            catalogo[0]
        ]

        self.assertEqual(resultado, esperado)

    def test_busca_com_termo_vazio(self):
        catalogo = [
            {"id": 1, "titulo": "1984"}
        ]
        with self.assertRaises(ValueError):
            buscar_por_titulo(catalogo=catalogo, termo="")

    def test_listar_titulos(self):
        catalogo = [
            {"id": 1, "titulo": "Kyoshi"},
            {"id": 2, "titulo": "1984"}
        ]
        resultado = listar_titulos(catalogo=catalogo)

        self.assertEqual(resultado, ["Kyoshi", "1984"])

if __name__ == "__main__":
    unittest.main()