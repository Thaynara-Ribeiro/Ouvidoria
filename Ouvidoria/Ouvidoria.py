print('''---- Menu da Ouvidoria ----
Selecione uma das opções abaixo:
1) Listar Manifestações
2) Adicionar Manifestação
3) Consultar Manifestação por Código
4) Remover Manifestação por Código
5) Encerrar Programa''')
manifestacoes = []
while True:
     escolha = int(input('Digite qual sua escolha: '))
     if escolha == 1:
         if len(manifestacoes) == 0:
             print('Não existe manifestações adicionadas até o momento')
         else:
             print('Lista de Manifestações')
             for i in manifestacoes:
                 print(f"Código: {i['codigo']}, Tipo: {i['tipo']}, Descrição: {i['descricao']}")
     elif escolha == 2:
        codigo = len(manifestacoes) + 1
        tipo = input('Digite o tipo da manifestação (Reclamação, Elogio, Sugestão): ')
        descricao = input('Digite a descrição da manifestação: ')
        manifestacoes.append({'codigo': codigo, 'tipo': tipo, 'descricao': descricao})
        print(f'Manifestação adicionada com código {codigo}.')
     elif escolha == 3:
         consulta = int(input('Digite qual o codigo da sua consulta: '))
         for i in manifestacoes:
            if i['codigo'] == consulta:
                print('Manifestação Encontrada')
                print(f"Código: {i['codigo']}, Tipo: {i['tipo']}, Descrição: {i['descricao']}")
     elif escolha == 4:
         codigoRemocao = int(input('Digite o codigo da manifestação que deseja remover: '))
         manifestacoes.pop(codigoRemocao-1)
         print('Manifestação Removida com Sucesso!')
     elif escolha == 5:
         print('Programa encerrado com sucesso!')
         break
