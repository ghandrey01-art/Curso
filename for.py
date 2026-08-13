# nome = []
# idade = []
# sexo = []
# maiorid = 0

# for i in range(1, 5):
#     nomes = str(input(f"Digite o nome da {i}º pessoa: "))
#     idades = int(input(f"Digite a idade da {i}º pessoa: "))
#     mouf = str(input(f"Digite se a {i}º pesssoa é M/F: ").lower())
#     nome.append(nomes)
#     idade.append(idades)
#     sexo.append(mouf)

# print(f"A media de idade é {sum(idade) / len(idade)}")

# hmaisv = []
# for n, i, s in zip(nome, idade, sexo):
#     if s == "m":
#         if idade > maiorid:
#             maiorid = idade
#             hmaisv.append(n)
# print(f"O nome do Homen mais velho é {hmaisv}")


# menorm = []
# for n, i, s in zip(nome, idade, sexo):
#     if i <= 20 and s == "f":
#         menorm.append(n)
#         if not menorm:
#             print(f"Não tem mulheres na lista!")
#         else:
#             print(f"O nome da mulher mais velha é {menorm}")

vogal = ["a","e","i","o","u"]
nome = str(input("Digite o seu nome: ").lower())
for i in nome:
    if i in vogal:
        continue
    print(i)