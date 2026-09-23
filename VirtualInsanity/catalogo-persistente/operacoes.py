from pathlib import Path
from config import PASTA_DADOS, PASTA_PROJETO, ARQUIVOS_OBRAS

def obras_validation(obras):
    if not isinstance(obras, list):
        raise ValueError("Envie uma lista")
    if not obras:
        raise ValueError("Você precisa colocar ao menos uma obra")

    return [obra.strip() for obra in obras]


def obra_validation(obra):
    if not obra:
        raise ValueError("Envie-me algum valor")
    return obra.strip()


def obra_convertion(obra):
    if isinstance(obra, int):
        obra = str(obra)
    if isinstance(obra, list):
        return obras_validation(obra)
    elif isinstance(obra, str):
        return [obra_validation(obra)]
    else:
        raise ValueError("Não pode ser nulo")


def salvar_obras(obras):
    obras = obras_validation(obras=obras)
    PASTA_DADOS.mkdir(exist_ok=True)
    with ARQUIVOS_OBRAS.open("w", encoding="utf-8") as arquivo:
        for obra in obras:
            arquivo.write(obra + "\n")


def ler_obras(path):
    if path.exists():
        with path.open("r", encoding="utf-8") as arquivo:
            return [linha.strip() for linha in arquivo if linha.strip()]
    return []


def adicionar_obra(obra):
    novas_obras = obra_convertion(obra=obra)
    obras_existentes = ler_obras(ARQUIVOS_OBRAS)
    existentes_lower = {o.lower() for o in obras_existentes}
    adicionou_alguma = False
    for nova in novas_obras:
        if nova.lower() not in existentes_lower:
            obras_existentes.append(nova)
            existentes_lower.add(nova.lower())
            adicionou_alguma = True
    if adicionou_alguma:
        salvar_obras(obras_existentes)

    return adicionou_alguma