import time
pessoas = []
tarefa = []
pessoas_taref = {}

print("BEM VINDO AO SISTEMA DE TAREFAS")
while True:
    print("1 - Pessoas")
    print("2 - Tarefas")
    print("3 - Ações")
    print("4 - Sair")
    escolha = int(input("Escolha uma opçao com seu número: "))

############################################################################################

    if escolha == 1:
        print("===============================================")
        print("=============== PAINEL PESSOAS ================")
        print("===============================================")
        while True:
            print("1 - Adicionar pessoa")
            print("2 - Listar pessoas")
            print("3 - Remover pessoa")
            print("4 - Sair")
            escolha_p = int(input("Escolha uma opçao com seu número: "))
            if escolha_p == 1:
                addpessoa = str(input("Digite o nome da pessoa: ")).lower()
                pessoas.append(addpessoa)
                print(f"Pessoa {addpessoa} adicionada com sucesso!")
            elif escolha_p == 2:
                print("Pessoas cadastradas:")
                if not pessoas:
                    print("Nenhuma pessoa adicionada.")
                    continue
                else:
                    for i in pessoas:
                        print(i)
                
            elif escolha_p == 3:
                if not pessoas:
                    print("Nenhuma pessoa foi adicionada.")
                    continue
                else:
                    for i in pessoas:
                        print(f"{i} Pode ser removido")
                    rpessoa = str(input("Digite o nome da pessoa que deseja remover: ")).lower()
                    if rpessoa in pessoas:
                        pessoas.remove(rpessoa)
                        print(f"{rpessoa} foi removido(a) com sucesso.")

            elif escolha_p == 4:
                for i in range(3):
                    print("Encerrando o painel de pessoas" + "." * i, end="\r")
                    time.sleep(1)
                print("Encerrando o sistema de pessoas...")
                break

############################################################################################

    elif escolha == 2:
        print("===============================================")
        print("=============== PAINEL TAREFAS ================")
        print("===============================================")
        while True:
            print("1 - Adicionar tarefa")
            print("2 - Listar tarefas")
            print("3 - Remover tarefa")
            print("4 - Sair")
            escolha_t = int(input("Escolha uma opçao com seu número: "))
            if escolha_t == 1:
                addtarefa = str(input("Digite a tarefa: ")).lower()
                tarefa.append(addtarefa)
                print(f"Tarefa {addtarefa} adicionada com sucesso!")
            elif escolha_t == 2:
                print("Tarefas cadastradas:")
                if not tarefa:
                    print("Nenhuma tarefa adicionada.")
                    continue
                else:
                    for i in tarefa:
                        print(i)
            elif escolha_t == 3:
                for i in tarefa:
                    print(i)
                else:
                    print("Nenhuma tarefa adicionada.")
                rtarefa = str(input("Digite a tarefa que deseja remover: ")).lower()
                if rtarefa in tarefa:
                    tarefa.remove(rtarefa)
                    print(f"{rtarefa} foi removido(a) com sucesso.")
                else:
                    print(f"{rtarefa} não encontrado(a) na lista de tarefas.")
            elif escolha_t == 4:
                for i in range(3):
                    print("Encerrando o painel de tarefas" + "." * i, end="\r")
                    time.sleep(1)
                print("Encerrando o painel de tarefas...")
                break
            
############################################################################################

    elif escolha == 3:
        print("===============================================")
        print("=============== PAINEL AÇÕES ================")
        print("===============================================")
        while True:
            print("1 - Dar tarefa para uma pessoa")
            print("2 - Remover tarefa de uma pessoa")
            print("3 - Listar tarefas de uma pessoa")
            print("4 - Dar ok para uma tarefa")
            print("5 - Sair")
            escolha_a = int(input("Escolha uma opçao com seu número: "))

            if escolha_a == 1:
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
                                        if p_escolhida not in pessoas_taref:
                                            pessoas_taref[p_escolhida] = []

                                        pessoas_taref[p_escolhida].append({
                                        "tarefa": t_escolhida, "Concluida": False
                                        })
                                        print(pessoas_taref)
                    if escolha_pt == "4":
                        print("Saindo do atribuir tarefa.")
                        print("-----------------------------------------------")
                        break

            elif escolha_a == 2:
                if not pessoas_taref:
                    print("Nenhuma tarefa foi dada para alguem!")
                    continue
        
                print("Pessoas que tem tarefas: ")
                for i,p in enumerate(pessoas_taref):
                    print(f"{i + 1} - {p}")
                recebe_p = int(input("Digite o numero correspondente da pessoa que voce quer dar uma tarefa: "))
                if recebe_p < 1 or recebe_p > len(pessoas_taref):
                    print("Voce digitou um numero que nao tem uma pessoa cadastrada")
                else:
                    removept = list(pessoas_taref.keys())[recebe_p - 1]
                    tarefasremove = {}
                    print(f"Tarefas de {removept}:")
                    for n,t in pessoas_taref.items():
                        if n == removept:
                            tarefasremove[len(tarefasremove) + 1] = (n, t)

                    for i, (n, t) in tarefasremove.items():
                        print(f"{i} - {t['tarefa']}")

                    recebe_t = int(input("Digite o numero da tarefa que deseja remover: "))
                    if recebe_t < 1 or recebe_t > len(tarefasremove):
                        print("Voce digitou um numero de tarefa invalido")
                        continue
                    else:
                        n_remove, t_remove = tarefasremove[recebe_t]
                        for n,t in list(pessoas_taref.items()):
                            if n == n_remove and t["tarefa"] == t_remove["tarefa"]:
                                del pessoas_taref[n]
                                print(f"Tarefa {t_remove['tarefa']} removida de {n_remove}.")
                                break

            elif escolha_a == 3:
                if not pessoas_taref:
                    print("Nao tem nenhuma pessoa com alguma tarefa a fazer")
                    print("-----------------------------------------------")
                    continue

                print("Pessoas que tem tarefas:")
                for i, n in enumerate(pessoas_taref):
                    print(f"{i + 1} - {n}")

                lista_p = int(input("Digite o numero da pessoa que deseja consultar: "))

                if lista_p < 1 or lista_p > len(pessoas_taref):
                    print("Voce digitou um numero que nao tem uma pessoa cadastrada")
                    continue

                pessoa_escolhida = list(pessoas_taref.keys())[recebe_p - 1]

                print("-----------------------------------------------")
                print(f"Tarefas de {pessoa_escolhida}:")

                for i, t in enumerate(pessoas_taref[pessoa_escolhida]):
                    print(f"{i + 1} - {t['tarefa']} - Concluida: {t['Concluida']}")

                print("-----------------------------------------------")

            elif escolha_a == 4:
                if not pessoas_taref:
                    print("Nao tem nenhuma pessoa com alguma tarefa a fazer")
                    print("-----------------------------------------------")
                    continue

                inconcluido = {}

                for pessoa, tarefas in pessoas_taref.items():
                    tarefas_pendentes = []
                    for t in tarefas:
                        if t["Concluida"] is False:
                            tarefas_pendentes.append(t)
                    if tarefas_pendentes:
                        inconcluido[pessoa] = tarefas_pendentes
                if not inconcluido:
                    print("Todas as tarefas foram concluidas!")
                    print("-----------------------------------------------")
                    continue
                print("Pessoas que nao estao com tarefas feitas:")
                for i, pessoa in enumerate(inconcluido):
                    print(f"{i + 1} - {pessoa}")

                darok = int(input("Digite o numero da pessoa que quer dar ok para sua tarefa: "))
                if darok < 1 or darok > len(inconcluido):
                    print("Voce digitou um numero que nao tem uma pessoa cadastrada")
                    continue
                pessoa_escolhida = list(inconcluido.keys())[darok - 1]
                print("-----------------------------------------------")
                print(f"Tarefas nao concluidas de {pessoa_escolhida}:")
                for i, t in enumerate(inconcluido[pessoa_escolhida]):
                    print(f"{i + 1} - {t['tarefa']}")
                print("-----------------------------------------------")

                tarefa_ok = int(input("Digite o numero da tarefa que deseja dar ok: "))

                if tarefa_ok < 1 or tarefa_ok > len(inconcluido[pessoa_escolhida]):
                    print("Voce digitou um numero de tarefa invalido")
                    continue

                tarefa_escolhida = inconcluido[pessoa_escolhida][tarefa_ok - 1]

                tarefa_escolhida["Concluida"] = True

                print(f"Tarefa '{tarefa_escolhida['tarefa']}' de {pessoa_escolhida} marcada como concluida!")
                    
            elif escolha_a == 5:
                for i in range(3):
                    print("Encerrando o painel de ações" + "." * i, end="\r")
                    time.sleep(1)
                print("Encerrando o painel de ações...")
                break
        
############################################################################################

    elif escolha == 4:
        for i in range(3):
            print("Encerrando o sistema de tarefas" + "." * i, end="\r")
            time.sleep(1)
        print("Encerrando o sistema de tarefas...")
        break

    else:
        print("Numero invalido,escolha um numero valido.")