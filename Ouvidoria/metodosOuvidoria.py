def listarManifestacao(manifestacoes):
        if len(manifestacoes) == 0:
            print('Não existe manifestações adicionadas até o momento')
        else:
            print('Lista de Manifestações')
            for i in manifestacoes:
                print(f"Código: {i['codigo']}, Tipo: {i['tipo']}, Descrição: {i['descricao']}")

def adicionarManifestacao(manifestacoes):
    codigo = len(manifestacoes) + 1
    tipo = input('Digite o tipo da manifestação (Reclamação, Elogio, Sugestão): ')
    descricao = input('Digite a descrição da manifestação: ')
    manifestacoes.append({'codigo': codigo, 'tipo': tipo, 'descricao': descricao})
    print(f'Manifestação adicionada com código {codigo}.')

def consultaManifestacao(manifestacoes):
    consulta = int(input('Digite qual o codigo da sua consulta: '))
    for i in manifestacoes:
        if i['codigo'] == consulta:
            print('Manifestação Encontrada')
            print(f"Código: {i['codigo']}, Tipo: {i['tipo']}, Descrição: {i['descricao']}")

def removerManifestacao(manifestacoes):
    codigoRemocao = int(input('Digite o codigo da manifestação que deseja remover: '))
    manifestacoes.pop(codigoRemocao - 1)
    print('Manifestação Removida com Sucesso!')