def menu_gerenciamento ():
    opcao = 0
    while opcao != 11:
        print("\n=====MENU GERENCIAMENTO=====")
        print(" 1 para cadastro e validação de novos eleitores")
        print(" 2 para remover um eleitor")
        print(" 3 para editar dados de eleitores")
        print(" 4 para buscar eleitores")
        print(" 5 para listar eleitores")        
        print(" 6 para cadastrar e validar candidato")
        print(" 7 para editar candidatos")
        print(" 8 para remover candidatos")
        print(" 9 para buscar candidatos")
        print(" 10 para listar candidatos")
        print("11 para voltar")
        try:
            opcao = int (input("escolha uma opção de 1 a 11: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Cadastrar e validar novos eleitores")
            case 2:
                print("Remover um eleitor")
            case 3:
                print("Editar dados de eleitores")
            case 4:
                print("Buscar eleitores")
            case 5:
                print("Listar eleitores")
            case 6:
                print("Cadastrar e validar candidatos")               
            case 7:
                print("Editar candidatos")
            case 8:
                print("Remover candidatos")
            case 9:
                print("Buscar candidatos")
            case 10:
                print("Listar candidatos")
            case 11:
                print("Voltando")
            case _:
                print("Opção inválida")
            

def menu_abrir_votacao():
    opcao = 0
    while opcao != 4:
        print("\n===== ABRIR SISTEMA DE VOTACAO =====")
        print("1 para dados do eleitor e validação")
        print("2 para verificar se é mesário")
        print("3 para Zeríssima")
        print("4 para voltar")
        
        try:
            opcao=int(input("escolha uma opção de 1 a 4: "))
        except ValueError:
            opcao = 0
        
        match opcao:
            case 1:
                print("Dados do eleitor e validação")
            case 2:
                print("Verificar se é mesário")
            case 3:
                print("Zeríssima")
            case 4:
                print("Voltando")
            case _:
                print("Opção inválida")


def processo_votacao():
    opcao = 0
    while opcao != 4:
        print("\n===== VOTAÇÃO =====")
        print("1 para identificação do eleitor e validação para prosseguir")
        print("2 para seleção do candidato")
        print("3 para registro e finalização do voto")
        print("4 para voltar")
        try:
            opcao=int(input("escolha uma opção de 1 a 4:"))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Identificação e valiadação do eleitor")
            case 2:
                print("Seleção do candidato")
            case 3:
                print("Registro e finalização do voto")
            case 4:
                print("Voltando")    
            case _:
                print("Opção inválida")


def Encerramento_votacao():
    opcao = 0
    while opcao != 3:
        print("\n=====ENCERRAMENTO DA VOTAÇÃO=====")  
        print("1 para autenticação do mesário")
        print("2 para confirmação de encerramento") 
        print("3 para protocolo de fechamento definitivo")
        print("4 para voltar")

        try:
            opcao=int(input("escolha uma opção de 1 a 4:"))
        except ValueError:
            opcao = 0
            
        match opcao:
            case 1:
                print("Autenticação do mesário")
            case 2:
                print("Confirmação de encerramento")
            case 3:
                print("Protocolo de fechamento definitivo")
            case 4:
                print("Voltando")
            case _:
                print("Opção inválida")



def fim_votacao():
    opcao = 0
    while opcao != 5:
        print("\n===== RESULTADOS DA VOTACAO =====")
        print("1 para boletim de urna")
        print("2 para estatistica de comparecimento")
        print("3 para votos por partido")
        print("4 para validacao de integridade")
        print("5 para Voltar")
        try:
            opcao=int(input("escolha uma opção de 1 a 5:"))
        except ValueError:
            opcao = 0
        
        match opcao:
            case 1:
                print("Boletim de urna")
            case 2:
                print("Estatistica de comparecimento")
            case 3:
                print("Votos por partido")
            case 4:
                print("Validacao de integridade")
            case 5:
                print("Voltando")
            case _:
                print("opção inválida")



def menu_auditoria():
    opcao = 0
    while opcao != 3:
        print("\n=== AUDITORIA DA VOTACAO ===")
        print("1 para Exibir logs")
        print("2 para Exibir protocolos")
        print("3 para Voltar")
        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                print("Exibicao de logs ")
            case 2:
                print("Exibicao de protocolos ")
            case 3:
                print("Voltando")
            case _:
                print("Opcao invalida.")



def menu_votacao():
    opcao = 0
    while opcao != 4:
        print("\n===== MENU VOTACAO =====")
        print("1 - Abrir sistema de votacao")
        print("2 - processo da votação")
        print("3 - Encerramento da votação")
        print("4 - Fim da votacao")
        print("5 - Auditoria")

        try:
            opcao = int(input("Escolha uma opcao: "))
        except ValueError:
            opcao = 0

        match opcao:
            case 1:
                menu_abrir_votacao()
            case 2:
                processo_votacao()
            case 3:
                Encerramento_votacao()
            case 4:
                fim_votacao()
            case 5:
                menu_auditoria()
            case _:
                print("Opcao invalida.")



def menu_principal():
    opcao = 0
    while opcao != 3:
        print("\n===== MENU PRINCIPAL =====")
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