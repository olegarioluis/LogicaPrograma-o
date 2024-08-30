# A. Print com o nome completo
print('Bem vindos a empresa do LF')

# B. Lista e a Variável com RU
lista_funcionarios = []
id_global = 48

# C. Função para cadastrar Funcionário
def cadastrar_funcionario(id):

    # C-a. Pergunta nome, setor e salàrio do Funcionário
    print('\n----MENU CADASTRAR FUNCIONÁRIO----')
    nome = input('Por favor entre com o nome Funcionário: ')
    setor = input('Por favor entre com o setor do Funcionário: ')
    salario = float(input('Por favor entre com o salário do Funcionário: '))

    # C-b. Armazena id, nome, setor e salario dentro de um dicionário
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }

    # C-c. Copia dicionário para dentro da lista
    lista_funcionarios.append(funcionario.copy())

# D. Fução Consulta Funcionário
def consultar_funcionarios():

    while True:

        # D-a. Menu de opções
        print('\n----MENU CONSULTA FUNCIONÁRIO---')
        print('Escolha a opção desejada:')
        print('1 - Consultar Todos os Funcionários')
        print('2 - Consultar Funcionário por ID')
        print('3 - Consultar Funcionário(s) por setor')
        print('4 - Retornar') 

        opcao = input('>> ')

        if opcao == '1':
            print('\nTodos os funcionários:')
            for funcionario in lista_funcionarios:
                print(funcionario)

        elif opcao == '2':
            id_consulta = int(input('Digite o id do funcionário: '))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario['id'] == id_consulta:
                    print('\nFuncionário encontrado:')
                    print(funcionario)
                    encontrado = True
                    break

            if not encontrado:
                print("Funcionário não encontrado.")

        elif opcao == '3':
            setor_consulta = input('Digite o setor do(s) funcionário(s): ')
            encontrados = []
            for funcionario in lista_funcionarios:
                if funcionario['setor'].lower() == setor_consulta.lower():
                    encontrados.append(funcionario)
            if encontrados:
                print(f"\nFuncionários do setor '{setor_consulta}':")
                for func in encontrados:
                    print(func)
            else:
                print(f"Nenhum funcionário encontrado no setor '{setor_consulta}'.")

        elif opcao == '4':
            return
        
        else:
            print('Opcão inválida')

# E. Função remove funcionário
def remover_funcionario():

    while True:

        id_remove = int(input('Digite o id do Funcionário a ser removido: '))
        funcionario_remover = None
        for funcionario in lista_funcionarios:
            if funcionario['id'] == id_remove:
                funcionario_remover = funcionario
                break

        if funcionario_remover:
            lista_funcionarios.remove(funcionario_remover)
            print('Funcionário removido com sucesso!')
            return
        
        else:
            print('Id inválido')

# F. Menu Principal
while True:

    print('\n----MENU PRINCIPAL----')
    print('Escolha a opção desejada:')
    print('1 - Cadastrar Funcionários')
    print('2 - Consultar Fincionário(s)')
    print('3 - Remover Funcionário')
    print('4 - Sair')

    opcao = input('>> ')

    if opcao == '1':
        id_global += 1
        cadastrar_funcionario(id_global)

    elif opcao == '2':
        consultar_funcionarios()

    elif opcao == '3':
        remover_funcionario()
    
    elif opcao == '4':
        print("Encerrando o programa...")
        break

    else:
        print("Opção inválida")

