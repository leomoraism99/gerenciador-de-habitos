def exibir_cabecalho(titulo):
    print("\n" + "=" * 50)
    print(titulo.upper().center(50))
    print("=" * 50 + "\n")


def cadastrar_habito():
    print("\n--- CADASTRAR NOVO HÁBITO ---")
    print("(Digite 'menu' a qualquer momento para voltar ao menu pincipal.)")

    nome= input("Digite o nome do hábito: ")
    if nome.lower() == 'menu' or nome == "":
        return
    print("\nQual a frequência deste hábito?")
    print("1. Diário (todos os dias)")
    print("2. Semanal (X vezes por semana)")
    print("3. Mensal (X vezes por mês)")
    opcao_freq = input("Escolha uma opção (1, 2 ou 3)\n").strip()
    if opcao_freq == 'menu':
        return
    if opcao_freq == '1':
        frequencia = "Diário"
        meta_ciclo = 7
    elif opcao_freq == '2':
        frequencia = "Semanal"
        entrada = (input("Quantas vezes por semana deseja realizar este hábito? "))
        if entrada.lower() == 'menu':
            return
        meta_ciclo = int(entrada)
    elif opcao_freq == '3':
        frequencia = "Mensal"
        entrada = (input("Quantas vezes por mês deseja realizar este hábito? "))
        if entrada.lower() == 'menu':
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
        "status": "ativo"
    }
    lista_habitos.append(novo_habito)
    print(f"\nHábito '{nome}' cadastrado com sucesso!\n")
    while True:
        print("\nO que deseja fazer agora?")
        print("1. Cadastrar outro hábito")
        print("2. Ir para o Menu Principal")
        
        opcao_pos = input("Escolha uma opção: ").strip()

        if opcao_pos == "1":
            cadastrar_habito()
            break
        elif opcao_pos == "2":
            break
        else:
            print("Opção inválida!")

lista_habitos = []
historico_eventos = []

def menu_principal():
    exibir_cabecalho("GERENCIADOR DE HÁBITOS")
    print("O seu diário de evolução pessoal e acompanhamento")
    print("de metas diárias, streaks e conquistas.\n")
    
    input("Pressione ENTER para aceder ao menu principal...\n")
    while True:
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
        elif opcao == '3':
            print("'Concluir hábito' selecionado.")
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