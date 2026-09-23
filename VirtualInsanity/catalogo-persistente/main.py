from pathlib import Path
from operacoes import adicionar_obra, ler_obras, salvar_obras
from config import ARQUIVOS_OBRAS

def main():
    obras = ["Lunis", "Flor do Luar", "Projeto B", "The Last Melancholy"]
    salvar_obras(obras=obras);
    print(ler_obras(ARQUIVOS_OBRAS))
    obra_nova = ["Macaronii"]


    adicionar_obra(obra_nova)




if __name__ == "__main__":
    main()
    