generos_livro_a = { "fantasia", "aventura", "mistério"}
generos_livro_b = { "fantasia", "romance", "mistério"}

print(generos_livro_a | generos_livro_b) # união
print(generos_livro_a & generos_livro_b )
print(generos_livro_a - generos_livro_b ) # exclusivos do livro a
print(generos_livro_b - generos_livro_a) # exclusivo do livro b