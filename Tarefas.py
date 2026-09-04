import time
pessoas = []
tarefa = []

while True:
    print("1 - Adicionar pessoa")
    print("2 - Adicionar tarefa")
    print("3 - Sair")
    escolha = int(input("Escolha uma opçao com seu número: "))

    if escolha == 1:
        addpessoa = str(input("Digite o nome da pessoa: "))
        pessoas.append(addpessoa)
    elif escolha == 2:
        addtarefa = str(input("Digite a tarefa: "))
        tarefa.append(addtarefa)
    elif escolha == 3:
        break

while True:
    print("1 - Listar pessoas")
    print("2 - Listar tarefas")
    print("3 - Sair")
    escolha = int(input("Escolha uma opçao com seu número: "))

    if escolha == 1:
        print("Pessoas cadastradas:")
        for i in pessoas:
            print(i)
        else:
            print("Nenhuma pessoa adicionada.")
    elif escolha == 2:
        print("Tarefas cadastradas:")
        for i in tarefa:
            print(i)
        else:
            print("Nenhuma tarefa adicionada.")
    elif escolha == 3:
        break

while True:
    print("1 - Remover pessoa")
    print("2 - Remover tarefa")
    print("3 - Sair")
    escolha = int(input("Escolha uma opçao com seu número: "))

    if escolha == 1:
        rpessoa = str(input("Digite o nome da pessoa que deseja remover: "))
        if rpessoa in pessoas:
            pessoas.remove(rpessoa)
            print(f"{rpessoa} foi removido(a) com sucesso.")
        else:
            print(f"{rpessoa} não encontrado(a) na lista de pessoas.")

    elif escolha == 2:
        rtarefa = str(input("Digite a tarefa que deseja remover: "))
        if rtarefa in tarefa:
            tarefa.remove(rtarefa)
            print(f"{rtarefa} foi removido(a) com sucesso.")
        else:
            print(f"{rtarefa} não encontrado(a) na lista de tarefas.")

    elif escolha == 3:
        break
    
pessoas_taref = {}
# "tarefa": t_escolhida, "Concluida": False

while True:
    print("1 - Dar tarefa para uma pessoa")
    print("2 - Remover tarefa de uma pessoa")
    print("3 - Listar tarefas de uma pessoa")
    print("4 - Dar ok para uma tarefa")
    print("5 - Sair")
    escolha_t = int(input("Escolha uma opçao com seu número: "))

    if escolha_t == 1:
        if not pessoas:
            print("Nenhuma pessoa foi adicionada.")
            continue
        elif not tarefa:
            print("Nenhuma tarefa foi adicionada.")
            continue
        while True:
            print("1 - Pessoas disponiveis")
            print("2 - Tarefas disponiveis")
            print("3 - Atribuir a tarefa")
            print("4 - Sair")
            escolha_pt = input(("Digite o numero correspondente a açao que quer fazer: "))
            if escolha_pt == "1":
                for p in pessoas:                            
                    print(f"Esta pessoa está disponivel: {p}")
                    print("-----------------------------------------------")
                    if p == len(pessoas):
                        continue
            if escolha_pt == "2":
                for t in tarefa:
                    print(f"Esta tarefa está disponivel: {t}")
                    print("-----------------------------------------------")
                    if t == len(tarefa):
                        continue
            if escolha_pt == "3":
                print("Primeiro escolha a pessoa que voce quer dar uma tarefa!")
                for i,p in enumerate(pessoas):
                    print(f"{i + 1} - {p} está disponivel")
                    print("-----------------------------------------------")
                    if i + 1 == len(pessoas):
                        recebe_p = int(input("Digite o numero correspondente da pessoa que voce quer dar uma tarefa: "))
                        if recebe_p < 1 or recebe_p > len(pessoas):
                            print("Voce digitou um numero que nao tem uma pessoa cadastrada")
                            continue
                        p_escolhida = pessoas[recebe_p - 1]
                        print(f"Voce escolheu a pessoa {p_escolhida}, agora escolha a sua tarefa")
                        for i,t in enumerate(tarefa):
                            print(f"{i + 1} - {t} disponivel: ")
                            print("-----------------------------------------------")
                            if i + 1 == len(tarefa):
                                recebe_t = int(input(f"Digite o numero correspondente da tarefa que voce quer dar para a {p_escolhida}: "))
                                if recebe_t < 1 or recebe_t > len(tarefa):
                                    print("Voce digitou um numero que nao tem uma tarefa cadastrada")
                                    continue

                                t_escolhida = tarefa[recebe_t - 1]
                                print(f"Voce escolheu a pessoa {p_escolhida}, agora escolha a sua tarefa")
                                pessoas_taref[p_escolhida] = {
                                   "tarefa": t_escolhida, "Concluida": False
                                }
                                print(pessoas_taref)
            if escolha_pt == "4":
                print("Saindo do atribuir tarefa.")
                print("-----------------------------------------------")
                break

    elif escolha_t == 2:
        if not pessoas_taref:
            print("Nenhuma tarefa foi adicionada")
            continue

        print("Pessoas que tem tarefas: ")
        for i,p in enumerate(pessoas_taref):
            print(f"{i + 1} - {p}")
        recebe_p = int(input("Digite o numero correspondente da pessoa que voce quer dar uma tarefa: "))
        if recebe_p < 1 or recebe_p > len(pessoas_taref):
            print("Voce digitou um numero que nao tem uma pessoa cadastrada")
        else:
            r_escolhido = list(pessoas_taref.keys())[recebe_p - 1]
            print(f"Removendo: Pessoa escolhida: {r_escolhido} Tarefa: {pessoas_taref[r_escolhido]["tarefa"]}")
            del pessoas_taref[r_escolhido]
            continue

    elif escolha_t == 3:
        if not pessoas_taref:
            print(f"Nao tem nenhuma pessoa com alguma tarefa a fazer")
            print("-----------------------------------------------")
            continue
        for i, (n, t) in enumerate(pessoas_taref.items()):
            print(f"{i + 1} - {n}: {t['tarefa']} - {t['Concluida']}")
            print("-----------------------------------------------")
        continue
    elif escolha_t == 4:
        if not pessoas_taref:
            print(f"Nao tem nenhuma pessoa com alguma tarefa a fazer")
            print("-----------------------------------------------")
            continue
        while True:
            inconcluido = {}
            for k,d in pessoas_taref.items():
                if d["Concluida"] is False:
                    inconcluido[k] = d.copy() 
                elif k == len(pessoas_taref):
                    continue
            break

        print("Pessoas que nao estao com tarefas feitas")
        for i, (n, t) in enumerate(inconcluido.items()):
            print(f"{i + 1} - {n}")
            print(f"Tarefa: {t['tarefa']}")
            print("-----------------------------------------------")
            if i + 1 == len(inconcluido):
                continue
        darok = int(input(f"Digite o numero da pessoa que quer dar ok para sua tarefa: "))
        if darok < 1 or darok > len(inconcluido):
            print("Voce digitou um numero que nao tem uma pessoa cadastrada")
        else:
            ok = list(inconcluido.keys())[darok - 1]
            print(f"Tarefa de {ok} marcada como concluida!")
            pessoas_taref[ok]["Concluida"] = True
            del inconcluido[ok]
            continue

    elif escolha_t == 5:
        print("Encerrando o sistema de tarefas" + "." * i, end="\r")
        time.sleep(1)
        print("Encerrando o sistema de tarefas...")
        break
