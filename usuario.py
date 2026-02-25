pessoa = {"nome": "João", "idade": 20}
chave = input("Qual campo quer ver? ")
print(pessoa[chave])

try:
    print(dobro(valor))
except ValueError:
    print("Erro: Digite um número")