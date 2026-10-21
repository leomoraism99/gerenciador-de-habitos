from datetime import datetime, date

def pedir_entrada(mensagem):
    entrada = input(mensagem).strip()
    if entrada.lower() == 'menu':
        return None
    return entrada


def menu_pos_acao():
    while True:
        print("\nO que deseja fazer agora?")
        print("1. Cadastrar outro hábito")
        print("2. Ir para o Menu Principal")
        print("3. Excluir algum hábito?")
        print("4. Concluir algum hábito?")
        print("5. Consultar hábito")

        opcao_pos = input("Escolha uma opção: ").strip()

        if opcao_pos == "1":
            cadastrar_habito()
            break
        elif opcao_pos == "2":
            break
        elif opcao_pos == "3":
            excluir_habito()
            break
        elif opcao_pos == "4":
            concluir_habito()
            break
        elif opcao_pos == "5":
            consultar_habito()
            break
        else:
            print("Opção inválida!")


def exibir_cabecalho(titulo):
    print("\n" + "=" * 50)
    print(titulo.upper().center(50))
    print("=" * 50 + "\n")


def cadastrar_habito():
    print("\n--- CADASTRAR NOVO HÁBITO ---\n")
    print("(Digite 'menu' a qualquer momento para voltar ao menu pincipal.)")

    nome= pedir_entrada("Digite o nome do hábito: ")
    if nome is None or nome == "":
        return
    print("\nQual a frequência deste hábito?")
    print("1. Diário (todos os dias)")
    print("2. Semanal (X vezes por semana)")
    print("3. Mensal (X vezes por mês)")
    opcao_freq = pedir_entrada("Escolha uma opção (1, 2 ou 3)\n")
    if opcao_freq is None:
        return

    if opcao_freq == '1':
        frequencia = "Diário"
        meta_ciclo = 1
    elif opcao_freq == '2':
        frequencia = "Semanal"
        entrada = pedir_entrada("Quantas vezes por semana deseja realizar este hábito? ")
        if entrada is None:
            return
        if not entrada.isdigit():
            print("\nDigite apenas números para a meta!")
            return
        meta_ciclo = int(entrada)
    elif opcao_freq == '3':
        frequencia = "Mensal"
        entrada = pedir_entrada("Quantas vezes por mês deseja realizar este hábito? ")
        if entrada is None:
            return
        if not entrada.isdigit():
            print("\nDigite apenas números para a meta!")
            return
        meta_ciclo = int(entrada)
    else:
        print("Opção inválida!")
        return

    novo_habito = {
        "nome": nome,
        "frequencia": frequencia,
        "meta_ciclo": meta_ciclo,
        "progresso_ciclo": 0,
        "streak": 0,
        "ultima_conclusao": None,
        "status": "ativo",
        "data_inicio": date.today().isoformat()
    }
    lista_habitos.append(novo_habito)
    print(f"\nHábito '{nome}' cadastrado com sucesso!\n")
    menu_pos_acao()

lista_habitos = []
historico_eventos = []

def consultar_habito():
    print("\n--- SEUS HÁBITOS ---\n")
    print("(Digite 'menu' a qualquer momento para voltar ao menu pincipal.)")
    if not lista_habitos:
        print("Nenhum hábito cadastrado.")
        return
    for i, habito in enumerate(lista_habitos, start=1):
        print(f"[{i}] {habito['nome']}")
        print(f"    ├── Frequência: {habito['frequencia']} (Meta: {habito['meta_ciclo']}x)")
        print(f"    ├── Progresso: {habito['progresso_ciclo']}/{habito['meta_ciclo']}")
        print(f"    └── Streak: {habito['streak']} 🔥\n")

    entrada = pedir_entrada("\nPressione ENTER para continuar (ou 'menu' para voltar): ")
    if entrada is None:
     return

menu_pos_acao()
        
def concluir_habito():
    print("\n--- CONCLUIR HÁBITO ---\n")
    print("(Digite 'menu' a qualquer momento para voltar ao menu pincipal.)")
    if not lista_habitos:
        print("Nenhum hábito cadastrado.")
        return
    print("Seus hábitos atuais:\n")
    for i, habito in enumerate(lista_habitos, start=1):
        print(f"[{i}] {habito['nome']} - Progresso: {habito['progresso_ciclo']}/{habito['meta_ciclo']}")
        print()
    print()
    entrada = pedir_entrada("Digite o número do hábito que deseja fazer o check de hoje! ")
    if entrada is None:
        return
    if not entrada.isdigit():
        print("\nOpção inválida! Selecione um número da lista.")
        return
    indice = int(entrada) - 1
    
    if 0 <= indice < len(lista_habitos):
        habito_selecionado = lista_habitos[indice]
        if habito_selecionado['progresso_ciclo'] >= habito_selecionado['meta_ciclo']:
            print(f"\n🛑 O hábito '{habito_selecionado['nome']}' já atingiu a meta deste ciclo!")
        else:
            habito_selecionado['progresso_ciclo'] += 1
    
            if habito_selecionado['progresso_ciclo'] >= habito_selecionado['meta_ciclo']:
                habito_selecionado['streak'] += 1
                print(f"\n🎉 Parabéns! Você atingiu sua meta de '{habito_selecionado['nome']}'!")
            else:
                print(f"\n✅ Check de hoje feito!\nProgresso atual: {habito_selecionado['progresso_ciclo']}/{habito_selecionado['meta_ciclo']}")
    else:
        print("\nOpção inválida! Selecione um número da lista.")
        return
    menu_pos_acao()

def vrf_rnv_ciclos():
    hoje = date.today()
    for habito in lista_habitos:
        data_inicio = datetime.strptime(habito["data_inicio"], "%Y-%m-%d").date()
        dias_passados = (hoje - data_inicio).days

        if habito["frequencia"] == "Diário":
            intervalo = 1
        elif habito["frequencia"] == "Semanal":
            intervalo = 7
        elif habito["frequencia"] == "Mensal":
            intervalo = 30
        else:
            continue
        if dias_passados >= intervalo:
            if habito["progresso_ciclo"] < habito["meta_ciclo"]:
                habito["streak"] = 0
        habito["progresso_ciclo"] = 0
        habito["data_inicio"] = hoje.isoformat()

def menu_principal():
    exibir_cabecalho("GERENCIADOR DE HÁBITOS")
    print("O seu diário de evolução pessoal e acompanhamento")
    print("de metas diárias, streaks e conquistas.\n")
    
    input("Pressione ENTER para aceder ao menu principal...\n")
    while True:
        vrf_rnv_ciclos()
        exibir_cabecalho("MENU PRINCIPAL")
        print('1. Cadastrar hábito')
        print('2. Consultar hábito')
        print('3. Concluir hábito')
        print('4. Gerenciar hábitos (Excluir, Arquivar)')
        print('5. Consultar histórico de hábitos')
        print('6. Sair')
        opcao = input('Escolha uma opção: ')
        if opcao == '1':
            print("'Cadastrar hábito' selecionado.")
            cadastrar_habito()
        elif opcao == '2':
            print("'Consultar hábito' selecionado.")
            consultar_habito()
        elif opcao == '3':
            print("'Concluir hábito' selecionado.")
            concluir_habito()
        elif opcao == '4':
            print("'Gerenciar hábitos' selecionado.")
        elif opcao == '5':
            print("'Consultar histórico de hábitos' selecionado.")
        elif opcao == '6':
            print("'Sair' selecionado.")
            break
        else:
            print('Opção inválida. Por favor, escolha uma opção válida.')
menu_principal()

