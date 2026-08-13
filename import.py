import math
import time
# conta = 0
# print("         CRIE A SUA CONTA")
# while conta == 0:
#     cadastroac = str(input("Digite a conta desejada: "))
#     cadastrose = str(input("Digite a senha desejada: "))
#     confirmar = str(input(f"Seu usuario é '{cadastroac}', e sua senha é '{cadastrose}', quer confirmar? ").lower())
#     if "s" in confirmar or "k" in confirmar:
#         conta += 1
#         print("Conta criada com sucesso!")
#     else:
#         print("Informe um novo usuario ou senha!")

# tentalogin = 0
# contas = 0

# while tentalogin >= 0:
#     login = str(input("Informe sua conta: "))
#     senha = str(input("Informe sua senha: "))
#     if login == cadastroac and senha == cadastrose:
#         print("Acesso confirmado! Bem vindo ao programa de contas!")
#         print("Digite dois números para começarmos a operar.")
#         numero1 = int(input("Digite o primeiro número: "))
#         numero2 = int(input("Digite o segundo número: "))
#         opcao1 = 0
#         while opcao1 != 5:
#             print("Escolhe uma operação com o numero: ")
#             print("1- Soma")
#             print("2- Multiplicar")
#             print("3- Qual o maior")
#             print("4- Divisão")
#             print("5- Sair do programa")
#             operar = str(input(f"Você escolheu como primeiro o {numero1} e o segundo {numero2}, qual operação deseja fazer? "))
#             if "1" in operar:
#                 print(f"A soma de {numero1} e {numero2} é {numero1 + numero2}")
#                 troca = str(input("Deseja trocar algum dos números? S/N").lower())
#             elif "2" in operar:
#                 print(f"A multiplicação de {numero1} e {numero2} é {numero1 * numero2}")
#                 troca = str(input("Deseja trocar algum dos números? S/N").lower())
#             elif "3" in operar:
#                 print(f"O maior de {numero1} e {numero2} é {max(numero1,numero2)}")
#                 troca = str(input("Deseja trocar algum dos números? S/N").lower())
#             elif "4" in operar:
#                 print(f"A divisão de {numero1} e {numero2} é {numero1 / numero2}")
#                 troca = str(input("Deseja trocar algum dos números? S/N").lower())
#             elif "5" in operar:
#                 print("Fim Do Programa!")
#                 tentalogin = -1
#                 break
#             if "s" in troca:
#                 trocar = str(input("Informe o número que você deseja trocar: "))
#                 if "1" in trocar:
#                     trocando = int(input("Informe o novo valor do primeiro número: "))
#                     numero1 = trocando
#                 if "2" in trocar:
#                     trocando = int(input("Informe o novo valor do segundo número: "))
#                     numero2 = trocando

#             else:
#                 print("Você não digitou um número correto para operar!")
        

#     else:
#         tentalogin += 1
#         print("Acesso negado, usuario ou senha incorretos!")
#         if tentalogin == 2:
#             print("Você tem somente mais uma chance, tente novamente.")
#         elif tentalogin == 3:
#             print("Suas tentativas acabaram, tente novamente mais tarde.")
#             break

    




# import math

# numero = int(input("Digite um número: "))
# numero_cima = math.ceil(numero)
# numero_baixo = math.floor(numero)
# raiz = math.sqrt(numero)
# fatorial = math.factorial(numero)


# print("O número arredondado para cima é:{}".format(numero_cima))
# print("O número arredondado para baixo é:{}".format(numero_baixo))
# print(f"O fatorial de {numero} é {fatorial}, e a raiz é {raiz}")

# nome = input("Digite o seu nome: ")
# idade = int(input("Digite a sua idade: "))
# altura = float(input("Digite a sua altura: "))

# print("Ola {}, voce tem {} anos e tem {} de altura".format(nome,idade,altura))
# print(f"Ola {nome}, voce tem {idade} anos e tem {altura} de altura")

# blocos = int(input("Informe a quantia de blocos: "))
# altura = 0
# blocos_necessarios = 1

# while blocos >= blocos_necessarios:
#     blocos -= blocos_necessarios
#     altura += 1
#     blocos_necessarios += 1

# print(f"A altura é: {altura}")

# for contador in range(10):
#     print(f"valor = {contador}")

# for contador in range(1,10):
#     print(f"valor = {contador}")

# for contador in range(0,10):
#     print(f"valor = {contador}")

# for contador in range(0,10,2):
#     print(f"valor = {contador}")

# for contador in range(10,0,-1):
#     print(f"valor = {contador}")

# n = int(input("Digite um número: "))
# for i in range(n+1):
#     print('Valor = ', i)

# inicio = int(input("Digite um número para iniciar: "))
# fim = int(input("Digite um número para finalizar: "))
# pula = int(input("Digite um número para pular: "))

# for i in range(inicio, fim+1, pula):
#     print("Valor = ", i)
# print("fim")

# print("\033[34mTexto azul\033[0m")

# palavra = "Bruno"
# contador = 0
# for i in palavra:
#     contador += 1
#     if contador == len(palavra):
#         print(i,end= "*")
#     elif contador == 1:
#         print(f"*{i}", end="")
#     else:
#         print(i,end="")

# i = 0
# while i < 10:
#     print("Valor = ", i)
#     i+= 1

# for i in range(10):
#     print("Valor = ", i)

# for i in range(5,0,-1):
#     print("Ano novo em ", i)
#     time.sleep(1)
# print("Feliz Ano Novo!")

# print("Todos os números pares até 100: ")
# time.sleep(2)
# for i in range(2,101,2):
#     time.sleep(0.5)
#     print(i,"é número par")

# numeros = []

# for i in range(1,500,3):
#     conta = sum(numeros)
#     numeros.append(i)

# print(f"A soma de todos os números de 1 até 500 com multiplo de 3 é {conta}")

# tabuada = int(input("Qual o número que você deseja saber a tabuada?: "))
# print(f"A tabuada de {tabuada} é: ")
# for i in range(1,11):
#     conta = i * tabuada
#     print(f"{tabuada} vezes {i}")
#     print(conta)

# numero = int(input("Digite um número e eu direi se ele é primo ou não: "))
# primo = 2

# while primo < numero:
#     if numero % primo == 0:
#         print("O número não é primo.")
#         break
#     primo += 1

# if primo == numero:
#     print("Ele é primo.")

# numero = int(input("Digite um número: "))
# divisor = 0

# for i in range(1, numero + 1):
#     if numero % i == 0:
#         divisor += 1

# if divisor == 2:
#     print(f"{numero} é um número primo.")
# else:
#     print(f"{numero} não é um número primo.")

# blocos = int(input("Informe a quantia de blocos: "))
# altura = 0
# blocos_necessarios = 1

# while blocos >= blocos_necessarios:
#     blocos -= blocos_necessarios
#     altura += 1
#     blocos_necessarios += 1

nome = []
idade = []
sexo = []

for i in range(1, 3):
    nomes = str(input(f"Digite o nome da {i}º pessoa: "))
    idades = int(input(f"Digite a idade da {i}º pessoa: "))
    mouf = str(input(f"Digite se a {i}º pesssoa é M/F: ").lower())
    nome.append(nomes)
    idade.append(idades)
    sexo.append(mouf)

maiorid = idade.index(max(idade))
print(f"A media de idade é {sum(idade) / len(idade)}")
print(f"O nome do Homen mais velho é {nome[maiorid]}")

menorm = []
for n, i, s in zip(nome, idade, sexo):
    if i <= 20 and s == "f":
        menorm.append(n)
print(menorm)

# nomes = []
# idades = []
# pessoas = zip(nomes, idades)

# for i in range(1, 4):
#     nome = str(input(f"Digite o {i}° nome: "))
#     idade = int(input(F"Digite a {i}° idade: "))
#     nome.append(nomes)
#     idade.append(idades)

# print(f"")

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f"Digite o peso da {i}° pessoa (em kg): "))

    if i == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        

