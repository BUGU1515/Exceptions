qtd = int(input("Quantas notas? "))
soma = 0
for _ in range(qtd):
    soma += float(input("Nota: "))

media = soma / qtd
print("Média:", media)

try:
    print(dobro(valor))
except ValueError:
    print("Erro: Digite um número")