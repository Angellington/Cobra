from arquivo_operacoes import ler_titulos, salvar_titulos

def main():
    titulos = ["1984", "Lunis", "Flor do Luar", "The Last Melancholy"]

    salvar_titulos(titulos=titulos)

    titulos_lidos = ler_titulos()
    print(titulos_lidos)

if __name__ == "__main__":
    main()