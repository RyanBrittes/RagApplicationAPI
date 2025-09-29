
while True:
    print("\n*****Seja bem vindo!!*****")
    print("\nEscolha uma das seguintes opções para continuar: ")
    opt = input("""\n01 - Iniciar uma conversa com o tutor
                   \n02 - Solicitar a criação de uma lista de exercícios
                   \n03 - Tirar dúvidas sobre um tema específico
                   \n04 - Sair\n""")
    match opt:
        case "01":
            print("\nEntrou em 01")

        case "02":
            print("\nEntrou em 02")

        case "03":
            print("\nEntrou em 03")

        case "04":
            print("\nEntrou em 04")
            break
        
        case _:
            print("\nValor não encontrado, tente novamente")
