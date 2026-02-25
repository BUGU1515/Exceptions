nomes = ["Arthur", "Gabriel", "Enzo", "Julia"]

try:
    i = int(input("Indique um número para sortear uma pessoa? "))
    print("Nome:", nomes[i])

except ValueError:
    print("Erro: Digite apenas nomes.")