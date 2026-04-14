def menu_gerenciamento():
    opcao = 0  #comecamos a opcao com 0 so para entrar no menu pela primeira vez
    while opcao != 7: #  menu continua abrindo enquanto o usuario nao escolher a opcao de voltar
        print("\n=== MENU GERENCIAMENTO ===")
        print("1 - Cadastrar eleitor")
        print("2 - Listar eleitores")
        print("3 - Buscar eleitor")
        print("4 - Editar eleitor")
        print("5 - Remover eleitor")
        print("6 - Cadastrar candidato")
        print("7 - Voltar")
        try: #tenta transformar o que o usuario digitou em numero
            opcao = int(input("Escolha uma opcao: "))
        except ValueError: #se o usuario digitar letra ou algo invalido, a opcao vira 0 (ValueError)
            opcao = 0

        #a partir daqui o programa verifica qual numero foi escolhido
        match opcao:
            case 1:
                print("Cadastro de eleitor ainda nao foi feito.")
            case 2:
                print("Listagem de eleitores ainda nao foi feita.")
            case 3:
                print("Busca de eleitor ainda nao foi feita.")
            case 4:
                print("Edicao de eleitor ainda nao foi feita.")
            case 5:
                print("Remocao de eleitor ainda nao foi feita.")
            case 6:
                print("Cadastro de candidato ainda nao foi feito.")
            case 7:
                print("Voltando ao menu principal...")
            case _:
                print("Opcao invalida.")

def menu_abrir_votacao():
    opcao = 0
    while opcao != 3:
        print("\n=== ABRIR SISTEMA DE VOTACAO ===")
        print("1 - Identificar mesario")
        print("2 - Realizar zerezima")
        print("3 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Identificacao do mesario ainda nao foi feita.")
            case 2:
                print("Zerezima ainda nao foi feita.")
            case 3:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")

def menu_auditoria():
    opcao = 0
    while opcao != 3:
        print("\n=== AUDITORIA DA VOTACAO ===")
        print("1 - Exibir logs")
        print("2 - Exibir protocolos")
        print("3 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Exibicao de logs ainda nao foi feita.")
            case 2:
                print("Exibicao de protocolos ainda nao foi feita.")
            case 3:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")

def menu_resultados():
    opcao = 0
    while opcao != 5:
        print("\n=== RESULTADOS DA VOTACAO ===")
        print("1 - Boletim de urna")
        print("2 - Estatistica de comparecimento")
        print("3 - Votos por partido")
        print("4 - Validacao de integridade")
        print("5 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Boletim de urna ainda nao foi feito.")
            case 2:
                print("Estatistica de comparecimento ainda nao foi feita.")
            case 3:
                print("Votos por partido ainda nao foram feitos.")
            case 4:
                print("Validacao de integridade ainda nao foi feita.")
            case 5:
                print("Voltando ao menu de votacao...")
            case _:
                print("Opcao invalida.")

def menu_votacao():
    opcao = 0
    while opcao != 4:
        print("\n=== MENU VOTACAO ===")
        print("1 - Abrir sistema de votacao")
        print("2 - Auditoria da votacao")
        print("3 - Resultados da votacao")
        print("4 - Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                menu_abrir_votacao()
            case 2:
                menu_auditoria()
            case 3:
                menu_resultados()
            case 4:
                print("Voltando ao menu principal...")
            case _:
                print("Opcao invalida.")

def menu_principal():
    opcao = 0
    while opcao != 3:
        print("\n=== SISTEMA LAD.PY ===")
        print("1 - Gerenciamento")
        print("2 - Votacao")
        print("3 - Sair")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                menu_gerenciamento()
            case 2:
                menu_votacao()
            case 3:
                print("Saindo...")
            case _:
                print("Opcao invalida.")