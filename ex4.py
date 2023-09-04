'''“Banco de dados” de dicionários.'''

'''Programa interativo de Banco de dados que armazena os dados digitados pelo usuario,
o mesmo define os campos obrigatórios e possiveis campos extras, o programa permite
filtrar por algum campo especifico ou imprimir todos os usuários cadastrados.'''


banco_usuarios = {} #dicionário global

''' Crie uma função cadastrar_usuario para cadastrar um usuário de maneira flexível'''

#função que cadastra o usuário, recebe uma tupla com os campos obrigatórios para cadastro dos usuários.
def cadastrar_usuario(campos_obrigatorios):
    usuario = {} #inicia vazio
    for campo in campos_obrigatorios:
        valor = input(f"Insira o valor para '{campo}': ")
        usuario[campo] = valor
    
    while True: #permite inserir varios campos extras até o usuario sair.
        campo_extra = input("Insira um campo extra ou 'sair' para continuar: : ")
        if campo_extra.lower() == 'sair':
            break
        valor_extra = input(f"Insira o valor '{campo_extra}': ")
        usuario[campo_extra] = valor_extra #insere no dicionario usuario
    
    nome_usuario = usuario.get(campos_obrigatorios[0]) #define o primeiro campo obrigatório como nome
    if nome_usuario: 
        banco_usuarios[nome_usuario] = usuario
        print("Usuário cadastrado!")
    else:
        print(f"Erro! O usuário deve ter um campo '{campos_obrigatorios[0]}' obrigatório.")

'''Criar uma outra função imprimir_usuarios com 4 possibilidades de invocação:'''

#funçã oermite imprimir os usuários com diferentes critérios
def imprimir_usuarios(*args, **kwargs):
    while True:
        print("------------Menu Impressão------------")
        print("|   1 - Imprimir todos os usuários   |")
        print("|   2 - Filtrar por nomes            |")
        print("|   3 - Filtrar por campos           |")
        print("|   4 - Filtrar por nomes e campos   |")
        print("|   0 - Voltar ao menu principal     |")
        print("--------------------------------------")
        sub_opcao = input("Escolha uma opção: ")
        
        if sub_opcao == '0':
            break
        elif sub_opcao == '1': #Imprime todos os usuários
            for nome, usuario in banco_usuarios.items():
                print(f"{nome}: {', '.join([f'{campo}: {valor}' for campo, valor in usuario.items()])}")
        elif sub_opcao == '2': 
            nomes = input("Insira os nomes separados por vírgula: ").split(',')
            for nome in nomes:
                nome = nome.strip()
                if nome in banco_usuarios:
                    usuario = banco_usuarios[nome]
                    print(f"{nome}: {', '.join([f'{campo}: {valor}' for campo, valor in usuario.items()])}")
                else:
                    print(f"Usuário '{nome}' não cadastrado no banco de dados.")
        elif sub_opcao == '3':
            criterios = {}
            while True:
                campo = input("Insira o campo para critério ou 'sair' para continuar: ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Insira o valor '{campo}': ")
                criterios[campo] = valor
            for nome, usuario in banco_usuarios.items():
                imprimir = True
                for campo, valor in criterios.items():
                    if campo not in usuario or usuario[campo] != valor:
                        imprimir = False
                        break
                if imprimir:
                    print(f"{nome}: {', '.join([f'{campo}: {valor}' for campo, valor in usuario.items()])}")
        elif sub_opcao == '4':
            nomes = input("Insira os nomes separados por vírgula: ").split(',')
            criterios = {}
            while True:
                campo = input("Insira o campo para critério ou 'sair' para continuar: ")
                if campo.lower() == 'sair':
                    break
                valor = input(f"Insira o valor '{campo}': ")
                criterios[campo] = valor
            for nome in nomes:
                nome = nome.strip()
                if nome in banco_usuarios:
                    usuario = banco_usuarios[nome]
                    imprimir = True
                    for campo, valor in criterios.items():
                        if campo not in usuario or usuario[campo] != valor:
                            imprimir = False
                            break
                    if imprimir:
                        print(f"{nome}: {', '.join([f'{campo}: {valor}' for campo, valor in usuario.items()])}")
                else:
                    print(f"Usuário '{nome}' não encontrado.")
        else:
            print("Opção inválida. Tente novamente.")



#função que define os campos obrigatorios para o cadastro.
def definir_campos_obrigatorios():
    campos_obrigatorios = ()
    while True: #define quais os campos são obrigatórios.
        campo_obrigatorio = input("Insira o campo que vai ser obrigatório ou 'sair' para voltar ao menu principal:") 
        if campo_obrigatorio.lower() == 'sair':
            break
        campos_obrigatorios += (campo_obrigatorio,)
    return campos_obrigatorios

#função que chama o menu principal para iniciar.
def menu_principal():
    campos_obrigatorios = definir_campos_obrigatorios()

    while True:
        print("-----------Menu-------------")
        print("| 1 - Cadastrar usuário    |")
        print("| 2 - Imprimir usuários    |")
        print("| 0 - Encerrar             |")
        print("----------------------------")
        opcao = input("Escolha uma opção: ")

        if opcao == '1':
            cadastrar_usuario(campos_obrigatorios)
        elif opcao == '2':
            imprimir_usuarios()
        elif opcao == '0':
            break
        else:
            print("Opção inválida!")

    print("Fim...")


menu_principal()
)
