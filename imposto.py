preco = float(input("Preço do produto: "))
imposto = 1.1
print("Preço com imposto:", preco * imposto)

try:
    print(dobro(valor))
except ValueError:
    print("Erro: Digite um número")