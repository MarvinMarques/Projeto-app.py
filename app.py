import os

restaurantes = [{"nome":"Praça", "categoria":"Japonesa", "ativo":False}, 
                {"nome":"Pizza Suprema", "categoria":"Pizza", "ativo":True},
                {"nome":"Cantina", "categoria":"Italiano", "ativo":False}]

def exibir_nome_do_programa():
    print("""
░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░  
""")

def exibir_opções():
    print("1. Cadastrar restaurante")
    print("2. Listar restaurante")
    print("3. Ativar restaurante")
    print("4. Sair\n")

def finalizar_app():
    exibir_subtitulo("finalizar app")

def voltar_ao_menu_principal():
    input("\nAperte Enter para Voltar ao Menu ")
    main()

def opção_invalida():
    print("opção invalida!\n")
    voltar_ao_menu_principal()

def exibir_subtitulo(texto):
    os.system("cls")
    linha = "*" * (len(texto))
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    exibir_subtitulo("cadastro de novos restaurantes")
    nome_do_restaurante = input("digite o nome do restaurante para cadastra: ")
    categoria = input(f"Digite o Nome da Categoria{nome_do_restaurante}: ")
    dados_do_restaurante = {"nome":nome_do_restaurante, "categoria":categoria, "ativo":False}
    restaurantes.append(dados_do_restaurante)
    print(f"O restaurante {nome_do_restaurante} foi Cadastrado Com Sucesso!")

    voltar_ao_menu_principal()  

def lista_restaurantes():
    exibir_subtitulo("Listando Restaurantes")

    print(f"{"Nome Restaurantes".ljust(22)} | {"Categoria".ljust(20)} | Status")
    for restaurante in restaurantes:
        nome_restaurante = restaurante["nome"]
        categoria = restaurante["categoria"]
        ativo = "ativo" if restaurante["ativo"] else "desativado"
        print(f"- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {ativo}")
    voltar_ao_menu_principal()

def alternar_estado_restaurante():
    exibir_subtitulo('ALterando estado do restaurante')
    nome_restaurante = input('Digite o nome do restaurante que deseja alterar o estado: ')
    restaurante_encontrado = False

    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_encontrado = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O Restaurante {nome_restaurante} Foi Ativado Com Sucesso' if restaurante['ativo'] else f'O Restaurante {nome_restaurante} Foi Desativado Com Sucesso'
            print(mensagem)

        if not restaurante_encontrado:
            print("O Restaurante Não Foi Encontrado")
            
    voltar_ao_menu_principal()

def escolher_opção():
    try:
        opção_escolhida = int(input("Escolha uma opção: "))

        if opção_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opção_escolhida == 2:
            lista_restaurantes()
        elif opção_escolhida == 3:
            alternar_estado_restaurante()
        elif opção_escolhida == 4:
            finalizar_app()
        else:
            opção_invalida()
    except:
        opção_invalida()

def main():
    os.system("cls")
    exibir_nome_do_programa()
    exibir_opções()
    escolher_opção()

if __name__ == "__main__":
    main()