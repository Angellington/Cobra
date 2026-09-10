perfil_leito = {
    "nome": "Wellington",
    "idade": 21,
    "livros_lidos": 3,
    "estudando": True,
}

print(perfil_leito["nome"])
perfil_leito["livros_lidos"] = 10
perfil_leito["cidade"] = "Guaramiranga"
print("perfil leito", perfil_leito)

print(perfil_leito.get("nome", "Nome não encontrado"))

for key, value in perfil_leito.items():
    print(f"{key}: {value}")

del perfil_leito["cidade"]

print(perfil_leito)

print(perfil_leito.get("email", "Email não cadastrado"))