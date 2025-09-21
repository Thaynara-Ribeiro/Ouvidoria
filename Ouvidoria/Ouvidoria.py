print('''---- Menu da Ouvidoria ----
Selecione uma das opções abaixo:
1) Listar Manifestações
2) Adicionar Manifestação
3) Consultar Manifestação por Código
4) Remover Manifestação por Código
5) Encerrar Programa''')
manifestações = []
escolha = 0 
while escolha != 5:
    escolha = int(input('Digite o número da opção desejada: '))
    if escolha == 1:
        if len(manifestações) == 0:
            print('Nenhuma manifestação cadastrada.')
        else:
            for manifestação in manifestações:
                print(f"Código: {manifestação['código']}, Tipo: {manifestação['tipo']}, Descrição: {manifestação['descrição']}")
    elif escolha == 2:
        código = len(manifestações) + 1
        tipo = input('Digite o tipo da manifestação (Reclamação, Elogio, Sugestão): ')
        descrição = input('Digite a descrição da manifestação: ')
        manifestações.append({'código': código, 'tipo': tipo, 'descrição': descrição})
        print(f'Manifestação adicionada com código {código}.')
    elif escolha == 3:
        código_consulta = int(input('Digite o código da manifestação que deseja consultar: '))
        encontrada = False
        for manifestação in manifestações:
            if manifestação['código'] == código_consulta:
                print(f"Código: {manifestação['código']}, Tipo: {manifestação['tipo']}, Descrição: {manifestação['descrição']}")
                encontrada = True
                break
        if not encontrada:
            print('Manifestação com esse código não encontrada.')
    elif escolha == 4:
        código_remover = int(input('Digite o código da manifestação que deseja remover: '))
        encontrada = False
        for i, manifestação in enumerate(manifestações):
            if manifestação['código'] == código_remover:
                del manifestações[i]
                print(f'Manifestação com código {código_remover} removida.')
                encontrada = True
                break
        if not encontrada:
            print('Manifestação com esse código não encontrada.')
    elif escolha == 5:
        print('Programa encerrado.')
    else:
        print('Opção inválida. Tente novamente.')