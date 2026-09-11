from copy import deepcopy

original = [["Lunis", "Flor do Luar"], ["Fantasia"]]
copia = deepcopy(original)

copia[0].append("The Last Melancholy")
print(original)
print(copia)