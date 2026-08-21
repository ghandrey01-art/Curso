pessoas = []
lugar = []
tarefa = []

while True:
    print("1 - Adicionar pessoa")
    print("2 - Adicionar local")
    print("3 - Adicionar tarefa")
    print("4 - Sair")
    opcao = int(input("Escolha uma opçao com seu número: "))

    if opcao == 1:
        addpessoa = str(input("Digite o nome da pessoa: "))
        pessoas.append(addpessoa)
    elif opcao == 2:
        addlugar = str(input("Digite um local para a tarefa: "))
        lugar.append(addlugar)
    elif opcao == 3:
        addtarefa = str(input("Digite a tarefa: "))
        tarefa.append(addtarefa)
    elif opcao == 4:
        break

while True:
    print("1 - Listar pessoas")
    print("2 - Listar locais")
    print("3 - Listar tarefas")
    print("4 - Sair")
    opcao = int(input("Escolha uma opçao com seu número: "))

    if opcao == 1:
        print("Pessoas cadastradas:")
        for i in pessoas:
            print(i)
        else:
            print("Nenhuma pessoa adicionada.")
    elif opcao == 2:
        print("Locais cadastrados:")
        for i in lugar:
            print(i)
        else:
            print("Nenhum local adicionado.")
    elif opcao == 3:
        print("Tarefas cadastradas:")
        for i in tarefa:
            print(i)
        else:
            print("Nenhuma tarefa adicionada.")
    elif opcao == 4:
        break

# while True:
#     print("1 - Remover pessoa")
#     print("2 - Remover local")
#     print("3 - Remover tarefa")
#     print("4 - Sair")
#     opcao = int(input("Escolha uma opçao com seu número: "))

#     if opcao == 1:
#         rpessoa = str(input("Digite o nome da pessoa que deseja remover: "))
#         if rpessoa in pessoas:
#             pessoas.remove(rpessoa)
#             print(f"{rpessoa} foi removido(a) com sucesso.")
#         else:
#             print(f"{rpessoa} não encontrado(a) na lista de pessoas.")

#     elif opcao == 2:
#         rlugar = str(input("Digite o local que deseja remover: "))
#         if rlugar in lugar:
#             lugar.remove(rlugar)
#             print(f"{rlugar} foi removido(a) com sucesso.")
#         else:
#             print(f"{rlugar} não encontrado(a) na lista de locais.")

#     elif opcao == 3:
#         rtarefa = str(input("Digite a tarefa que deseja remover: "))
#         if rtarefa in tarefa:
#             tarefa.remove(rtarefa)
#             print(f"{rtarefa} foi removido(a) com sucesso.")
#         else:
#             print(f"{rtarefa} não encontrado(a) na lista de tarefas.")

#     elif opcao == 4:
#         break

while True:
    print("1 - Dar tarefa para uma pessoa")
    print("2 - Remover tarefa de uma pessoa")
    print("3 - Listar tarefas de uma pessoa")
    print("4 - Dar ok para uma tarefa")
    print("5 - Ver quais tarefas foram feitas")
    print("6 - Sair")
    opcao = int(input("Escolha uma opçao com seu número: "))

    if opcao == 1:
        for i in pessoas:
            print(f"{pessoas.index(i)} - {i}")
            pessoa_n = str(input("Digite o número da pessoa que deseja dar uma tarefa: "))

            if pessoa_n in pessoas:
                dar_tarefa = str(input("Digite o número da tarefa que deseja dar: "))
                if dar_tarefa in tarefa:
                    print(f"Tarefa {dar_tarefa} precisa ser feita por {pessoas}.")
                else:
                    print(f"Tarefa {dar_tarefa} nao encontrada na lista de tarefas.")
        else:
            if not pessoas:
                print("Nenhuma pessoa adicionada.")
            elif i != pessoas:
                print(f"Pessoa {i} nao encontrada na lista de pessoas.")